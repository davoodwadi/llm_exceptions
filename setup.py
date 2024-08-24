from setuptools import setup, find_packages
from pathlib import Path
from llm_exceptions import __version__ as v

readme_file = Path("README.md").read_text()

setup(
    name='llm_exceptions',
    version=v,
    description='LLM explains stack trace for all exceptions. It automatically takes your input code and the error and tries to give a solution.',
    author='Davood Wadi',
    author_email='davoodwadi@gmail.com',
    url='https://github.com/davoodwadi/llm_exceptions',
    long_description_content_type='text/markdown',
    long_description=readme_file,
    packages=find_packages(),
    install_requires=[
        'ipython',
        'markdown',
        'fireworks-ai'
    ],
    entry_points={
        'jupyter.commands': [
            'llm_exceptions = llm_exceptions:load_ipython_extension',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Jupyter',
        'Framework :: IPython',
        'License :: OSI Approved :: Apache Software License',
    ],
    python_requires='>=3.6',
)