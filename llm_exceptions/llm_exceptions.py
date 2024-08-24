from __future__ import print_function
import traceback
from IPython.display import Markdown, display_markdown, display, HTML
import re
import os
import requests
import json

import html
from markdown import markdown

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic, 
                                register_line_magic, register_cell_magic,
                                register_line_cell_magic)
from IPython.core.magic_arguments import (
    argument, magic_arguments, parse_argstring)


import traceback
from functools import partial

# from fireworks.client import Fireworks


def get_chunks(s):
  pattern = r'```(.*)'
  matches = re.finditer(pattern, s)
  chunks = []
  position = 0
  lang=''
  for match in matches:
    # print(match.group(), match.span())
    chunks.append({
        'content': s[position:match.span()[0]],
        'lang': None if lang=='' else lang
    })
    lang = match.group().split('```')[1]
    position = match.span()[1]

  chunks.append({
        'content': s[position:],
        'lang': None
    })
  return chunks

def get_chunks_error(s):
  # loop through the lines and see if ``` is in there
  lines = s.split('\n')
  chunks=[]
  tick_counter = 0
  content_list=[]
  lang=None
  for line in lines:
    if '```' in line:
      tick_counter+=1
      content = '\n'.join(content_list)
      content = content.strip()
      if content and content!='```':
        chunks.append({
            'content':content,
            'lang': lang
        })
      content_list=[]
      # if start get lang or none
      if tick_counter%2==1: # start => get new lang
        lang = line.split('```')[1]
        lang = 'error' if lang=='' else lang
      else: # closing ``` => reset lang to None
        lang=None

    else:
      # print(f'adding line to content_list: {line}')
      content_list.append(line)

  content_list.append(line)
  content = '\n'.join(content_list)
  content = content.strip()

  if content and content!='```':
    # print(f'adding ***{content}***')
    chunks.append({
        'content':content,
        'lang': None
    })
  return chunks

def chunks_to_html(chs):
  formatter = HtmlFormatter(linenos=True, cssclass="source")
  fstyle = formatter.get_style_defs(arg='')
  CSS='''
.error {
    color: #C72C41; /* Dark Red */
    background-color: #F8D7DA; /* Light Pink */
    padding: 10px;
    border: 1px solid #C72C41; /* Optional border to highlight */
    border-radius: 4px; /* Optional rounded corners */
}
.solution{
    color: #5B3A29;
    background-color: #F5F5DC;
    padding: 10px;
    border: 1px solid #4CAF50; /* Optional border to highlight */
    border-radius: 4px; /* Optional rounded corners */
}
.code-block {
    background-color: #333333;
    padding: 10px;
    border: 1px solid #E0E0E0; /* Soft Gray */
    border-radius: 4px; /* Optional rounded corners */
    overflow-x: auto; /* Handle overflow for long lines */
    margin: 5px 0;
}
  '''
  html_content=f'''
  <style>
  {fstyle}
  {CSS}
  </style>

  '''
  for chunk in chs:
    if chunk['lang']=='error':
      content = chunk['content']
      content = html.escape(content)
      html_content+=f'''
      <p class="error">
        {content}
      </p>
      '''
    elif chunk['lang']:
      lexer = get_lexer_by_name(chunk['lang'], stripall=True)
      html_content+="<div class=code-block>"+highlight(chunk['content'], lexer, formatter)+'</div>'
    else:
      html_content+="<div class=solution>"+markdown(chunk['content'])+'</div>'
  return html_content

def md_to_html(md):
  chunks = get_chunks_error(md)
  html_content = chunks_to_html(chunks)
  return html_content


# client = Fireworks(api_key=os.environ.get('FIREWORKS_API_KEY'))
def get_error_messages_8b(error, HF_TOKEN=None, show_html=True):
  print(f'HF_TOKEN: {HF_TOKEN}')
  # print(error)
  headers = {"Authorization": f"Bearer {HF_TOKEN}"}
  url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
  # start: set up prompts for Llama3-8b-instruct
  systemTemplate = "<|start_header_id|>system<|end_header_id|>\n{text}<|eot_id|>\n\n"
  systemMessage = '''You are a helpful python code debugger. 
I will give you the code that I input and the error that I just received from my code. 
First, you will repeat the error. and then you explain the steps to debug the error. 
Feel free to output any code that would fix the error. 
Your response must be short and concrete.
'''
  systemPrompt = systemTemplate.format(text=systemMessage)
  userTemplate = '<|start_header_id|>user<|end_header_id|>\n{text}<|eot_id|>\n\n'
  assistantTag = '<|start_header_id|>assistant<|end_header_id|>\n'

  prompt = systemPrompt + userTemplate.format(text=error) + assistantTag
  # end: set up prompts for Llama3-8b-instruct

  # messages = [
  #     {'role':'system', 'content':'You are a helpful code debugger. I will give you an error that I just received from my code. First, you will repeat the error. and then you explain the steps to debug the error. Feel free to output any code that would fix the error. Your response must be short and concrete.'},
  #     {'role':'user', 'content':f'```{error}```'},

  # ]
  # response = client.chat.completions.create(
  # model="accounts/fireworks/models/llama-v3p1-405b-instruct",
  # model="accounts/fireworks/models/llama-v3p1-8b-instruct",
  # max_tokens= 16384,
  # temperature= 0.01,
  # messages= messages
  # )
  # content = response.choices[0].message.content
  body = {
    "inputs": prompt,
    'parameters': {
        # temperature: 0.0001,
        'max_new_tokens': 1000,
        'return_full_text': False,
  }}
  data = requests.post(url, json=body, headers=headers)
  if not data.ok:
    print('\nUnable to contact {url}')
    return error + '\nUnable to contact {url}'
  else:
    content = json.loads(data.content)[0]['generated_text']
  if show_html:
    html = md_to_html(content)
    # display_markdown(md)
    display(HTML(html))
    display_markdown(Markdown('-'*20))
  else:
    display_markdown(content, raw=True)

  return content



def llm_handler(self, etype, value, tb, tb_offset=None, kernel=None, HF_TOKEN=None, **kwargs):

  tail = kernel.history_manager.get_tail(include_latest=True)
  cell_input = tail[-1][2]
  # print(f'cell input: {cell_input}')
  # print('-'*50)
  s = traceback.format_exc()
  print(s)
  display_markdown(Markdown('-'*20))
  stack = traceback.extract_tb(tb, limit=None)
  # print(f'Exception: {etype} \nvalue: {value}\ntraceback: {stack}')
  # print('-'*50)

  try:
    md = Markdown('**LLM:**')
    display_markdown(md)
    llm_input = f'''Input code:
{cell_input}
Error:
{s}
'''
    # print('-'*50)
    # print(llm_input)
    # print('-'*50)
    resp = get_error_messages_8b(llm_input, HF_TOKEN=HF_TOKEN, **kwargs)
    # print(resp)
  except Exception as e:
    print('Cannot get LLM solution:')
    print(e)
    # stack = traceback.extract_tb(tb, limit=None)
    # print('-'*50)
    # print(f'Exception: {etype} \nvalue: {value}\ntraceback: {stack}')
    # print('-'*50)


# @magics_class
# class LLMExceptions(Magics):

#     @line_magic
#     def llm_magic(self, line):
#         self.shell.set_custom_exc((Exception,), partial(llm_handler, kernel = self.shell))

#     @register_line_cell_magic
#     def llm_magic_init(self, line, cell=None):
#         self.shell.set_custom_exc((Exception,), partial(llm_handler, kernel = self.shell))

#     @cell_magic
#     def llm_cell_magic(self, line, cell):
#         self.llm_magic(line)

#     @line_cell_magic
#     def llm_line_cell_magic(self, line, cell=None):
#         self.llm_magic(line)
