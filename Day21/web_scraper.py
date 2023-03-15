import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the webpage to scrape
url = "https://www.example.com"

# Send a request to the webpage and get the HTML response
response = requests.get(url)
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the relevant information on the webpage
title = soup.find("title").text
paragraphs = [p.text for p in soup.find_all("p")]

# Save the information to a CSV file
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Paragraphs"])
    writer.writerow([title, "\n".join(paragraphs)])
