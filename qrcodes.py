import qrcode

def criar(text, author):
  img = qrcode.make(text)
  img.save(author+"Resuminho.png")