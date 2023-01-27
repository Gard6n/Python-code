
user1P = 0
user2P = 0

while True:
    print()
    #print()
    #print('Press 2 at anytime too see player wins')
    print()
    print()
    player1 = input('Player 1 Enter Rock,Paper,Scissors ')
    print('=====================================')
    print()
    player2 = input('Player 2 Enter Rock,Paper,Scissors ')
    print('=====================================')
    print()

    if player1.lower() == 'rock' and player2.lower() == 'paper':
        print('-------------')
        print('Player2 wins')
        user2P =+1

    if player1.lower() == 'paper' and player2.lower() == 'scissors':
        print('-------------')
        print('Player2 wins')
        user2P=+1

    if player1.lower() == 'scissors' and player2.lower() == 'rock':
        print('-------------')
        print('Player2 wins')
        user2P=+1

    if player2.lower() == 'rock' and player1.lower() == 'paper':
        print('-------------')
        print('Player1 wins')
        user1P =+1

    if player2.lower() == 'paper' and player1.lower() == 'scissors':
        print('-------------')
        print('Player1 wins')
        user1P=+1

    if player2.lower() == 'scissors' and player1.lower() == 'rock':
        print('-------------')
        print('Player1 wins')
        user1P=+1


    if player1 == '2' or player2 == '2':
        print()
        print()
        print('------------------------------------------------')
        print(f'Player1 has {user1P} wins and Player2 has {user2P} wins ')
        print('------------------------------------------------')
        print()
