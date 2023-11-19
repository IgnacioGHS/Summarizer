import tkinter as tk
from goose3 import Goose
from bardapi import Bard
import os 

class InterfaceSwitcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Summarizer')

        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)

        self.create_frame1()
        self.create_frame2()

        self.current_frame = None  # To track the current visible frame
        self.show_frame(self.frame1)

    def create_frame1(self):
        label1 = tk.Label(self.frame1, text="Menu")
        label1.pack(pady=10)

        articlelabel = tk.Label(self.frame2, text='')
        articlelabel.pack()

        utext = tk.Text(self.frame2, height=1, width=140)
        utext.pack()

        button1 = tk.Button(self.frame1, text="Summarize article", command=self.show_frame2)
        button1.pack()

    def create_frame2(self):
        def get_text(url):
            g = Goose()
            article = g.extract(url)
            return article.cleaned_text, article

        def summarize():
            url = utext.get('1.0', 'end').strip()

            text, article = get_text(url)

            prompt = f"Summarize the following news article:\n{text}"

            generated_summary = Bard().get_answer(prompt)['content']

            title.config(state='normal')
            author.config(state='normal')
            publishing.config(state='normal')
            summary.config(state='normal')

            title.delete('1.0', 'end')
            title.insert('1.0', article._title)

            author.delete('1.0', 'end')
            author.insert('1.0', article._authors)

            publishing.delete('1.0', 'end')
            publishing.insert('1.0', article._publish_date)

            summary.delete('1.0', 'end')
            summary.insert('1.0', generated_summary)  # Use a different variable here

            title.config(state='disabled')
            author.config(state='disabled')
            publishing.config(state='disabled')
            summary.config(state='disabled')

        
        # Article title:
        tlabel = tk.Label(self.frame2, text='Title')
        tlabel.pack()

        title = tk.Text(self.frame2, height=1, width=140)
        title.config(state='disabled', bg='#dddddd')
        title.pack()


        # Article author:
        alabel = tk.Label(self.frame2, text='Author')
        alabel.pack()

        author = tk.Text(self.frame2, height=1, width=140)
        author.config(state='disabled', bg='#dddddd')
        author.pack()


        # Article publishing date:
        plabel = tk.Label(self.frame2, text='Publishing Date')
        plabel.pack()

        publishing = tk.Text(self.frame2, height=1, width=140)
        publishing.config(state='disabled', bg='#dddddd')
        publishing.pack()


        # Article summary:
        slabel = tk.Label(self.frame2, text='Summary')
        slabel.pack()

        summary = tk.Text(self.frame2, height=20, width=140)
        summary.config(state='disabled', bg='#dddddd')
        summary.pack()


        # Article URL:
        ulabel = tk.Label(self.frame2, text='URL')
        ulabel.pack()

        utext = tk.Text(self.frame2, height=1, width=140)
        utext.pack()


        # Button:
        btn = tk.Button(self.frame2, text='Summarize', command=summarize)
        btn.pack()

        button2 = tk.Button(self.frame2, text="Go back", command=self.show_frame1)
        button2.pack()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame
        self.current_frame.pack()

    def show_frame1(self):
        self.show_frame(self.frame1)

    def show_frame2(self):
        self.root.geometry("1200x575")
        self.show_frame(self.frame2)

if __name__ == "__main__":
    root = tk.Tk() # Object
    app = InterfaceSwitcherApp(root)
    root.geometry("300x200")
    root.mainloop()
