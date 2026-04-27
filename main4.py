import random
import time

numero = random.randint(1, 20)
print('Este jogo é um jogo de adivinha...')
time.sleep(2)
print('Ele consiste em você chutar um numero e tentar adivinhar...')
time.sleep(2.8)
print('Porem o computador ira te ajudar...')
time.sleep(2)
print('Se você errar ele ira dizer se o numero é maior ou menor que seu chute...')
time.sleep(3)
print('>>> Vamos Comecar <<<')

chute = int(input('Você acha que é qual número? '))

while chute != numero:
    if chute < numero:
        print('Não, o número é MAIOR que', chute)
    elif chute > numero:
        print('Não, o número é MENOR que', chute)

    chute = int(input('Você acha que é qual número? '))

print('>>> Parabéns, você acertou o número', numero, '! <<<')
