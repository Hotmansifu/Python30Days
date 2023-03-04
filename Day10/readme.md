# Analyzing Amazon Order History

This Python script analyzes your Amazon order history CSV file to provide insights about your shopping habits on Amazon. The script calculates the total amount spent on Amazon, the most frequently used card, the highest spending month, the most frequent ordering customer email, and the most frequent category.

## Usage

1. Export your Amazon order history as a CSV file by following these [instructions](https://www.amazon.com/gp/help/customer/display.html?nodeId=GNHQ4WJSRW33MWAH).

2. Save the CSV file as `order_history.csv` in the same directory as this script.

3. Run the script by typing `python analyze_amazon.py` in your terminal.

4. The script will output the following information:

- Total amount spent on Amazon
- Most frequently used card
- Highest spending month
- Most frequent ordering customer email
- Most frequent category

## Requirements

This script requires Python 3 and the following packages:

- pandas

You can install the required packages using the following command:

```pip install pandas```

## License

This project is licensed under the [MIT License](LICENSE).
