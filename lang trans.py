from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.config(bg='darkmagenta')
root.title("Language Translator")

Label(root, text="Language Translator", font="papyrus 20 bold", bg='darkmagenta').pack()
Label(root, text="Translate anything to your language", font='papyrus 15 bold', bg='darkmagenta', width='30').pack(side='bottom')
Label(root, text="Enter Text", font='papyrus 13 bold', bg='darkmagenta').place(x=200, y=60)

Input_text = Text(root, font='papyrus 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=20, y=100)

Label(root, text="Output", font='papyrus 13 bold', bg='darkmagenta').place(x=780, y=60)

Output_text = Text(root, font='papyrus 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, font="papyrus 13 bold",values=language, width=25)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, font="papyrus 13 bold",values=language, width=25)
dest_lang.place(x=730, y=60)
dest_lang.set('choose output language')

OutputVar = StringVar()

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())
    Output_text.delete('1.0', END)
    OutputVar.set(translated.text)

trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='Silver', activebackground='sky blue')
trans_btn.place(x=490, y=180)

Output_label = Label(root, textvariable=OutputVar, font='papyrus 10 bold', bg='white', relief='solid', wraplength=400)
Output_label.place(x=600, y=100)

root.mainloop()
