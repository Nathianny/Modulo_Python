# Exemplo 1: Contagem regressiva de 10 a 1

contador = 10;

while contador >= 1:
    print(contador);
    contador -= 1; # Mesma coisa de contador = contador - 1
    print();
    
# Exemplo 2: Leitura de notas de alunos até que uma nota negativa seja inserida

notas = [];
nota = float(input("Digite uma nota (-1 para sair): "));

while nota != -1:
    notas.append(nota);
    nota = float(input("Digite uma nota (-1 para sair): "));
    if nota < -1:
        print("------------------------------------------------------------");
        print("Opção inválida, digite uma nota válida ou -1 para finalizar.");
        print("------------------------------------------------------------");
    
print(notas);
print();

# Exemplo 3: Verificação de senha correta

senha = input("Digite sua senha: ");
contador = 0;
senhaBloqueada = False;

while senha != "123456":
    print("Senha incorreta!");
    contador += 1;
    if contador == 3:
        #print("Senha bloqueada, entre em contato com o administrador.");
        senhaBloqueada = True;
        break;
    senha = input("Digite sua senha: ");
    print();
    
if (senhaBloqueada):
    print("Senha bloqueada, entre em contato com o administrador.");
    print();
else:
    print("Senha correta!");
    print();
    
# Exemplo 4: Impressão dos primeiros N números pares

quantidade = int(input("Informe a quantidade de números pares a serem impressos: "));
contador = 1;

while quantidade > 0:
    if contador % 2 == 0:
        print(contador);
        quantidade -= 1;
    contador += 1;
    
print();
    
# Exempço 5: Jodo da advinhação

numeroSecreto = 42;
palpite = int(input("Digite um número: "));

while palpite != numeroSecreto:
    print("Você errou hahaha! Tente novamente.");
    palpite = int(input("Digite um número: "));
    
print("Parabéns, você acertou o palpite!");
print();

# Exemplo 6: Impressão de uma sequência de caracteres até que a palavra "sair" seja digitada

palavra = input("Digite uma palavra! ('sair' para encerrar): ");
palavra = palavra.lower();

while palavra != "sair":
    print(palavra);
    palavra = input("Digite uma palavra! ('sair' para encerrar): ");
    palavra = palavra.lower();
    
print();

# Exemplo 7: Implementação de menu de opções

opcao = 0;

while opcao != 4:
    print("Menu:");
    print("1 - Opção 1");
    print("2 - Opção 2");
    print("3 - Opção 3");
    print("4 - Sair");
    
    opcao = int(input("Informe a opção escolhida: "))
    
    if opcao == 1:
        print("Opção 1 escolhida!");
        print();
    elif opcao == 2:
        print("Opção 2 escolhida!");
        print();
    elif opcao == 3:
        print("Opção 2 escolhida!");
        print();
    elif opcao == 4:
        print("Saindo...");
        print();
        break;
    else:
        print("Opção inválida!");
        print();
    