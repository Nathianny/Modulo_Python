# Exemplo de programa que aboda o tipo de dado string em Python

frase = "Olá mundo!";
# Declaração de uma String
print("String original: ");
print(frase);
print();

# Acessando caracteres individuais
print("Acessando caracteres individuais: ");
print("Primeiro caractere: ", frase[0]);
print();

print("Acessando caracteres individuais: ");
print("Ultimo caractere: ", frase[-1]);

# Utilizando o input para pegar o nome informado pelo usuário
nome = input("Nome: ");
print(nome);
print();

# Inserindo as variáveis no print com f
print(f"Bem-vindo {nome}");
print("Bem-vindo {}".format(nome));
print();

# Concatenando strings
print("Concatenando strings: ");
outraFrase = "Bem-vindo";
fraseCompleta = frase + " " + outraFrase;
print(fraseCompleta);

# Tamanho da spring
tamanho = len(frase);
print("Tamanho: ", tamanho);
print();

# Dividindo uma string em sub strings
print("Dividindo a string: ");
palavras = fraseCompleta.split();
print(palavras);
print();

# Substituindo partes das strings
print("Substituindo partes das strings: ");
novaFrase = frase.replace("mundo", "Python");
print(novaFrase);
print();

# Convertendo para letras maiúsculas e minúsculas
print("Convertendo para letras maiúsculas e minúsculas: ");
print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());
print();