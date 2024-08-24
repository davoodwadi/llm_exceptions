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

To use the package, you'll first need a Hugging Face API token. If you don't have a token, you can get one by signing up on [Hugging Face](https://huggingface.co/). The token will give you acces to the underlying LLM as an API. The default model is `meta-llama/Meta-Llama-3-8B-Instruct`.

Then set the `HF_TOKEN` environment variable with your Hugging Face API token. You can set the environment variable in your terminal like this:

### MacOS/Linux

```bash
export HF_TOKEN='your_hugging_face_token'
```

Or, set it directly in your Python script or Jupyter Notebook:

```python
import os
os.environ['HF_TOKEN'] = 'your_hugging_face_token'
```

### Setting Up in Google Colab

To use **LLM Exceptions** in Google Colab, follow these steps:

1.  **Install the Package**:

    Run the following command in a Colab cell to install the package:

    ```python
    !pip install llm-exceptions
    ```

2.  **Set the Hugging Face Token**:

    In Google Colab, environment variables are handled differently from Jupyter notebooks. You have two options:

    i. In the `Secrets` button on the left bar, you can set your `HF_TOKEN` and give it `Notebook access` by toggling the button on.

    Or,

    ii. You can set the `HF_TOKEN` environment variable with your Hugging Face API token directly in a cell (this is _less_ safe):

    ```python
    import os
    os.environ['HF_TOKEN'] = 'your_hugging_face_token'
    ```

    Replace `'your_hugging_face_token'` with your actual Hugging Face API token. If you don't have a token, you can get one by signing up on [Hugging Face](https://huggingface.co/).

3.  **Load the LLM Exceptions Extension**:

    Load the extension using the following magic command:

    ```python
    %load_ext llm_exceptions
    ```

    Once loaded, the extension will automatically capture and analyze any exceptions in your code.

4.  **Run Your Code**:

    Now you can run your code as usual. If an exception occurs, **LLM Exceptions** will provide an explanation and potential solution right within the Colab environment.

Once you do that, `LLM-Exceptions` will works automatically to explain your errors.

## Usage

To use **LLM Exceptions** in a Jupyter Notebook or Google Colab, load the extension with the following magic command:

```python
%load_ext llm_exceptions
```

Once the extension is loaded, simply run your code as usual. If an exception occurs, **LLM Exceptions** will automatically analyze the stack trace and provide a detailed explanation along with potential solutions.

### Example in Google Colab

1. Install and set up the package:

   ```python
   !pip install llm-exceptions
   import os
   os.environ['HF_TOKEN'] = 'your_hugging_face_token'
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

### Example in Jupyter Notebook/Lab

1.  Load the extension in your notebook:

    ```python
    %load_ext llm_exceptions
    ```

2.  Run some code that produces an error:

    ```python
    def divide(a, b):
        return a / b

    divide(5, 0)
    ```

3.  When the error occurs, **LLM Exceptions** will provide an explanation:

    ```
    ZeroDivisionError: division by zero
    ```

    > **LLM Explanation**: The error `ZeroDivisionError` occurs because you are attempting to divide a number by zero, which is mathematically undefined. To fix this error, ensure that the divisor `b` is not zero before performing the division.

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
