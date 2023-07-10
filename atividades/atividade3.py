# Questão 1- Escreva um programa que solicite ao usuário dois números
# inteiros e exiba a soma, subtração, multiplicação e divisão entre esses números.

n1 = int(input("Digite o 1º número: "));
n2 = int(input("Digite o 2º número: "));

soma          = n1 + n2;
subtracao     = n1 - n2;
multiplicacao = n1 * n2;
divisao       = n1 / n2;

print("A soma dos números é:", soma);
print("A subtração dos números é:", subtracao);
print("A multiplicação dos números é:", multiplicacao);
print("A divisão dos números é:", divisao);


# Questão 2 - Escreva um programa que solicite ao usuário uma temperatura
# em graus Celsius e verifique se ela está acima do ponto de ebulição da água (100°C). 
# Caso positivo, exiba a mensagem "A água está fervendo!".

temperatura = float(input("Digite a temperatura: "));

if temperatura > 100:
    print(f"A água está fervendo!");
else:
    print(f"A água não está fervendo!");


# Questão 3 - Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é par ou ímpar.

numInt = int(input("Digite um número inteiro: "));

if numInt % 2 == 0:
    print(f"O número informado é par!")
else:
    print(f"O número informado é ímpar!")


# Questão 4 - Escreva um programa que solicite uma senha ao usuário e verifique se a senha está correta.
# Considere a senha correta como "123456".

senha = input("Digite sua senha: ");
senhaCorreta = "123456";

if senha == senhaCorreta:
    print("Senha correta!");
else:
    print("Senha incorreta!");
  

# Questão 5 - Escreva um programa que solicite ao usuário uma idade e verifique se ela está entre 18 e 30 anos (inclusive).

idade = int(input("Digite a sua idade: "));

if idade >= 18 and idade <= 30:
    print("Idade dentro do padrão exigido.");
else:
    print("Idade fora do padrão exigido.");


# Questão 6 - Escreva um programa que solicite ao usuário três números inteiros e verifique se pelo menos um deles é positivo.

n1 = int(input("Digite o 1º número inteiro: "));
n2 = int(input("Digite o 2º número inteiro: "));
n3 = int(input("Digite o 3º número inteiro: "));

if (n1 > 0) or (n2 > 0) or (n3 > 0):
    print("Pelo menos um dos números informados é positivo!");
else:
    print("Todos os números informados são negativos ou zero.");


# Questão 7 - Escreva um programa que solicite ao usuário uma letra e verifique se ela é uma vogal (a, e, i, o, u).

letra = input("Digite uma letra: ");

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("É uma vogal!");
else:
    print("Não é uma vogal!");


# Questão 8 - Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

num = int(input("Digite um número inteiro: "));

if num > 0:
    print(f"O número informado é positivo!");
elif num < 0:
    print(f"O número informado é negativo!");
else:
    print(f"O número digitado é {num}!");


# Questão 9 - Escreva um programa que solicite ao usuário três números e verifique se eles estão em ordem crescente.

n1 = float(input("Digite o 1º número: "));
n2 = float(input("Digite o 2º número: "));
n3 = float(input("Digite o 3º número: "));

if n1 < n2 < n3:
    print(f"Os números informados estão em ordem crescente!");
else:
    print(f"Os números informados não estão em ordem crescente!");


# Questão 10 - Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.

numInt = int(input("Digite um número inteiro: "));

if numInt % 3 == 0 and numInt % 5 == 0:
    print("O número é múltiplo de 3 e 5 ao mesmo tempo!");
else:
    print("O número não é múltiplo de 3 e 5 ao mesmo tempo!");
