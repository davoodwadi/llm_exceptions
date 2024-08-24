"""LLM Exceptions Jupyter Magic"""
__version__ = '0.0.1'
import sys
# from .llm_exceptions import LLMExceptions
from .llm_exceptions import llm_handler
from functools import partial

import IPython
# from IPython.core.magic_arguments import (
#     argument, magic_arguments, parse_argstring)


# @magic_arguments()
# @argument(
#     '-v', '--show_html', default=False,
#     help="Whether to show the LLM output as colored html or simple markdown"
#     )
def load_ipython_extension(ipython=None, show_html=True):
    if ipython is None:
        ipython = IPython.get_ipython()

    if ipython is None:
        raise RuntimeError("Can't load llm_exceptions. No IPython kernel found.")

    print(show_html)
    # args = parse_argstring(load_ipython_extension, 'line')
    # print(args)
    ipython.set_custom_exc((Exception,), partial(llm_handler, kernel = ipython, show_html=False))
    print('llm_exceptions loaded successfully!')
    # ipython.register_magics(LLMExceptions)

# if "ipykernel" in sys.modules:
#     kernel = get_ipython()
#     print(kernel)
#     load_ipython_extension(kernel)