from tkinter import *
from functools import partial

class Ac(object):
	def __init__(self):

		self.chave = [1,0,-1,0,2,0,-2,3,0,-3,4,0,-4,0,-5]
		self.chav2 = [0,-5,0,4,0,-4,3,0,-3,2,0,-2,1,0,-1]

		self.janelaASCII = Tk()

		self.janelaASCII.title('Encryptonita - ASCII')
		self.janelaASCII.maxsize(width = 475, height = 215)
		self.janelaASCII.minsize(width = 475, height = 215)
		self.janelaASCII.iconbitmap('kryptonita-591633.ico')

		self.frameLabel = Frame(self.janelaASCII)
		self.label = Label(self.frameLabel, text = 'Criptografia ASCII', pady = 10)

		self.frameInput = Frame(self.janelaASCII)
		self.frameString = Frame(self.frameInput)
		self.frameBotoes = Frame(self.janelaASCII, pady = 10)

		self.labelString = Label(self.frameString, text = 'Digite sua string')
		self.inputS = Entry(self.frameString, width = 75)

		self.bCripta = Button(self.frameBotoes, text = 'Encriptar', command = partial(self.cript, None))
		self.bDescript = Button(self.frameBotoes, text = 'Desencriptar', command = partial(self.descript, None))

		self.frameSaida = Frame(self.janelaASCII)
		self.labelSaida = Label(self.frameSaida, text = 'Saída')
		self.inputSaida = Entry(self.frameSaida, width = 75)

		self.frameLabel.pack()
		self.label.pack()

		self.frameInput.pack()
		self.frameString.pack()
		self.frameBotoes.pack()

		self.labelString.pack()
		self.inputS.pack()

		self.bCripta.pack(side = LEFT)
		self.bDescript.pack(side = RIGHT)

		self.frameMensagem = Frame(self.janelaASCII, pady  = 10)
		self.mensagem = Label(self.frameMensagem, text = '', fg = 'red')

		self.frameMensagem.pack()
		self.mensagem.pack()

		self.frameSaida.pack()
		self.labelSaida.pack()
		self.inputSaida.pack()

		self.janelaASCII.mainloop()

	def entraDados(self,dados):
		string = None
		if dados == None:
			string = self.inputS.get()
		elif type(dados) == str:
	
		
			string = dados

		return string

	def cript(self,tipo):

		textoCript = ''
		string = self.entraDados(tipo)
	

		j = 0
		k = 0
		l = 0
		try:

			for i in range(0,len(string)):

				if j == len(self.chave):
					j = 0

				if k == len(self.chav2):
					k = 0

				if l > 3:
					l = 0

				letra = ord(string[i]) + self.chave[j]
				letra = chr(letra + self.chav2[k])

				textoCript += letra
				j += 1
				k += 1
				l += 1
	
			print(textoCript)

			if type(tipo) == str:
				return textoCript

			self.inputSaida.delete(0,END)
			self.inputSaida.insert(END, textoCript)

			self.mensagem['fg'] = 'blue'
			self.mensagem['text'] = 'Texto criptografado.'

		except:
			self.mensagem['fg'] = 'red'
			self.mensagem['text'] = 'Não foi possivel criptografar a texto.'

	#	finally:
	#		print('\nProcesso concluído.')

	def descript(self,tipo):

		textoCript = ''
		string = self.entraDados(tipo)

		j = 0
		k = 0
		l = 0

		try:

			for i in range(0,len(string)):

				if j == len(self.chave):
					j = 0

				if k == len(self.chav2):
					k = 0

				if l > 3:
					l = 0

				letra = ord(string[i]) - self.chave[j]
				letra = chr(letra - self.chav2[k])

				textoCript += letra
				j += 1
				k += 1
				l += 1

			if type(tipo) == str:
				return textoCript

			self.inputSaida.delete(0,END)
			self.inputSaida.insert(END, textoCript)

			self.mensagem['fg'] = 'blue'
			self.mensagem['text'] = 'Texto descriptografado.'

			print('\n{}'.format(textoCript))
			print(string)


		except:
			self.mensagem['fg'] = 'red'
			self.mensagem['text'] = 'Não foi possivel descriptografar a texto.'



class Arq(Ac):
	def __init__(self):
		janelaArq = Tk()

		janelaArq.title('Encryptonita - ASCII (ARQUIVO)')
		janelaArq.maxsize(width = 470, height = 150)
		janelaArq.minsize(width = 470, height = 150)
		janelaArq.iconbitmap('kryptonita-591633.ico')

		self.chave = [1,0,-1,0,2,0,-2,3,0,-3,4,0,-4,5,0,-5]
		self.chav2 = [5,0,-5,0,4,0,-4,3,0,-3,2,0,-2,1,0,-1]
		#appUc = Uc(janelaUni)
		self.frameLabel = Frame(janelaArq)
		self.label = Label(self.frameLabel, text = 'Criptografia Arquivo (ASCII)', pady = 10)

		self.frameInput = Frame(janelaArq)
		self.frameCaminho = Frame(self.frameInput, padx = 5)
		self.frameBotoes = Frame(janelaArq, pady = 10)


		self.labelCaminho = Label(self.frameCaminho, text = 'Digite o caminho do arquivo.')
		self.inputC = Entry(self.frameCaminho, width = 75)

		self.bCripta = Button(self.frameBotoes, text = 'Encriptar', width = 25, command = self.arqCript)
		self.bDescript = Button(self.frameBotoes, text = 'Desencriptar', width = 25, command = self.arqDescript)

 ##COLOCA PACOTE

		self.frameLabel.pack()
		self.frameInput.pack()
		self.label.pack()

		self.frameCaminho.pack()
		self.frameBotoes.pack()


		self.labelCaminho.pack()
		self.inputC.pack()

		self.bCripta.pack(side = LEFT)
		self.bDescript.pack(side = RIGHT)

		self.frameMensagem = Frame(janelaArq, pady = 5)
		self.mensagem = Label(self.frameMensagem, text = '', fg = 'red')

		self.frameMensagem.pack()
		self.mensagem.pack()

		janelaArq.mainloop()

	def dadosArq(self):
		caminhoArq = self.inputC.get()
		print(caminhoArq)
		try:
			arquivo = open(caminhoArq, 'r')
			textoArq = arquivo.read()
			#print(textoArq)
			arquivo.close()
			return textoArq, caminhoArq, True
		except:
			self.mensagem['fg'] = 'red'
			self.mensagem['text'] = 'Não foi possivel abrir o arquivo.'
			#print('\nNão foi possivel abrir o arquivo.')
			return None, None, False


	def arqCript(self):
		textoArq = ''
		arqString, caminhoArq, existe = self.dadosArq()
		if existe == True:
			try:			
				textoArq = self.cript(arqString)
				arquivo = open(caminhoArq, 'w')
				arquivo.write(textoArq)
				arquivo.close()

				self.mensagem['fg'] = 'blue'
				self.mensagem['text'] = 'Arquivo criptografado.'
			except a:
				self.mensagem['fg'] = 'red'
				self.mensagem['text'] = 'Não foi possivel criptografar o arquivo.'
				#print('\nNão possivel criptografar o arquivo.')

			finally:
				print('\nProcesso concluído.')


	def arqDescript(self):
		textoArq = ''
		arqString, caminhoArq, existe = self.dadosArq()
		if existe == True:
			try:			
				textoArq = self.descript(arqString)
				arquivo = open(caminhoArq, 'w')
				#print(textoArq)
				arquivo.write(textoArq)
				arquivo.close()

				self.mensagem['fg'] = 'blue'
				self.mensagem['text'] = 'Arquivo descriptografado.'
			except:
				self.mensagem['fg'] = 'red'
				self.mensagem['text'] = 'Não foi possivel descriptografar o arquivo.'
				#print('\nNão possivel descriptografar o arquivo.')

			finally:
				print('\nProcesso concluído.')