import os
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
from itertools import cycle
import time

# List of directories to exclude
EXCLUDE_DIRS = ["node_modules", ".git", "__pycache__", "site-packages"]

def generate_structure(directory):
    structure = [f"Selected Directory: {directory}\n"]  # Include the selected directory at the top

    def write_structure(dir_path, prefix=""):
        entries = sorted(os.listdir(dir_path))
        entry_count = len(entries)

        for index, entry in enumerate(entries):
            full_path = os.path.join(dir_path, entry)
            is_last = (index == entry_count - 1)

            # Create appropriate branch symbol
            branch = "└── " if is_last else "├── "
            structure.append(f"{prefix}{branch}{entry}")

            # Skip excluded directories
            if os.path.isdir(full_path) and entry in EXCLUDE_DIRS:
                continue

            # Extend prefix for children
            if os.path.isdir(full_path):
                new_prefix = f"{prefix}    " if is_last else f"{prefix}│   "
                write_structure(full_path, new_prefix)

    write_structure(directory)
    return "\n".join(structure)

def select_directory():
    # Let the user select a directory
    directory = filedialog.askdirectory()
    if directory:
        # Start the loading animation and directory generation in separate threads
        Thread(target=show_loading).start()
        Thread(target=process_directory, args=(directory,)).start()
    else:
        messagebox.showwarning("No Selection", "Please select a directory.")

def process_directory(directory):
    global loading
    try:
        structure = generate_structure(directory)
        global current_structure
        current_structure = structure

        # Display the structure in the GUI
        text_widget.delete("1.0", tk.END)  # Clear previous text
        text_widget.insert(tk.END, structure)

        # Enable the save and copy buttons
        button_save.pack(pady=5, side=tk.LEFT, padx=10)
        button_copy.pack(pady=5, side=tk.LEFT, padx=10)

    finally:
        loading = False  # Stop loading animation

def show_loading():
    spinner = cycle(["|", "/", "-", "\\"])  # Loading animation characters
    global loading
    loading = True
    while loading:
        for frame in spinner:
            loading_label.config(text=f"Loading... {frame}")
            time.sleep(0.1)
            if not loading:  # Exit loop if loading is False
                break
    loading_label.config(text="")  # Clear loading text after completion

def save_structure():
    if not current_structure:
        messagebox.showwarning("No Content", "No structure to save. Generate it first!")
        return

    # Let the user select a location to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                                             title="Save File")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(current_structure)
        messagebox.showinfo("Success", f"File saved successfully at {file_path}")

def copy_to_clipboard():
    if not current_structure:
        messagebox.showwarning("No Content", "No structure to copy. Generate it first!")
        return

    root.clipboard_clear()
    root.clipboard_append(current_structure)
    root.update()  # Update clipboard contents
    messagebox.showinfo("Success", "Directory structure copied to clipboard!")

# Create GUI
root = tk.Tk()
root.title("Directory Structure Generator")
root.geometry("700x550")
root.configure(bg="#1e1e1e")  # Set dark background for the main window

current_structure = ""  # Store the generated directory structure
loading = False  # To control the loading animation

# Style configurations for dark theme
widget_fg_color = "#ffffff"
button_bg_color = "#3c6e71"
button_fg_color = "#ffffff"
text_widget_bg_color = "#1e1e1e"
text_widget_fg_color = "#ffffff"

# Add a label
label = tk.Label(root, text="Generate a directory structure and save or copy it", font=("Arial", 12), bg="#1e1e1e", fg=widget_fg_color)
label.pack(pady=10)

# Add buttons for actions
button_select = tk.Button(root, text="Select Directory", command=select_directory, font=("Arial", 12), bg=button_bg_color, fg=button_fg_color)
button_select.pack(pady=5)

# Loading label for animation
loading_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e", fg="#ffa500")
loading_label.pack()

# Add a text widget to display the generated structure
text_widget = tk.Text(root, wrap="none", font=("Courier", 10), height=20, width=80, bg=text_widget_bg_color, fg=text_widget_fg_color, insertbackground=text_widget_fg_color)
text_widget.pack(pady=10, padx=10)

# Add the save and copy buttons but hide them initially
button_frame = tk.Frame(root, bg="#1e1e1e")  # Create a frame for Save and Copy buttons
button_frame.pack()

button_save = tk.Button(button_frame, text="Save File", command=save_structure, font=("Arial", 12), bg="#008080", fg=button_fg_color)
button_copy = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#ffa500", fg=button_fg_color)

# Run the GUI application
root.mainloop()
