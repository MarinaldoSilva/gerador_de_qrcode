import qrcode
import tkinter as tk
from tkinter import filedialog #janelas de 'salvar como'

def gerar_qr():
    txt_p_qr = entrada_texto_p_qr.get()

    if txt_p_qr:
        img_qr = qrcode.make(txt_p_qr)

        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".png",
            initialfile="qr_code.png",
            title="salvar QRcode"
        )
        if caminho_arquivo:
            img_qr.save(caminho_arquivo)
            rotulo_status.config(text=f"QR Code salvo com sucesso.", fg="green")
    else:
        rotulo_status.config(text="Digite um texto para ser convertido")

#criando janela
janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.config(padx=20, pady=20)#padding do espaço interno nos eixos x e y

msg_label = tk.Label(janela, text="Digite o que vai virar um QR Code: ")
entrada_texto_p_qr = tk.Entry(janela, width=50)
bnt_gerar = tk.Button(janela, text="Gerar e salvar QR Code")
rotulo_status = tk.Label(janela, text="",pady=10)
label_footer = tk.Label(janela, text="Desenvolvido por Marinaldo Silva", fg="red")

#a função pack(), empacota tudo dentro da janela(tk.TK) um abaixo do outro, como se fosse uma lista

label_footer.pack(side=tk.BOTTOM, pady=5)#side=tk.BOTTOM, estou dizendo que vai ficar fixo abaixo
msg_label.pack()
entrada_texto_p_qr.pack()
bnt_gerar.pack(pady=10)
rotulo_status.pack()

#bnt com o link para a função gerar_qrcode
bnt_gerar.config(command=gerar_qr)
janela.mainloop()






