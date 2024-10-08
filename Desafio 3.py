import json #importando a biblioteca json

arquivo = open('faturamento.json','r')
dados = json.load(arquivo)
menor = dados[0]['valor']
maior = dados[0]['valor']
menor_dia = 0
maior_dia = 0
superior = 0
soma_total = 0
media = 0
sem_faturamento = 0
for dado in dados:
    if dado['valor'] == 0.0:
        sem_faturamento+=1
        continue   #Se quiser considerar 0.0 como menor valor de faturamento remover o 'continue'
    if  dado['valor'] < menor:
        menor = dado['valor']
        menor_dia = dado['dia']
    if  dado['valor'] > maior:
        maior = dado['valor']
        maior_dia = dado['dia']
    soma_total = soma_total + dado['valor']

media = soma_total / (len(dados) - sem_faturamento)
for dado in dados:
    if dado['valor'] > media:
        superior+=1
print(f"O menor valor de faturamento ocorrido em um dia do mês, foi no dia {menor_dia} e foi de {menor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês, foi no dia {maior_dia} e foi de {maior:.2f}")
print(f"O Número de dias no mês em que o valor de faturamento diário foi superior à média mensal {media:.2f} foram {superior} dias.")





