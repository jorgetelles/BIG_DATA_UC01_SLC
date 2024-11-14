#promama prestação em atraso 
prestação = float ( input ("informe o valor da prestação:"))
taxa = float(input("informe a taxa mensal:"))
tempo = float(input("informe a quantidade de meses em atraso:"))
valor_final = prestação +(prestação*(taxa/100)*tempo)
print(f"ovalor final da prestação é R${valor_final:.2f}")
