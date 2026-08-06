from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = pass_input.get()
    if email == 'ali@gmail.com' and password == '1234':
        messagebox.showinfo("Yayy", 'Login Successful')
    else:
        messagebox.showerror("Error", "Login Failed")


root = Tk()

root.title("Login Form")
root.iconbitmap("favicon.ico")

root.minsize(300,300)
root.geometry('350x500') # For fix size

root.configure(background='#0096DC')
img = Image.open('logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10,10))

text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 20))

email_label = Label(root, text="Enter Email", fg='white', bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=40)
email_input.pack(ipady=6, pady=(1,15))

pass_label = Label(root, text="Enter Password", fg='white', bg='#0096DC')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana', 12))

pass_input = Entry(root, width=40)
pass_input.pack(ipady=6, pady=(1,15))

login_btn = Button(root, text="Login Here", fg='black', bg='white', width=20, height=2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana', 10))

root.mainloop()