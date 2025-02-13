from tkinter import *
import qrcode
from PIL import Image, ImageTk
import os

app = Tk()
app.title('Gerador de QRCode')
app.geometry('350x470')
app.config(bg='#262626')
app.resizable(False, False)

def generate():
    global qr_image
    name = title.get()
    text = entry.get()

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    qr = qrcode.make(text)
    qr.save(os.path.join(diretorio_atual, '../Gen-QRCode/QRCode/', f'{name}.png'))

    qr_image = Image.open(os.path.join(diretorio_atual, '../Gen-QRCode/QRCode/', f'{name}.png'))
    qr_image = qr_image.resize((int(app.winfo_width() * 0.7), int(app.winfo_height() * 0.4)), Image.LANCZOS)
    qr_image = ImageTk.PhotoImage(qr_image)
    
    Image_view.config(image=qr_image)

Image_view = Label(app, bg='#262626')
Image_view.pack(padx=50, pady=30)

Label(app, text='Titulo do QRCode:', fg='white', bg='#262626', font=15).place(x=110, y=260)
title = Entry(app, width=28, font='Arial 15')
title.place(x=20, y=290)

Label(app, text='Link do site: ', fg='white', bg='#262626', font=15).place(x=130, y=325)
entry = Entry(app, width=28, font='Arial 15')
entry.place(x=20, y=355)

Button(app, text='Gerar', width=20, height=2, bg='#0574ab', fg='Black', command=generate).place(x=100, y=400)

app.mainloop()
