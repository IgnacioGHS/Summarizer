import tkinter as tk
from tkinter import filedialog
from goose3 import Goose
from bardapi import Bard
import PyPDF2
import os 


class InterfaceSwitcher:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title('Summarizer')

        self.key_frame = tk.Frame(self.root) 
        self.menu_frame = tk.Frame(self.root)
        self.article_frame = tk.Frame(self.root)
        self.pdf_frame = tk.Frame(self.root)

        self.create_key_frame()
        self.create_menu_frame()
        self.create_article_frame()
        self.create_pdf_frame()

        self.current_frame = None
        self.show_frame(self.key_frame)

    def create_key_frame(self):
        def get_key():
            api_key = keytext.get('1.0', 'end').strip()
            os.environ["_Bard_API_KEY"] = api_key

        def key_to_menu():
            get_key()
            self.show_menu_frame()
        keylabel = tk.Label(self.key_frame, text='Insert API key:')
        keylabel.pack()

        keytext = tk.Text(self.key_frame, height=1, width=140)
        keytext.pack()

        keybtn = tk.Button(self.key_frame, text='Insert', command=key_to_menu)
        keybtn.pack()

    def create_menu_frame(self):
        menubtn1 = tk.Button(self.menu_frame, text='Article', command=self.show_article_frame)
        menubtn1.pack()

        menubtn2 = tk.Button (self.menu_frame, text='PDF', command=self.show_pdf_frame)
        menubtn2.pack()

    def create_article_frame(self):
        def summarize():
            url = utext.get('1.0', 'end').strip()

            # Init and process Goose
            g = Goose()
            article = g.extract(url)
            text = article._cleaned_text

            # Create prompt
            prompt = f"Summarize the following news article:\n{text}"

            # Use Bard
            generated_summary = Bard().get_answer(prompt)['content']


            # Tk Inter config
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
            summary.insert('1.0', generated_summary)  

            title.config(state='disabled')
            author.config(state='disabled')
            publishing.config(state='disabled')
            summary.config(state='disabled')

        
        # Article title:
        tlabel = tk.Label(self.article_frame, text='Title')
        tlabel.pack()

        title = tk.Text(self.article_frame, height=1, width=140)
        title.config(state='disabled', bg='#dddddd')
        title.pack()


        # Article author:
        alabel = tk.Label(self.article_frame, text='Author')
        alabel.pack()

        author = tk.Text(self.article_frame, height=1, width=140)
        author.config(state='disabled', bg='#dddddd')
        author.pack()


        # Article publishing date:
        plabel = tk.Label(self.article_frame, text='Publishing Date')
        plabel.pack()

        publishing = tk.Text(self.article_frame, height=1, width=140)
        publishing.config(state='disabled', bg='#dddddd')
        publishing.pack()


        # Article summary:
        slabel = tk.Label(self.article_frame, text='Summary')
        slabel.pack()

        summary = tk.Text(self.article_frame, height=20, width=140)
        summary.config(state='disabled', bg='#dddddd')
        summary.pack()


        # Article URL:
        ulabel = tk.Label(self.article_frame, text='URL')
        ulabel.pack()

        utext = tk.Text(self.article_frame, height=1, width=140)
        utext.pack()


        # Button:
        btn = tk.Button(self.article_frame, text='Summarize', command=summarize)
        btn.pack()

        button2 = tk.Button(self.article_frame, text="Go back", command=self.show_menu_frame)
        button2.pack()

    def create_pdf_frame(self):
        def read_pdf(file_path):
            with open(file_path, 'rb') as file:
                # Create a PDF reader object using PdfReader
                pdf_reader = PyPDF2.PdfReader(file)

                # Get the number of pages in the PDF
                num_pages = len(pdf_reader.pages)   

                # Iterate through all pages and extract text
                text = ""
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
            return text

        def pdf_summarize():
            file_path = filedialog.askopenfilename(title="Select a File")
            
            if file_path:   
                text = read_pdf(file_path)

                # Create prompt
                prompt = f"Summarize the following file:\n{text}"

                # Use Bard
                generated_summary = Bard().get_answer(prompt)['content']


                # Tk Inter config
                summary.config(state='normal')
                selectedtext.config(state='normal')

                summary.delete('1.0', 'end')
                summary.insert('1.0', generated_summary) 

                selectedtext.delete('1.0', 'end')
                selectedtext.insert('1.0', file_path) 

                summary.config(state='disabled')
                selectedtext.config(state='disabled')

            
        # Article title:
        summary = tk.Text(self.pdf_frame, height=29, width=140)
        summary.config(state='disabled', bg='#dddddd')
        summary.pack()


        # Article URL:
        selected = tk.Label(self.pdf_frame, text='Selected file')
        selected.pack()

        selectedtext = tk.Text(self.pdf_frame, height=1, width=140)
        selectedtext.pack()


        # Button:
        btn = tk.Button(self.pdf_frame, text='Select file', command=pdf_summarize)
        btn.pack()

        button2 = tk.Button(self.pdf_frame, text="Go back", command=self.show_menu_frame)
        button2.pack()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame
        self.current_frame.pack()

    def show_key_frame(self):
        self.show_frame(self.key_frame)

    def show_menu_frame(self):
        self.root.geometry("300x200")
        self.show_frame(self.menu_frame)
    
    def show_article_frame(self):
        self.root.geometry("1200x575")
        self.show_frame(self.article_frame)

    def show_pdf_frame(self):
        self.root.geometry("1200x575")
        self.show_frame(self.pdf_frame)


if __name__ == "__main__":
    root = tk.Tk() # Object
    app = InterfaceSwitcher(root)
    root.geometry("300x200")
    root.mainloop()
