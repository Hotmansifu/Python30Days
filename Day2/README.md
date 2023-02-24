# Website Monitor

This Python script monitors a website for changes and displays a notification if the website's content has been updated. The script uses the `requests` library to retrieve the website's content and the `win10toast` library to display a Windows toast notification.

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt` in your terminal or command prompt.
3. Open `monitor.py` in your code editor.
4. Update the `url`, `previous_file`, `username`, and `password` variables with the URL of the website to monitor, the file name to store the previous HTML content, and your authentication information, respectively.
5. Save and run the `main.py` file in your terminal or command prompt using `python monitor.py`.
6. The script will continuously monitor the website for changes every 5 minutes and display a notification if the content has been updated.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
