#Practicing coding in Python, using a PythonGeeks Password Generator.  3/6/25.
#As reference, as of now (3/8), the code works after learning I was mixing up random.sample vs random.choices, as well as not using string variables correctly.

import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except ValueError: # Corrected exception type
        messagebox.showerror(message="Please key in the required inputs.")
        return

    character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'*+,-./:;<=>?@[]^_`{|}~"

    if repeat == 1:  # 1 means No Repetition
        try: # Added a try block to catch an error when the length is longer than the character_string
            password_list = random.sample(character_string, length)
        except ValueError:
            messagebox.showerror(message="Password length is longer than available characters without repetition.")
            return
    else:  # Any other value means Repetition allowed
        password_list = random.choices(character_string, k=length)

    password = ''.join(password_list)
    password_v = StringVar()
    password_v.set("Created password: " + password)

    password_label = Entry(password_gen, bd=1, bg="gray85", textvariable=password_v, state="readonly")
    password_label.place(x=10, y=140, height=50, width=320)

  



#And now, the user interface.  Would be kind of stupid to create a generator that people couldn't use.
password_gen = Tk()
password_gen.geometry("350x200")
password_gen.title("Brad's Password Generator, learned from PythonGeeks")

#Mention the title of the app
title_label = Label(password_gen, text="Brad's Password Generator, learned from PythonGeeks", font=('Ubuntu Mono',10))
title_label.pack()
#Read length
length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20,y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190,y=30)
#Read repetition
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=20,y=60)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300,y=60)
#A Button to generate a password
password_button = Button(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=100,y=100)

#And now, Exit and close the app
password_gen.mainloop()




