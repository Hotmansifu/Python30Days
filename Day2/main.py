import requests
import time
from win10toast import ToastNotifier

# URL of the website to monitor
url = "https://programs.cu.edu.ge/students/gpa.php"

# URL of the page to redirect to after logging in
redirect_url = "https://programs.cu.edu.ge/students/gpa.php"

# File to store previous HTML content
previous_file = "previous.html"

# Authentication information
username = "l_andghuladze3"
password = "OzUCiTy321@%"

# Initialize the ToastNotifier object
toaster = ToastNotifier()

# Create a session object to persist the authentication information
session = requests.Session()

# Log in to the website and redirect to the target page
login_url = "https://programs.cu.edu.ge/cu/loginStud"
login_data = {"username": username, "password": password}
session.post(login_url, data=login_data)
session.get(redirect_url)

while True:
    # Retrieve current HTML content
    response = session.get(url)
    current_content = response.content

    # Check if previous HTML content exists
    try:
        with open(previous_file, "rb") as f:
            previous_content = f.read()
    except FileNotFoundError:
        previous_content = None

    # Compare current and previous HTML content
    if current_content != previous_content:
        print("Website content has changed!")
        toaster.show_toast("Website content has changed!", "The content of the website has been updated.", duration=10)

    # Save current HTML content as previous HTML content
    with open(previous_file, "wb") as f:
        f.write(current_content)

    # Wait for 5 minutes before the next check
    time.sleep(5 * 60)
