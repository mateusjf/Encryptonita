from tkinter import *
from cAscii import *
from cUnicode import *

class MeuCripter(object):
	def __init__(self, janela):

		janela.maxsize(width = 200, height= 99)
		janela.minsize(width = 200, height= 99)
		janela.iconbitmap('kryptonita-591633.ico')

		self.frameLabel = Frame(janela)
		self.label =  Label(self.frameLabel, text = 'Criptografia')

		janela.title('Encryptonita')

		self.frameLabel.pack()
		self.label.pack()

		self.frameBotoes = Frame(janela)
		self.botao1 = Button(self.frameBotoes, text = "Unicode", width = 30, command = self.geraUni)
		self.botao2 = Button(self.frameBotoes, text = "ASCII", width = 30, command = self.geraAsci)
		self.botao3 = Button(self.frameBotoes, text = "Arquivo - ASCII", width = 30, command = self.arqAsc)

		self.frameBotoes.pack()
		self.botao1.pack()
		self.botao2.pack()
		self.botao3.pack()

		janela.mainloop()

	def geraUni(self):
		unic = Uc()

	def geraAsci(self):
		asc2 = Ac()

	def arqAsc(self):
		arq = Arq()


		
janela = Tk()

app = MeuCripter(janela)
