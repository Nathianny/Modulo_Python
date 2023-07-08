# Exemplo 1: Impressão de números de 1 a 10

print();
for numero in range(1, 11):
    print(numero);
print();

# Exemplo 2: Impressão de frutas de uma lista de frutas

frutas = ["maçã", "laranja", "uva"];

for fruta in frutas:
    print(fruta);
print();

# Exemplo 2.1:

frutas = ["maçã", "laranja", "uva"];
for fruta in frutas:
    if fruta == "laranja":
        continue;
    print(fruta);
print();

# Exemplo 2.2

frutas = ["maçã", "laranja", "uva"];
for fruta in frutas:
    if (fruta == "laranja"):
        break;
    print(fruta);
print();

# Exemplo 3: Cálculo da média de uma lista de notas

notas = [7.5, 8.00, 6.5, 9.0, 7.0];
soma = 0;

for nota in notas:
    soma += nota;
media = soma / len(notas);
print("A média das notas é:", media);
print();

#Exemplo 4: Contando as vogais de uma String

palavra = "Python";
vogais = 0;

for letra in palavra:
    if letra in "aeiou":
        vogais += 1;
print(f"A palavra {palavra} possu {vogais} vogais.");
print();

# Exemplo 5: Interação sobre os itens de uma lista

lista = ["a", "b", "c", "d", "e"];

for indice in range(len(lista)):
    print(f"O elemento no índice {indice} é {lista[indice]}");
print();

# Exemplo 6: Interação sobre um elemento número com incremento

for numero in range(1, 11, 2):
    print(numero);
print();