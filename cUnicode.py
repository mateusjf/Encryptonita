from tkinter import *

class Uc(object):
	def __init__(self):

		self.CHAVE = ['0', 'A', '1', 'b', '2', 'C', '3', 'd', '4', 'E', '5', 'f']

		self.janelaUni = Tk()
		self.janelaUni.title('Encryptonita - Unicode')
		self.janelaUni.maxsize(width = 480, height = 230)
		self.janelaUni.minsize(width = 480, height = 230)
		self.janelaUni.iconbitmap('kryptonita-591633.ico')
		
		#appUc = Uc(janelaUni)

		self.frameLabel = Frame(self.janelaUni)
		self.label = Label(self.frameLabel, text = 'Criptografia para Unicode', pady = 12)

		self.frameString = Frame(self.janelaUni, padx = 5)
		self.labelString = Label(self.frameString, text = 'Insira a string aqui')
		self.inputS = Entry(self.frameString, width = 77)

		self.frameChavBotao = Frame(self.janelaUni, padx=5)
		self.labelChave = Label(self.frameChavBotao, text = 'Insira a chave', pady = 8)
		self.inputC = Entry(self.frameChavBotao, width = 37)
		self.frameBotao = Frame(self.frameChavBotao, padx = 5)
		self.cBotao = Button(self.frameBotao, text = 'Encripta', width = 15, command = self.cript)
		self.dBotao = Button(self.frameBotao, text = 'Desencripta', width = 15, command = self.descript)

		self.frameMensagem = Frame(self.janelaUni, pady = 8)
		self.mensagem = Label(self.frameMensagem, text = '')

		self.frameSaida = Frame(self.janelaUni)
		self.labelSaida = Label(self.frameSaida, text = 'Saída')
		self.inputSaida = Entry(self.frameSaida, width = 77)


 ##COLOCA PACOTE

		self.frameLabel.pack()
		self.label.pack()

		self.frameString.pack()
		self.labelString.pack()
		self.inputS.pack()

		self.frameChavBotao.pack()
		self.labelChave.pack()
		self.inputC.pack(side = LEFT)
		self.frameBotao.pack(side = RIGHT)
		self.cBotao.pack(side = LEFT)
		self.dBotao.pack(side = RIGHT)

		self.frameMensagem.pack()
		self.mensagem.pack()

		self.frameSaida.pack()
		self.labelSaida.pack()
		self.inputSaida.pack()

		self.janelaUni.mainloop()

	def entradDados(self):
		chaveMestra = []
		texto = self.inputS.get()
		chaveEntrada = self.inputC.get()
		j = 0
		for i in range(0, len(chaveEntrada)):
			if j == len(self.CHAVE):
				j = 0
			chaveMestra.insert(-1, int(ord(chaveEntrada[i]) * ord(self.CHAVE[j])))
			j += 1

		return texto, chaveMestra


	def cript(self):
		self.inputSaida.delete(0,END)
		
		palavraEncript = ''

		texto, chaveCript = self.entradDados()
		
		try:
			j = 0
			for i in range(0,len(texto)):
				if j == len(chaveCript):
					j = 0

				letra = int(ord(texto[i]) + chaveCript[j])
				palavraEncript += chr(letra)
				#print(letra)
				j += 1

			self.inputSaida.insert(END, palavraEncript)

			self.mensagem['fg'] = 'blue'
			self.mensagem['text'] = 'Texto criptografado.'

			print('Texto Encriptado: {}'.format(palavraEncript))
			print('Texto encriptado com sucesso.\n')

		except:
			self.mensagem['fg'] = 'red'
			self.mensagem['text'] = 'Não foi possivel criptografar a texto.'
			print('Não foi possivel criptografar o texto.\n')
		finally:
			print('Processo Concluído')

	def descript(self):
		self.inputSaida.delete(0,END)

		palavraDescript = ''

		texto, chaveCript = self.entradDados()
		
		try:
			j = 0
			for i in range(0, len(texto)):
				if j == len(chaveCript):
					j = 0

				letra = int(ord(texto[i]) - chaveCript[j])
				palavraDescript += chr(letra)
				j += 1

			self.inputSaida.insert(END, palavraDescript)

			self.mensagem['fg'] = 'blue'
			self.mensagem['text'] = 'Texto descriptografado.'

			print('Texto Desencriptado: {}'.format(palavraDescript))
			print('Texto desencriptado com sucesso.\n')
		except:
			self.mensagem['fg'] = 'red'
			self.mensagem['text'] = 'Não foi possivel descriptografar a texto.'

			print('Não foi possivel descriptografar o texto.\n')
			print('1 - Talvez a chave não seja compativel matematicamente com a string ')
		finally:
			print('Processo Concluído')

