# Exemplo de programa que aborda o tipo de dado numérico em Python

# Operadores matemáticos básicos
num1 = 10;
num2 = 5;

soma          = num1 + num2;
subtracao     = num1 - num2;
multiplicacao = num1 * num2;
divisao       = num1 / num2;
resto         = num1 % num2;
potencia      = num1 ** num2;

print("Operações de matemática básicas: ");
print("Soma: ", soma);
print("Subtração: ", subtracao);
print("Multiplicação: ", multiplicacao);
print("Divisão: ", divisao);
print("Resto: ", resto);
print("Potência: ", potencia);
print();

# Arredondamento de número
numeroFloat = 3.14;
numeroArredondado = round(numeroFloat);
print("Arredondamento: ", numeroArredondado);
print();

#Funções matemáticas da biblioteca math
import math

num = 4.7;
print("Funções matemáticas: ");
print("Valor absoluto: ", abs(-4.7));
print("Arredondamento para cima: ", math.ceil(num));
print("Arredondamento para baixo: ", math.floor(num));
print();

# Geração de números aleatórios
import random
print("Números aleatórios: ");
print("Números aleatórios de 1 a 10: ", random.randint(1, 10));
print("Número float aleatório entre 0 e 1: ", random.random());
print();

# Formatação de números
numeroFormatado = 1234.56789;
print("Formatação de números: ");
print(f"Número com 2 casas decimais {numeroFormatado:.2f}");
print("Número com 2 casas decimais {:.2f}".format(numeroFormatado));
print();