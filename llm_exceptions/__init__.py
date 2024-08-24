"""LLM Exceptions Jupyter Magic"""
import os
import sys

from .llm_exceptions import llm_handler
from functools import partial

import IPython

HF_TOKEN = os.environ.get('HF_TOKEN')
if not HF_TOKEN:
    raise ValueError("HF_TOKEN is is not added as an environment variable.")

def load_ipython_extension(ipython=None, show_html=True):
    if ipython is None:
        ipython = IPython.get_ipython()

    if ipython is None:
        raise RuntimeError("Can't load llm_exceptions. No IPython kernel found.")

    ipython.set_custom_exc((Exception,), partial(llm_handler, kernel = ipython, show_html=False, HF_TOKEN=HF_TOKEN))
    print('llm_exceptions loaded successfully!')
    # ipython.register_magics(LLMExceptions)

# if "ipykernel" in sys.modules:
#     kernel = get_ipython()
#     print(kernel)
#     load_ipython_extension(kernel)