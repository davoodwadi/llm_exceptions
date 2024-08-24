# LLM Exceptions

**LLM Exceptions** is a Python package that enhances your debugging experience by automatically explaining stack traces for all exceptions. It leverages large language models to provide explanations and potential solutions for errors in your code. This tool is particularly useful for those who are beginners to python and apprehend the countless errors they face.

## Features

- **Automatic Error Analysis**: Automatically captures stack traces from exceptions and provides detailed explanations and potential solutions.
- **Easy Integration**: Simple to set up in Jupyter Notebooks or Google Colab.
- **Explained by LLMs**: Uses large language models to generate accurate and helpful explanations.

## Installation

You can install the package using `pip`:

```bash
pip install llm-exceptions
```

## Setup

To use the package, you'll need to set the `HF_TOKEN` environment variable with your Hugging Face API token. This token is required to access the large language models. The default model is `meta-llama/Meta-Llama-3-8B-Instruct`.

You can set the environment variable in your terminal like this:

```bash
export HF_TOKEN='your_hugging_face_token'
```

Or, set it directly in your Python script or Jupyter Notebook:

```python
import os
os.environ['HF_TOKEN'] = 'your_hugging_face_token'
```

## Usage

To use **LLM Exceptions** in a Jupyter Notebook or Google Colab, load the extension with the following magic command:

```python
%load_ext llm_exceptions
```

Once the extension is loaded, simply run your code as usual. If an exception occurs, **LLM Exceptions** will automatically analyze the stack trace and provide a detailed explanation along with potential solutions.

### Example

1. Load the extension in your notebook:

   ```python
   %load_ext llm_exceptions
   ```

2. Run some code that produces an error:

   ```python
   def divide(a, b):
       return a / b

   divide(5, 0)
   ```

3. When the error occurs, **LLM Exceptions** will provide an explanation:

   ```
   ZeroDivisionError: division by zero
   ```

   > **LLM Explanation**:
   > The error `ZeroDivisionError` occurs because you are attempting to divide a number by zero, which is mathematically undefined. To fix this error, ensure that the divisor `b` is not zero before performing the division.

## Citations

If you use **LLM Exceptions** in your research or project, please consider citing it as follows:

```
@software{llm_exceptions,
author = {Davood Wadi},
title = {LLM Exceptions: Automatic Stack Trace Analysis and Solutions},
year = {2024},
url = {https://github.com/davoodwadi/llm_exceptions},
note = {Version 0.0.4}
}
```

## License

This project is licensed under the Apache-2.0 license. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you encounter any problems or have suggestions for improvements.

## Acknowledgements

This package uses large language models provided by Hugging Face. Make sure to sign up on their platform to obtain the necessary API token.
