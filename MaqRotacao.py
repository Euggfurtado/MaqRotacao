#Eugenio Furtado Ferreira

import numpy as np

cilindro0 = [[1, 2],
			[2,4],
			[3,6],
			[4,8],
			[5,10],
			[6,12],
			[7,14],
			[8,16],
			[9,18],
			[10,20],
			[11,22],
			[12,24],
			[13,26],
			[14,3],
			[15,5],
			[16,7],
			[17,9],
			[18,11],
			[19,13],
			[20,15],
			[21,17],
			[22,19],
			[23,21],
			[24,23],
			[25,25],
			[26,1]]



cilindro1 = [[7, 1],
			[8,2],
			[9,3],
			[10,4],
			[11,5],
			[13,6],
			[1,7],
			[12,8],
			[5,9],
			[6,10],
			[26,26],
			[20,25],
			[22,24],
			[15,23],
			[18,22],
			[3,21],
			[2,20],
			[4,19],
			[16,11],
			[24,12],
			[25,13],
			[14,14],
			[23,15],
			[21,16],
			[19,17],
			[17,18]]


cilindro2 = [[26,25],
			[25,23],
			[24,21],
			[23,1],
			[22,3],
			[21,5],
			[20,7],
			[19,9],
			[18,19],
			[17,17],
			[16,15],
			[15,11],
			[14,13],
			[13,2],
			[12,4],
			[11,6],
			[10,8],
			[9,10],
			[8,26],
			[7,24],
			[6,22],
			[5,20],
			[4,12],
			[3,16],
			[2,14],
			[1,18]]


# Função para ler o arquivo com a mensagem base original que será criptografada
def lerArquivo():

    mensagem = " "

    # abre o arquivo para leitura
    arquivo = open('texto.txt','r')

    # salva na variável mensagem o conteúdo do arquivo
    for linha_arq in arquivo:
        mensagem+=linha_arq
    arquivo.close()

    # trata os caracteres especiais(Espaço, Ponto, Virgula e a Quebra de Linha)
    mensagem = mensagem.replace(" ","")
    mensagem = mensagem.replace(".","")
    mensagem = mensagem.replace(",","")
    mensagem = mensagem.replace("\n","")

    # mensagem de confirmação e retorno com a mensagem
    print("Arquivo Base Lido Com Sucesso")
    return mensagem


def transAscii(txt):
	vetorAscii = []
	for i in range(len(txt)):
		aux = (ord(txt[i])-96)
		vetorAscii.append(aux)
	return vetorAscii

def criptografia(txt):
	entradaC0 = 0
	saidaC0 = 0
	entradaC1 = 0
	saidaC1 = 0
	entradaC2 = 0
	saidaC2 = 0
	txtCifrado = []
	movC0=0
	movC1=0
	movC2=0
	for i in range(len(txt)):
		entradaC0 = txt[i]
		print("---------------Começo----------------")
		print("entradaC0 %d" %(entradaC0))
		for j in range(26):
			aux0 = (j + movC0)%26

			if(entradaC0 == cilindro0[aux0][1]):				
				saidaC0 = aux0 
				print("cilindro0  %d" %(cilindro0[j][1]))
				print("SaidaC0 POSICAO %d" %(saidaC0))
				break
			if(j==25):
				print("Erro")
				exit()
		entradaC1 = cilindro1[j][0]
		print("-------------------------------")
		print("entradaC1 %d" %(entradaC1))

		for x in range(26):
			aux1 = (x + movC1)%26
			if(entradaC1 == cilindro1[aux1][1]):	

				saidaC1 = aux1
				#print("cilindro1 %d" %(cilindro1[saidaC1][1]))
				#print("SaidaC1 POSICAO %d" %(saidaC1))
				break
			if(x==25):
				print("Erro")
				exit()

		entradaC2 = cilindro2[x][0]
		#print("-------------------------------")
		#print("entradaC2 %d" %(entradaC2))

		for z in range(26):
			aux2 = (z + movC2)%26
			if(entradaC2 == cilindro2[aux2][1]):	

				saidaC2 = aux2 
				#print("cilindro2 %d" %(cilindro2[saidaC2][1]))
				#print("SaidaC2 POSICAO %d" %(saidaC2))
				break
			if(z==25):
				print("Erro")
				exit()
		letraSaida = saidaC2 + 97
		txtCifrado.append(chr(letraSaida))
		#print("-----------End---------------")
		movC0 += 1
		if(movC0>=26):
			movC1 +=1
			movC0 = 0
			if (movC1>=26):
				movC2 +=1
				movC1 = 0
				if (movC2>=26):
					movC2 = 0

	return txtCifrado


		

texto=lerArquivo()
texto = transAscii(texto)
saida = criptografia(texto)
print(saida)