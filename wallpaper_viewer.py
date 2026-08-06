from tkinter import *
from PIL import ImageTk, Image
import os


def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter+=1

counter = 1

root = Tk()
root.title("Wallpaper Viewer")
root.iconbitmap('favicon.ico')

root.geometry('250x400') # For fix size
root.configure(background='black')

files = os.listdir('wallpapers')

img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers', file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))


img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root, text="Next", fg='black', bg='white', width=25, height=2, command=rotate_image)
next_btn.pack(pady=(10,20))
next_btn.config(font=('verdana', 10))





root.mainloop()