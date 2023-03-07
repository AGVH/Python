import random

print('Paper Scissors Rock')
options = ('rock', 'paper', 'scissors')
rounds = 1
computer_wins = 0
user_wins = 0

while True:
    
    print('*' * 15 )
    print('ROUND ', rounds)
    print('*' * 15 )
    
    user_choice = input('paper, scissors, rock => ').lower()

    rounds += 1
    
    if not user_choice in options:
        print('\!/Invalid choice\!/')
        continue 

    print('User choice => ', user_choice)
    print('vs')

    computer_choice = random.choice(options)

    print('Computer choice => ', computer_choice)

    if user_choice == computer_choice:
        print('Draw!')
        
    elif user_choice == 'rock':
        if computer_choice == 'tijera':
            print('Rock is better than scissors')
            print('=>USER wins')
            user_wins += 1
            
        else:
            print("Paper is better than rock")
            print('=>COMPUTER wins')
            computer_wins += 1
            
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('Paper is better than rock')
            print('=>USER wins')
            user_wins += 1
        else:
            print('Scissors is better than paper')
            print('=>COMPUTER wins')
            computer_wins += 1
            
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('Scissors is better than paper')
            print('=>USER wins')
            user_wins += 1
        else:
            print('Rock is better than scissors')
            print('=>COMPUTER wins')
            computer_wins += 1
            
    if computer_wins ==2:       
        print('+++Computer is the champion!+++')
        break
    
    if user_wins == 2:
        print('+++User is the champion!+++')
    
    