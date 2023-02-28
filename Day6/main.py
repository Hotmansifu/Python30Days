import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(url, quality):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    stream = streams[quality-1]
    stream.download()

def start_download():
    url = entry.get()
    try:
        quality = int(quality_var.get())
        if quality < 1 or quality > len(streams):
            raise ValueError("Invalid option.")
        download_video(url, quality)
        messagebox.showinfo("Info", "Download complete.")
    except ValueError:
        messagebox.showerror("Error", "Invalid option.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.geometry("400x400")
    root.configure(background='#7FFFD4')

    label = tk.Label(root, text="Enter the YouTube video link:", background='#7FFFD4')
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Show available qualities", command=lambda: show_qualities(entry.get()))
    button.pack()

    label = tk.Label(root, text="Select the desired video quality:", background='#7FFFD4')
    label.pack()

    quality_var = tk.IntVar()
    streams = []

    def show_qualities(url):
        yt = YouTube(url)
        print("Available video qualities:")
        global streams
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        for i, stream in enumerate(streams):
            tk.Radiobutton(root, text=f"{stream.resolution}", variable=quality_var, value=i+1).pack()

    download_button = tk.Button(root, text="Download", command=start_download)
    download_button.pack()

    root.mainloop()
