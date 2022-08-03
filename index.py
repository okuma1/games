import inquirer
from forca import forca

jogo = 0

print("-"*50 + "\n" "MENU DE JOGOS" + "\n" + "-"*50)

questions = [
    inquirer.List('size',
        message="Qual jogo você quer jogar?",
        choices=['Forca', 'Palavra secreta', 'Numero secreto'],
    ),
]

resposta = inquirer.prompt(questions)

if (resposta['size'] == 'Forca'):
    forca()

def restart():
    global jogo

    while (jogo != 1):
        i = str(input("Deseja jogar?(s/n): "))

        if i == 'n':
            jogo = 1
            print("Até a próxima!")


