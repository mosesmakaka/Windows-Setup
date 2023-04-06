import tkinter as tk
import os

# Create the main window
window = tk.Tk()
window.title("Windows 11 Hidden Features")

# Create a label
label = tk.Label(window, text="Click enable to install hidden features")
label.pack()

# Create an entry box
entry = tk.Entry(window)
#entry.pack()

# Function to run the batch file
def run_batch_file():
    filename = entry.get() + ".bat"
    os.system("hf" + filename)

# Create a button to run the batch file
button = tk.Button(window, text="Enable", command=run_batch_file)
button.pack()

# Run the main event loop
window.mainloop()
