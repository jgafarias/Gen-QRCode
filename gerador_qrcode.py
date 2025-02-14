from tkinter import *
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkbootstrap
import io
import os

def generate():
    # Obtém o texto da entrada (URL) fornecida pelo usuário
    text = entry.get()

    # Verifica se o texto começa com "https://", caso contrário, exibe um aviso
    if not text.startswith('https://'):
        messagebox.showwarning('ERRO', 'O link deve começar com "https://".')
        return
        
    # Cria o QRCode com base no texto fornecido
    qr_image = create_qrcode(text)
    # Exibe o QRCode na interface gráfica
    display_qrcode(qr_image)

def create_qrcode(text):
    # Configura o QRCode com as opções desejadas
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Adiciona o texto (URL) ao QRCode
    qr.add_data(text)
    qr.make(fit=True)

    # Cria a imagem do QRCode
    img = qr.make_image(fill='black', back_color='white')
    return img

def display_qrcode(img):
    # Converte a imagem do QRCode para um formato que pode ser exibido na interface gráfica
    with io.BytesIO() as buffer:
        img.save(buffer, format="PNG")
        qr_image = Image.open(buffer)
        # Redimensiona a imagem do QRCode
        qr_image = qr_image.resize((int(app.winfo_width() * 0.75), int(app.winfo_height() * 0.5)), Image.LANCZOS)
        qr_image = ImageTk.PhotoImage(qr_image)
    
    # Configura o widget Label para exibir a imagem do QRCode
    Image_view.config(image=qr_image)
    # Mantém uma referência à imagem para evitar a coleta de lixo (garbage collection)
    Image_view.image = qr_image

def save_qrcode_as():
    # Obtém o texto da entrada (URL) fornecida pelo usuário
    text = entry.get()

    # Verifica se o texto começa com "https://", caso contrário, exibe um aviso
    if not text.startswith('https://'):
        messagebox.showwarning('ERRO', 'O link deve começar com "https://".')
        return

    # Cria o QRCode com base no texto fornecido
    qr_image = create_qrcode(text)
    # Abre um diálogo para o usuário escolher o local e o nome do arquivo para salvar o QRCode
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')], title="Salvar QRCode como")
    if file_path:
        # Salva a imagem do QRCode no local escolhido
        qr_image.save(file_path)
        # Exibe uma mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O QRCode foi salvo em {file_path}')

# Configura a janela principal da aplicação usando ttkbootstrap para um estilo moderno
app = ttkbootstrap.Window(themename='superhero')
app.title('Gerador de QRCode')
app.geometry('350x470')
app.resizable(False, False)

# Centraliza a janela na tela
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Cria um widget Label para exibir a imagem do QRCode
Image_view = Label(app, bg='#262626')
Image_view.pack(padx=50, pady=30)

# Cria um rótulo (label) e uma entrada (entry) para o link do site
Label(app, text='Link do site: ', fg='white', font=15).place(x=130, y=320)
entry = ttkbootstrap.Entry(app, width=27, font='Arial 15')
entry.place(x=20, y=352)

# Cria botões para gerar e salvar o QRCode
ttkbootstrap.Button(app, text='Gerar', bootstyle='info', width=15, command=generate).place(x=50, y=412)
ttkbootstrap.Button(app, text='Salvar', bootstyle='success', width=10, command=save_qrcode_as).place(x=195, y=412)

# Inicia o loop principal da aplicação
app.mainloop()
