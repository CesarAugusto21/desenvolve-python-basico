frase = input("Digite uma frase: ")
vogal =  "aeiouAEIOU"
frase_consoante = frase.replace("a", "*")
frase_consoante2 = frase_consoante.replace("e", "*")
frase_consoante3 =frase_consoante2.replace("i", "*")
frase_consoante4 = frase_consoante3.replace("o", "*")
frase_consoante5 = frase_consoante4.replace("u", "*")
frase_consoante6 = frase_consoante5.replace("A", "*")
frase_consoante7 = frase_consoante6.replace("E", "*")
frase_consoante8 = frase_consoante7.replace("I", "*")
frase_consoante9 = frase_consoante8.replace("O", "*")
frase_consoante10 = frase_consoante9.replace("U", "*")

print(frase_consoante10)