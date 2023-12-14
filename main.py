import random

def computerChoice():
    choices = ['R','P','S']
    return random.choice(choices)

wins = 0
loses = 0
ties = 0
choices = ['R','P','S']
continueToPlay = True

while continueToPlay:
    
    computerChoice = random.choice(choices)
    
    print('R - Rock')
    print('P - Paper')
    print('S - Scissors')
    print()
    playerChoice = input('Your choice: ')
    print()
    
    if playerChoice == 'R':
        if computerChoice == 'R':
            print("The computer chose rock. You chose rock. It's a tie.")
            print()
            ties += 1
        if computerChoice == 'P':
            print("The computer chose paper. You chose rock. You lost!")
            print()
            loses += 1
        if computerChoice == 'S':
            print("The computer chose scissors. You chose rock. You won!")
            print()
            wins += 1
    if playerChoice == 'P':
        if computerChoice == 'R':
            print("The computer chose rock. You chose paper. You won!")
            print()
            wins += 1
        if computerChoice == 'P':
            print("The computer chose paper. You chose paper. It's a tie.")
            print()
            ties += 1
        if computerChoice == 'S':
            print("The computer chose scissors. You chose paper. You lost!")
            print()
            loses += 1
    if playerChoice == 'S':
        if computerChoice == 'R':
            print("The computer chose rock. You chose scissors. You lost!")
            print()
            loses += 1
        if computerChoice == 'P':
            print("The computer chose paper. You chose scissors. You won!")
            print()
            wins += 1
        if computerChoice == 'S':
            print("The computer chose scissors. You chose scissors. It's a tie")
            print()
            ties += 1
    
    choiceToPlay = input('Would you like to play again? - Y or N: ')
    print()
    if choiceToPlay.upper() == 'N':
        continueToPlay = False


print()
print(f'Computer Wins: {loses}')
print(f'Ties: {ties}')
print(f'Your wins: {wins}')


