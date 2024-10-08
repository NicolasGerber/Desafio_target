numero = int(input("Escreva um numero inteiro:"))

limite = 30 #Numero Limitante da sequência
lista_fib = [0,1]
for i in range (2,limite):
    lista_fib.append(lista_fib[i-1] + lista_fib[i-2]) #Adiciona no final do vetor a soma dos dois numeros anteriores
if lista_fib.__contains__(numero):
    print(f"O numero {numero} faz parte da sequência de Fibonacci")
else:
    print(f"O numero {numero} não faz parte da sequência de Fibonacci")




