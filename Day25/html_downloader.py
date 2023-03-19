import tkinter as tk
import requests

class HTMLDownloader:
    def __init__(self, master):
        self.master = master
        master.title("HTML Downloader")

        # Create a label and entry field for the URL
        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        # Create a button to download the HTML content
        self.download_button = tk.Button(master, text="Download", command=self.download)
        self.download_button.pack()

    def download(self):
        # Get the URL from the entry field
        url = self.url_entry.get()

        # Make a GET request to the URL and get the HTML content
        response = requests.get(url)
        html = response.content.decode()

        # Save the HTML content to a file
        with open('page.html', 'w') as f:
            f.write(html)

        # Display a message box to confirm the download
        tk.messagebox.showinfo('Download Complete', 'HTML content saved to page.html')

# Create the main window and start the application
root = tk.Tk()
app = HTMLDownloader(root)
root.mainloop()
