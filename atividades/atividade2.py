# Questão 1 - Crie uma lista chamada "frutas" contendo as seguintes frutas:
# maçã, banana, laranja, abacaxi e melancia. Em seguida, exiba a lista completa na tela.

listaFrutas = ["maçã", "banana", "laranja", "abacaxi", "melancia"];

print(listaFrutas);

# Questão1 2- Adicione a fruta "uva" à lista "frutas" utilizando o método append(). 
# Exiba a lista atualizada na tela.

listaFrutas.append("uva");

print(listaFrutas);

# Questão1 3- Remova a fruta "banana" da lista "frutas" utilizando o método remove(). 
# Exiba a lista atualizada na tela.

listaFrutas.remove("banana");

print(listaFrutas);

# Questão1 4- Acesse o segundo elemento da lista "frutas" e armazene-o em uma variável chamada "fruta_selecionada". 
# Em seguida, exiba o valor armazenado na variável.

fruta_selecionada = (listaFrutas[1]);

print(fruta_selecionada);

# Questão1 5- Crie uma tupla chamada "cores" contendo as seguintes cores:
# vermelho, azul, verde, amarelo e roxo. Em seguida, exiba a tupla completa na tela.

cores = ("vermelho", "azul", "verde", "amarelo", "roxo");

print(cores);

# Questão1 6- Acesse o terceiro elemento da tupla "cores" e armazene-o em uma variável chamada "cor_selecionada". 
# Em seguida, exiba o valor armazenado na variável.

cor_selecionada = cores[2];

print(cor_selecionada);

# Questão1 7- Tente adicionar a cor "laranja" à tupla "cores" e observe o resultado. 
# Explique o motivo pelo qual ocorreu um erro fazendo um comentário no código.

#cores.append("laranja");

#AttributeError: 'tuple' object has no attribute 'append'

# Tuplas são imutáveis, sendo assim, não aceitam alterações.

# Questão1 8- Crie um dicionário chamado "aluno" contendo as seguintes informações: 
# nome, idade e cidade. Utilize as chaves "nome","idade" e "cidade" para representar cada informação.
# Em seguida, exiba o dicionário completo na tela.

aluno = {
    'nome'  : 'marcos',
    'idade' : 48,
    'cidade': 'osasco'
}

print(aluno);

# Questão1 9- Acesse a idade do aluno no dicionário "aluno" e armazene-o em uma variável chamada "idade_aluno". 
# Em seguida, exiba o valor armazenado na variável.

idade_aluno = aluno['idade'];

print(idade_aluno);

# Questão1 10- Adicione a informação do gênero do aluno ao dicionário "aluno" utilizando a chave "gênero" e o valor correspondente. 
# Exiba o dicionário atualizado na tela.

aluno['genero'] = 'masculino';

print(aluno);

# Questão1 11 - Remova a informação da cidade do dicionário "aluno" utilizando o método pop() 
# e a chave correspondente. Exiba o dicionário atualizado na tela.

aluno.pop("cidade");

print(aluno);