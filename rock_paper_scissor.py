import random
import tkinter as tk

stats = []

def getWinner(call):

    if random.random() <= (1/3):
        throw = 'Rock'
    elif (1/3) < random.random() <= (2/3):
        throw = 'Scissors'
    else:
        throw = 'Paper'

    if (throw == 'Rock' and call == 'Paper') or (throw == 'Paper' and call == 'Scissors') or (throw == 'Scissors' and call == 'Rock'):
        stats.append('W')
        result = "You Won!!!"
    elif throw == call:
        stats.append('D')
        result = "It Is A Draw!!!"
    else:
        stats.append('L')
        result = 'You Lost!!!'

    global output 
    output.config(text = 'Computer Threw : ' + throw + '\n' + result)


def sPass():
    getWinner('Scissors')

def rPass():
    getWinner('Rock')

def pPass():
    getWinner('Paper')


window = tk.Tk()

scissors = tk.Button(window, text='Scissors', bg='#ff9999', padx=10, pady=5, command=sPass, width=20)
rock = tk.Button(window, text='Rock', bg='#80ff80', padx=10, pady=5, command=rPass, width=20)
paper = tk.Button(window, text='Paper', bg='#3399ff', padx=10, pady=5, command=rPass, width=20)
output = tk.Label(window, width=20, fg='red', text="What's Your Call?")

scissors.pack(side='left')
rock.pack(side='left')
paper.pack(side='left')
output.pack(side='right')
window.mainloop()

for i in stats:
    print(i, end=' ')

if stats.count('L') > stats.count('W'):
    result = 'You have Lost the series.'
elif stats.count('L') == stats.count('W'):
    result = 'Series has ended in a Draw.'
else:
    result = 'You have Won the series.'

print('\n',result,'\n', end='')
