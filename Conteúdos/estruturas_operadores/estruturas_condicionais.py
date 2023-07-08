"""
Estruturas condicionais
"""

# Verificação de idade para entrada em um clube noturno
idade = int(input("Digite sua idade:"));
if idade >= 18:
    print("Seja bem-vindo(a), curta nossa festa!");
    print();
else:
    print("Desculpe, não é permitido a entrada de menores de idade em nosso estabelecimento!");
    print();
    
# Verifica se um número está dentro de um intervalo, entre 10 e 20
numero = 15;
if numero >= 10 and numero <= 20:
    print("O número está dentro do intervalo.");
    print();
else:
    print("O número não está dentro do intervalo.")
    print();
    
# Comparar o tamanho de duas listas
lista1 = [1,2,3,4,5];
lista2 = [1,2,3,4,5];
if len(lista1) > len(lista2):
    print("A lista 1 é maior que a lista 2!");
    print();
elif len(lista2) > len(lista1):
    print("A lista 2 é maior que a lista 1!");
    print();
else:
    print("As listas tem o mesmo tamanho.");
    print();
    
# Verificação de acesso em um sistema
senha = input("Digite sua senha:");
senhaCorreta = "123456";
if senha == senhaCorreta:
    print("Usuário logado com sucesso!");
    print();
else:
    print("A senha informada está incorreta!");
    print();
    
# Verificação de acesso de um sistema com login e senha
usuario = input("Digite seu usuário: ");
senha = input("Digite sua senha: ");

usuarioCorreto = "admin";
senhaCorreta   = "admin";

if usuario == usuarioCorreto and senha == senhaCorreta:
    print("Login bem-sucedido!");
    print();
else:
    print("Usuário ou senha incorreto!");
    print();

# Verificação de múltiplas condições com "and" ou "or"
numero = 10;

if (numero > 0 and numero < 5) or (numero > 10 and numero < 15):
    print("O número atende aos critérios.");
    print();
else:
    print("O número não atende aos critérios.");
    print();

    
# Verificação de uma condição negada
# Verificar se uma pessoa está apta a dirigir
idade = int(input("Informe sua idade: "));
possuiCarteira = False;

if idade>= 18 and not possuiCarteira:
    print("Você precisa de ter a CNH!");
    print();
else:
    print("Você está apto a dirigir.");
    print();
    
# Match Case
comando = "Olá mundo!";

match comando:
    case "Olá mundo!":
        print("Olá para você também!");
        print();
    case "Adeus mundo!":
        print("Adeus!");
        print();
    case _:
        print("Sem resultados!");
        print();