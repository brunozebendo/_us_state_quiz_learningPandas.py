"""a ideia do código é criar um jogo de advinhação, onde o jogador digita o nome do estado e ele vai para o mapa
no local correspondente, no entanto, não migrou para o meu PY charm nem a figura, nem o tabela"""

import turtle
import pandas
'''importado os dois módulos necessários, o turtle que já tem funções próprias como já foi ensinado'''
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
'''acima foi criado o código para importar a imagem do mapa do estados unidos como fundo'''

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
'''aqui a variável data recebe a leitura de uma planilha com 3 informações, o estado e a localização x e y, que são o
local do pixel na tela, depois transforma isso em uma lista e cria-se um dicionário vazio para as tentativas de
acerto do jogador'''

while len(guessed_states) < 50:
    '''o código fica dentro de um while para que feche caso o jogador erre mais de 50 vezes.'''
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    '''o código acima cria a caixa de título, a primeira parte já passa o comprimento da lista de tentativas,
     a de baixo é a da caixa onde será escrita a resposta (prompt). Reparar como a função len já poupou um código
     para ir diminuindo a quantidade de tentativas'''
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    '''o código acima serve para quando o jogador clique em exit para sair o jogo já tenha criado um dicionário com
    os estados que o jogador não acertou, para isso ele compara se o estado da advinhação consta na lista de todos
    os estados e vai retirando-os conforme o jogador for acertando. No final ele cria uma nova tabela (DataFrame) e
    converte em um arquivo csv'''
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    '''aqui o código serve para quando o jogador acerta, nesse caso o item é acrescentado no dicionário guessed_states
    alterando o seu comprimento (len), os outros 3 códigos são para criar e esconder a "tartaruga" e o risco da caneta,
     já as próximas linhas servem para levar o nome do estado para a localização x,y determinada no dicionário e lá
      escrevê-la'''


