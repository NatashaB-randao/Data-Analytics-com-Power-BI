## Descrição
# Calcular a média é uma das operações estatísticas mais básicas e úteis para resumir um conjunto de dados. Dada uma lista de números, você deve calcular a média aritmética desses números.

# Documentação: https://docs.python.org/pt-br/dev/library/functions.html

# #Entrada
# Uma lista de números. Por exemplo:10, 20, 30, 40, 50.

## Saída
# Um número representando a média dos números na lista. Por exemplo: 30.0. O que fazer: Somar todos os números e dividir pela quantidade de elementos na lista.





# Receber a lista do usuário
entrada = input()
# Converte a string de entrada em uma lista de números
lista = [float(x.strip()) for x in entrada.split(',')]


# Calcula a soma dos números na lista
soma = sum(lista)
# Calcula a quantidade de elementos na lista
quantidade = len(lista)
# Calcula a média aritmética
media = soma / quantidade


# Exibe a média com uma casa decimal
print(f'{media:.1f}')