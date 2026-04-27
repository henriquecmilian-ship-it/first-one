import random

caracteres="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

quantidade=input("Digite a quantidade de caracteres para a senha: ")

senha=""

for quantidade in range(int(quantidade)):
    senha+=random.choice(caracteres)
print("Senha gerada:",'{}'.format(senha))

gotou=input=('está satisfeito com a senha gerada? (s/n)')


if gotou=='s':
    print("perfeito")
elif gotou=='n':
    novamente=input=("quer gerar uma nova senha?")
    
    if novamente=='s':
        senha=""
        for quantidade in range(int(quantidade)):
            senha+=random.choice(caracteres)
        print("Nova senha gerada:",'{}'.format(senha))
    elif novamente=='n':
        print("Adeus!")
