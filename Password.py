# Python program to generate random 
# password using Tkinter module 
import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *
import setuptools

#Generate Password Code

def NewPassword():
        entry.delete(0, END)
        length = 10
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%&*"


        all = lower + upper + numbers + symbols
        password = "".join (random.sample(all, length))
        return password

# Function for generation of password 
def generate(): 
                 
	password1 = NewPassword()
	entry.insert(10, password1)
	

# Function for copying password to clipboard 
def copy1(): 
	random_password = entry.get() 
	pyperclip.copy(random_password)

# Main Function 
# create GUI window 
root = Tk() 

# Title of your GUI window 
root.title("Random Password Generator") 

# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 

# create Buttons Copy which will copy 
# password to clipboard and Generate 
# which will generate the password 
copy_button = Button(root, text="Copy", command=copy1) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=3)

# start the GUI 
root.mainloop() 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Nitin Hans", # Replace with your own username
    version="0.0.1",
    author="Nitin Hans",
    description="Password Generator Tool",
)
