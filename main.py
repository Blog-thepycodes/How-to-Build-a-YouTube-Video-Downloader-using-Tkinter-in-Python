from tkinter import *
from tkinter import filedialog
from pytube import YouTube
 
 
# Create main window
root = Tk()
root.title("Youtube Downloader - The Pycodes")
root.geometry("400x200")
root.resizable(False, False)
 
 
# Download Function
def download_video():
   url = entry_url.get()
   save_path = entry_path.get()
   print(f"URL: {url}")
   print(f"Save Path: {save_path}")
 
 
   try:
       yt = YouTube(url)
       stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
       stream.download(save_path)
       status_label.config(text="Download complete")
   except Exception as e:
       status_label.config(text=f"Error: {str(e)}")
 
 
# Browse Function
def browse_path():
   directory = filedialog.askdirectory()
   entry_path.delete(0, END)
   entry_path.insert(0, directory)
 
 
# URL Entry
label_url = Label(root, text="Enter YouTube URL:")
label_url.pack()
entry_url = Entry(root, width=40)
entry_url.pack()
 
 
# Path Entry
label_path = Label(root, text="Select save path:")
label_path.pack()
entry_path = Entry(root, width=40)
entry_path.pack()
button_browse = Button(root, text="Browse", command=browse_path)
button_browse.pack()
 
 
# Download Button
button_download = Button(root, text="Download", command=download_video)
button_download.pack()
 
 
# Status Label
status_label = Label(root, text="Status: Ready")
status_label.pack()
 
 
root.mainloop()
