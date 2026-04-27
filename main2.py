frase=input('Escreva um frase ou uma palavra : ')
vogais=('ÁAÀÂÃÄaáàâãäÉEÈÊËéèeêëÍÌIÎÏíìiîïÓÒÔÕOÖóòoôõöÚÙUÛÜúùûuü')

quan=len([letra for letra in frase if letra in vogais])

print(frase,'contem',quan,'de vogais')
