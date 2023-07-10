# Questão 1 - Utilizando um loop "While", imprima os números de 1 à 1o.

num = 1

while num <= 10:
    print(num)
    num += 1


# Questão 2 - Utilizando um loop "For", imprima os números de 1 à 1o.

for num in range(1, 11):
    print(num)

# Questão 3 - Utilizando um loop "While", calcule a soma dos números de 1 à 100.

num = 1
soma = 0

while num <= 100:
    soma += num
    num += 1

print("A soma dos números de 1 a 100 é:", soma)

# Questão 4 - Utilizando um loop "For", calcule a soma dos números de 1 à 100.

soma = 0

for num in range(1, 101):
    soma += num

print("A soma dos números de 1 a 100 é:", soma)

# Questão 5 - Utilizando um loop "While", imprima os números pares de 1 à 20.

num = 1

while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# Questão 6 - Utilizando um loop "For", imprima os números pares de 1 à 20.

for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Questão 7 - Utilizando um loop "While", inverta uma string digitada pelo usuário.

string = input("Digite uma string: ")
tamanho = len(string)
string_invertida = ""

while tamanho > 0:
    string_invertida += string[tamanho - 1]
    tamanho -= 1

print("String invertida:", string_invertida)

# Questão 8 - Utilizando um loop "For", verifique se uma palavra digitada pelo usuário é um palíndromo (lê-se da mesma forma de trás pra frente).

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()  # Converter a palavra para letras minúsculas
palavra_pali = True

for i in range(len(palavra)//2):
    if palavra[i] != palavra[-i-1]:
        palavra_pali = False
        break

if palavra_pali:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")

# Questão 9 - Utilizando um loop "While", encontre o menor número inteiro cujo quadrado seja maior do que 1000.

num = 1

while num ** 2 <= 1000:
    num += 1

print("O menor número inteiro cujo quadrado é maior do que 1000 é:", num)

# Questão 10 - Utilizando um loop "For", imprima os elementos de uma lista em ordem inversa.

lista = [1, 2, 3, 4, 5]

for i in range(len(lista)-1, -1, -1):
    print(lista[i])