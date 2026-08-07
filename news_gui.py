import requests
from tkinter import *
from PIL import ImageTk, Image
import io
import webbrowser


class NewsApp:

    def __init__(self):

        self.data = requests.get(
            "https://newsapi.org/v2/top-headlines?country=us&apiKey=dd29e841ab424c9a8353053a35d33774"
        ).json()

        self.current_index = 0

        self.load_gui()
        self.load_news_item(self.current_index)

        self.root.mainloop()

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.title("News App")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_link(self, url):
        webbrowser.open(url)

    def load_news_item(self, index):

        self.clear()

        article = self.data["articles"][index]
        img_url = article["urlToImage"]

        if img_url:
            try:
                response = requests.get(img_url, timeout=10)
                image = Image.open(io.BytesIO(response.content))
                image = image.resize((350, 250))

                photo = ImageTk.PhotoImage(image)

                img_label = Label(self.root, image=photo)
                img_label.image = photo
                img_label.pack()

            except Exception:

                Label(
                    self.root,
                    text="No Image Available",
                    bg="black",
                    fg="white",
                    font=("Verdana", 18)
                ).pack(pady=40)

        else:

            Label(
                self.root,
                text="No Image Available",
                bg="black",
                fg="white",
                font=("Verdana", 18)
            ).pack(pady=40)


        heading = Label(
            self.root,
            text=article["title"],
            bg="black",
            fg="white",
            wraplength=340,
            justify="center",
            font=("Verdana", 15, "bold")
        )

        heading.pack(pady=(10, 15))


        description = article["description"]

        if description is None:
            description = "No Description Available."

        details = Label(
            self.root,
            text=description,
            bg="black",
            fg="white",
            wraplength=340,
            justify="center",
            font=("Verdana", 11)
        )

        details.pack(pady=(0, 20))


        frame = Frame(self.root, bg="black")
        frame.pack(side=BOTTOM, pady=15)

        # Previous Button
        prev_btn = Button(
            frame,
            text="Prev",
            width=10,
            height=2,
            command=self.prev_news
        )

        prev_btn.grid(row=0, column=0, padx=5)

        # Read More Button
        read_btn = Button(
            frame,
            text="Read More",
            width=10,
            height=2,
            command=lambda: self.open_link(article["url"])
        )

        read_btn.grid(row=0, column=1, padx=5)

        # Next Button
        next_btn = Button(
            frame,
            text="Next",
            width=10,
            height=2,
            command=self.next_news
        )

        next_btn.grid(row=0, column=2, padx=5)


        if index == 0:
            prev_btn.config(state=DISABLED)

        if index == len(self.data["articles"]) - 1:
            next_btn.config(state=DISABLED)

    def next_news(self):

        if self.current_index < len(self.data["articles"]) - 1:
            self.current_index += 1
            self.load_news_item(self.current_index)

    def prev_news(self):

        if self.current_index > 0:
            self.current_index -= 1
            self.load_news_item(self.current_index)


obj = NewsApp()