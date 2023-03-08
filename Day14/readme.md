# Temperature converter

This is a Python program that converts temperatures between Fahrenheit and Celsius. The user is prompted to choose which conversion they want to make, and then input the temperature they want to convert.

The program contains two functions: `fahrenheit_to_celsius()` and `celsius_to_fahrenheit()`. These functions perform the actual temperature conversion calculations, which are based on the formulas:

* Celsius to Fahrenheit: F = (C x 9/5) + 32

* Fahrenheit to Celsius: C = (F - 32) x 5/9

The program then calls the appropriate function based on the user's choice and displays the converted temperature to the console with two decimal places using the format() method.


## Usage

To run the program, navigate to the directory where the temperature_converter.py file is located and run the following command in the terminal:

```python temperature_converter.py```
The program will then prompt the user to enter the temperature they want to convert and which conversion they want to make. The input temperature should be entered as an integer, followed by either "F" for Fahrenheit or "C" for Celsius. For example, to convert 32 degrees Fahrenheit to Celsius, the user should enter:
`32f `
The program will then display the converted temperature to the console.


## Contributing
Contributions to this program are welcome. If you find any bugs or have any suggestions for improvement, please create a GitHub issue or submit a pull request.
## License

This project is licensed under the [MIT License](LICENSE).
