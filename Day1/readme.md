# Typing Test

This is a simple typing test program written in Python that generates random text and tests the user's typing speed and accuracy.

## Requirements

- Python 3.x
- NLTK (Natural Language Toolkit) library

## Usage

To use the program, follow these steps:

1. Install NLTK library by running the following command in your terminal:

    ```
    pip install nltk
    ```

2. Import the necessary libraries by adding the following code at the beginning of your Python script:

    ```
    import random
    import time
    import nltk
    ```

3. Define the `generate_text` function that generates random text based on a chosen category from the Brown corpus in NLTK.

4. Define the `typing_test` function that prompts the user to type the generated text and calculates the typing speed, accuracy, and prompts the user to play again.

5. Call the `typing_test` function with the number of sentences as an argument.

6. Run the script in your terminal by navigating to the script directory and typing the following command:

    ```
    python typing_test.py
    ```

