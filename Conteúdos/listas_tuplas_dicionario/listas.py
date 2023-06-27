listaNumeros = [1,2,3,4,5];
listaStrings = ["a","b","c","d","e"];
listaMista =   [1,"a",3.14,True];
print(listaNumeros);
print(listaStrings);
print(listaMista);

frutas = ["maçã", "banana", "morango"];
print(frutas[1]);
# Alterando algum valor da lista
frutas[1] = "goiaba";
print(frutas);
print();
# Adicionando um valor na lista com o método append()
frutas.append("jabuticaba");
print(frutas);
print();
# Contando a quantidade de itens na lista com o método len()
print(f"Agora temos {len(frutas)} frutas em nossa lista.")

#
novaLista = [1, ["a", "b"]];
print(novaLista[1][0]);
print();

# Concatenando listas
lista1 = [1,2,3];
lista2 = [4,5,6];
listaConcatenada = lista1 + lista2;
print(listaConcatenada);
print();

# Repetindo a lista
listaRepetida = [0] * 4;
print(listaRepetida);
print();

#
letras  = ["a", "b", "c", "d"];
sublista = letras[1:4];
print(sublista);
print();

# Reforçando o método append()
frutas = ["maçã", "banana", "laranja"];
frutas.append("morango");
print(frutas);
print();

# Inserindo valores em lugares específicos na lista com o método insert()
frutas.insert(1, "abacaxi");
print(frutas);
print();

"""
Removendo valores da lista, definitivo (nesse caso não terá retorno na variável frutaRemovida) 
com o método remove()
"""
frutaRemovida = frutas.remove("banana");
print(frutas);
print(frutaRemovida);
print();

"""
Removendo um valor da lista, porém deixando possível localizar ele 
(nesse exemplo ele mostra a fruta que foi removida) com o método pop()
"""
frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);
print();

# Ordenando os valores da lista em ordem alfabética com o método sort()
frutas.sort();
print(frutas);
print();