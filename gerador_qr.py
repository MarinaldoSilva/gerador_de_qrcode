import qrcode

#link que será códificado
dados = "https://github.com/MarinaldoSilva"

#gerando a matriz e criando um obj da imagem com o pillow
img_qr = qrcode.make(dados)

diretorio = "qr-github.png"

#salvando a imagem na raiz do projeto
img_qr.save(diretorio)

print("gerado com sucesso!")