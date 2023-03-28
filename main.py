import tkinter as tk
import os

# Create the main window
window = tk.Tk()
window.title("Batch File UI")

# Create a label
label = tk.Label(window, text="Enter the name of the file you want to create:")
label.pack()

# Create an entry box
entry = tk.Entry(window)
entry.pack()

# Function to run the batch file
def run_batch_file():
    filename = entry.get() + ".txt"
    os.system("Windows 11 Hidden Features.bat " + filename)

# Create a button to run the batch file
button = tk.Button(window, text="Create File", command=run_batch_file)
button.pack()

# Run the main event loop
window.mainloop()
