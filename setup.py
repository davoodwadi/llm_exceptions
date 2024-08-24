from setuptools import setup, find_packages

setup(
    name='llm_exceptions',
    version='0.0.1',
    description='LLM explains stack trace for all exceptions. It automatically takes your input code and the error and tries to give a solution.',
    author='Davood Wadi',
    author_email='davoodwadi@gmail.com',
    url='davoodwadi.github.io',
    packages=find_packages(),
    install_requires=[
        'ipython',
        'markdown',
        'fireworks-ai'
    ],
    # entry_points={
    #     'ipython_extensions': [
    #         'llm_exceptions = llm_exceptions:load_ipython_extension',
    #     ]
    # },
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
        'License :: OSI Approved :: MIT License',  # Or specific license if you have one
    ],
    python_requires='>=3.6',
)