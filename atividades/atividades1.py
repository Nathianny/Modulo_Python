
nome = "Nathianny";
sobreNome = "Pereira";
idade = 27
frase = "Obrigado pela preferência, cliente ";

# Questão 1
print(f"Olá, meu nome é {nome} e tenho {idade} anos");

# Questão 2
print(len(frase));

# Questão 3
nome_completo = nome + " " + sobreNome;
print(nome_completo);

# Questão 4
print(frase.upper());

# Questão 5
print(frase.split());

# Questão 6
novaFrase = frase.replace("Obrigado", "preferência");
print(novaFrase);

# Questão 7
numero1 = 145
numero2 = 555
resultado = numero1 + numero1;
print(resultado);

# Questão extra
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
multiplicacao = numero1 * numero2
print("O resultado da multiplicação é:", multiplicacao)