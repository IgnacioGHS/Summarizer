import tkinter as tk
from tkinter import filedialog
import os

def select_file_and_get_directory():
    file_path = filedialog.askopenfilename(title="Select a File")
    
    if file_path:
        directory = os.path.dirname(file_path)
        print(f"Selected file: {file_path}")
        print(f"Directory: {directory}")
        # Do something with the file path and directory

root = tk.Tk()
root.title("File Selection Example")

button = tk.Button(root, text="Select File and Get Directory", command=select_file_and_get_directory)
button.pack(pady=20)

root.mainloop()
