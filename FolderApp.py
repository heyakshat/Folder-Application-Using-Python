#A Simple GUI Folder Creation Application Using Python 

import os
import tkinter as tk
from tkinter import messagebox

def create_folder():
    folder_name = folder_entry.get()
    if not folder_name:
        messagebox.showerror("Error", "Please enter a folder name.")
        return

    try:
        os.mkdir(folder_name)
        messagebox.showinfo("Success", f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        messagebox.showerror("Error", f"Folder '{folder_name}' already exists.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_subfolder():
    folder_name = folder_entry.get()
    subfolder_name = subfolder_entry.get()

    if not folder_name or not subfolder_name:
        messagebox.showerror("Error", "Please enter folder and subfolder names.")
        return

    try:
        os.makedirs(os.path.join(folder_name, subfolder_name))
        messagebox.showinfo("Success", f"Subfolder '{subfolder_name}' created successfully.")
    except FileExistsError:
        messagebox.showerror("Error", f"Subfolder '{subfolder_name}' already exists.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Folder Application")
root.geometry("300x200")

# Create labels and entry widgets
folder_label = tk.Label(root, text="Enter Folder Name:")
folder_label.pack(pady=5)

folder_entry = tk.Entry(root)
folder_entry.pack(pady=5)

create_folder_button = tk.Button(root, text="Create Folder", command=create_folder)
create_folder_button.pack(pady=10)

# Create labels and entry widgets for subfolder
subfolder_label = tk.Label(root, text="Enter Subfolder Name:")
subfolder_label.pack(pady=5)

subfolder_entry = tk.Entry(root)
subfolder_entry.pack(pady=5)

create_subfolder_button = tk.Button(root, text="Create Subfolder", command=create_subfolder)
create_subfolder_button.pack(pady=10)

# Run the main event loop
root.mainloop()
