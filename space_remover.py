#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog


# In[2]:


def remove_spaces(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove spaces between lines
            cleaned_line = line.strip()
            if cleaned_line:
                outfile.write(cleaned_line + '\n')


# In[3]:


def process_large_data():
    input_path = filedialog.askopenfilename(title="Select input file", filetypes=[("Text files", "*.txt")])

    if not input_path:
        return  # User canceled file selection

    output_path = filedialog.asksaveasfilename(title="Save output as", filetypes=[("Text files", "*.txt")])

    if not output_path:
        return  # User canceled save as

    remove_spaces(input_path, output_path)
    result_label.config(text="Spaces removed and saved successfully!")


# In[4]:


# Create GUI
app = tk.Tk()
app.title("Remove Spaces from Lines")


# In[5]:


# Add a button to trigger the process
process_button = tk.Button(app, text="Process Large Data", command=process_large_data)
process_button.pack(pady=10)


# In[6]:


# Display label for result message
result_label = tk.Label(app, text="")
result_label.pack(pady=5)


# In[ ]:


# Start the GUI event loop
app.mainloop()


# In[ ]:




