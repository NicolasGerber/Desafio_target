frase = ("Esta frase sera invertida!")
frase_invertida = ''
for i in range(len(frase)-1,-1,-1):
    frase_invertida+=frase[i]
print(frase_invertida)

