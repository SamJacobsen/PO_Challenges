p1 = 'Player 1'
p2 = 'Player 2'

matrix = [[0, p2, p1], [p1, 0, p2], [p2, p1, 0]]

print('Welcome to rock paper scissors')
print('Rock = 0, paper = 1, scissors = 2')


def take_input(prompt):
    while True:
        try:
            i = int(input(prompt))
            if i in range(0, 3):
                return i
        except ValueError:
            print('Cloud not parse whole number')
        print('Invalid input, try again')


p1_input = take_input('Player1: ')
p2_input = take_input('Player2: ')

winner = matrix[p1_input][p2_input]
if winner == 0:
    print('The game was a tie')
else:
    print(f'{winner} wins')
