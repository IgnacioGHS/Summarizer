import tkinter as tk
from goose3 import Goose
from bardapi import Bard
import os 


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


api_key = input('Please enter yor Google Bard API Key: ')
os.environ["_Bard_API_KEY"] = api_key

##### Tk GUI Setup #####

# Basic setup:
root = tk.Tk() # Object
root.title('Summarizer') # Window title
root.geometry('1200x550') # Window size


# Article title:
tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()


# Article author:
alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()


# Article publishing date:
plabel = tk.Label(root, text='Publishing Date')
plabel.pack()

publishing = tk.Text(root, height=1, width=140)
publishing.config(state='disabled', bg='#dddddd')
publishing.pack()


# Article summary:
slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()


# Article URL:
ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()


# Button:
btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()


# Mainloop:
root.mainloop()