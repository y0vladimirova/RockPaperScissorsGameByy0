import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
moves = [rock, paper, scissors]

player_score = 0
computer_score = 0
draws = 0

while True:

    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")
        continue

    computer_random_number = random.randint(1,3)

    computer_move = ''

    if computer_random_number == 1:
        computer_move = 'Rock'
    elif computer_random_number == 2:
        computer_move = 'Paper'
    elif computer_random_number == 3:
        computer_move = 'Scissors'

    print(f'The computer chose {computer_move}.')

    if(player_move == rock and computer_move == 'Scissors') or\
        (player_move == paper and computer_move == 'Rock') or \
        (player_move == scissors and computer_move == paper):
     player_score += 1
     print("You win!")
    elif player_move == computer_move:
        draws +=1
        print("Draw!")
    else:
        computer_score += 1
        print("You lose!")


    print(f'Score -> You: {player_score} | Computer: {computer_score}')
    again = input(f'Play again? [y/n]: ').lower().strip()
    if again != 'y':
        print('Thanks for playing')
        break

