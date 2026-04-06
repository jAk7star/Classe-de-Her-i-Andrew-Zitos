# Projeto: Herói e Níveis de XP
heroi = "Andrew Zitos"
XP = 5600
 #Definindo a XP de herói
if XP >= 0 and XP <= 999:
    print("O herói está no nível de ferro.")
elif XP >= 1000 and XP <= 2999:
    print("O herói está no nível de bronze.")
elif XP >= 3000 and XP <= 6999:
    print("O herói está no nível de prata.")
elif XP >= 7000 and XP <= 10999:
    print("O herói está no nível de ouro.")
elif XP >= 11000 and XP <= 14999:
    print("O herói está no nível de platina.")
elif XP >= 15000 and XP <= 19999:
    print("O herói está no nível de ascensional.")
else:
    print("O herói está no nível de immortal.")
#Considerando o XP do herói, isso significa que ele ganhou muita experiência, mas ainda tem muito a aprender e conquistar. Ele é um guerreiro h
print(f'Com isso, o bravo guerreiro {heroi} tem {XP} pontos de experiência.')
print(f'Ganhava, mas saia sangrando, disse {heroi}.')
print("E aí, vai encarar? Ele disse que consegue derrotar um lobo.")