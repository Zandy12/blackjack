import random

def game_display():
    print('                     ')
    print('~*%*~*%*~*%*~*%*~*%*~*%*~*%*~*%*~*%*~*%*')
    print('                                  Deck:  ')
    print('   [',dealer[0],'] [',dealer[1],'] [',dealer[2],'] [',dealer[3],'] [',dealer[4],']',' [ X ]   ')
    print('           D E A L E R         ')
    print('                     ')
    print('                     ')
    print('              Y O U            ')
    print('   [',you[0],'] [',you[1],'] [',you[2],'] [',you[3],'] [',you[4],']') 
    print('                     ')
    print('Money:',money,'                     Bet:',bet)
    print('~*%*~*%*~*%*~*%*~*%*~*%~*%*~*%*~*%*~*%*')
    print('                     ')

def text():
    global dealer_money
    global you_money
    global money
    global bet
    answer = False

    while answer == False:
        try:
            answer = int(input('How much would you like to bet?: '))
            if answer > money:
                print("You don't have enough money. Please type in a proper amound that you would like to bet.")
                text()
            else:
                dealer_money += answer
                you_money += answer
                money -= answer
                bet = you_money + dealer_money
        except:
            print('Please write the amount that you would like to bet.')

def shuffle():
    print('*The dealer puts in the same amount. He then shuffles the cards, draws 2 for him and passes 2 to you.*')
    you[0] = random.choice(deck)
    you[1] = random.choice(deck)
    dealer[0] = random.choice(deck)
    dealer[1] = ('X')
    if you[0] + you[1] + you[2] == 21:
        winning_statement()
    elif you[0] + you[1] + you[2] > 21:
        losing_statement()

def options_0():
    global bet
    global money
    global wager_bet
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? Split(only if you have 2 identical cards)? Insurance? or Surrender? ').lower()
     
        if response == ('hit'):
            you[2] = random.choice(deck)
            dealer[1] = random.choice(deck)
            dealer[2] = ('X')
            if you[0] + you[1] + you[2] == 21:
                winning_statement()
            elif you[0] + you[1] + you[2] > 21:
                losing_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_1()
        if response == ('stand'):
            dealer[1] = random.choice(deck)
            dealer[2] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_1()
        if response == ('double-down'):
            bet = you_money*2 + dealer_money*2
            money = money - dealer_money
            you[2] = random.choice(deck)
            dealer[1] = random.choice(deck)
            dealer[2] = ('X')
            if you[0] + you[1] + you[2] == 21:
                winning_statement()
            elif you[0] + you[1] + you[2] > 21:
                losing_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_1_dd()
        if response == ('split'):
            if bet == you_money + dealer_money and you[0] == you[1]:
                bet = (you_money*2) + (dealer_money*2)
                money = money - dealer_money
                you[2] = random.choice(deck)
                you[3] = random.choice(deck)
                dealer[1] = random.choice(deck)
                dealer[2] = ('X')    
                game_display()
                options_1_splitted()
            else:
                print('*You cannot split unless you have two of the same identical cards. Please choose another option.*')
                options_0()
        if response == ('insurance') and dealer[0] == (1): 
            wager_bet = you_money/2
            money -= wager_bet
            bet += wager_bet*2
            dealer[1] = random.choice(deck)
            dealer[2] = ('X')
            you[2] = random.choice(deck)
            if dealer[0] + dealer[1] == 21:
                winning_insurance_statement()
            elif dealer[0] + dealer[1] != 21:
                game_display()
                print('*You have lost the insurance bet to the dealer. He takes the wager bet with him.*') 
                bet -= wager_bet*2
                options_1()
        elif response == ('insurance') and dealer[0] == (11): 
            wager_bet = you_money/2
            money -= wager_bet
            bet += wager_bet*2
            dealer[1] = random.choice(deck)
            dealer[2] = ('X')
            you[2] = random.choice(deck)
            if dealer[0] + dealer[1] == 21:
                winning_insurance_statement()
            elif dealer[0] + dealer[1] != 21:
                game_display()
                print('*You have lost the insurance bet to the dealer. He takes the wager bet with him.*') 
                bet -= wager_bet*2
                options_1()
        elif response == ('insurance') and dealer[0] != (1):
            print("You can only pick insurance if the dealer's first card is an Ace. Please choose another option.")
            options_0()
        elif response == ('insurance') and dealer[0] != (11):
            print("You can only pick insurance if the dealer's first card is an Ace. Please choose another option.")
            options_0()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_0()

def options_1_splitted():
    global bet
    global money
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? or Surrender? ').lower()
     
        if response == ('hit'):
            you[4] = random.choice(deck)
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if you[0] + you[2] + you[4] == 21 or you[1] + you[3] + you[4] == 21:
                winning_statement()
            elif you[0] + you[2] + you[4] > 21 and you[1] + you[3] + you[4] > 21:
                losing_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_2_splitted()
        if response == ('stand'):
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_2-splitted()
        if response == ('double-down'):
            bet = (you_money*2)*3/2 + (dealer_money*2)*3/2
            money -= you_money
            you[4] = random.choice(deck)
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if you[0] + you[2] + you[4] == 21 or you[1] + you[3] + you[4] == 21:
                winning_statement()
            elif you[0] + you[2] + you[4] > 21 and you[1] + you[3] + you[4] > 21:
                losing_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_2_split_dd()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_1_splitted()

def options_2_splitted():
    global bet
    global money
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Stand? Double-Down? or Surrender? ').lower()
     
        if response == ('stand'):
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            if you[0] == you[1]:
                if you[0] + you[2] + you[4] == 21 or you[1] + you[3] + you[4] == 21:
                    winning_statement()
                elif you[0] + you[2] + you[4] > 21 and you[1] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[1] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[0] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
        if response == ('double-down'):
            bet = (you_money*2)*3/2 + (dealer_money*2)*3/2
            money -= you_money
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            if you[0] == you[1]:
                if you[0] + you[2] + you[4] == 21 or you[1] + you[3] + you[4] == 21:
                    winning_statement()
                elif you[0] + you[2] + you[4] > 21 and you[1] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[1] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[0] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_2_splitted()

def options_2_split_dd():
    global bet
    global money
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Stand? Double-Down? or Surrender? ').lower()
     
        if response == ('stand'):
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            if you[0] == you[1]:
                if you[0] + you[2] + you[4] == 21 or you[1] + you[3] + you[4] == 21:
                    winning_statement()
                elif you[0] + you[2] + you[4] > 21 and you[1] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[1] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[0] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
        if response == ('double-down'):
            bet = (you_money*3)*4/3 + (dealer_money*3)*4/3
            money -= you_money
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            if you[0] == you[1]:
                if you[0] + you[2] + you[4] == 21 or you[1] + you[3] + you[4] == 21:
                    winning_statement()
                elif you[0] + you[2] + you[4] > 21 and you[1] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] < dealer_hand_amount and you[1] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[2] + you[4] > dealer_hand_amount and you[1] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[1] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
            if you[0] == you[2]:
                if you[0] + you[1] + you[4] == 21 or you[2] + you[3] + you[4] == 21:
                    winning_statement()
                if you[0] + you[1] + you[4] > 21 and you[2] + you[3] + you[4] > 21:
                    losing_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    losing_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] < dealer_hand_amount and you[2] + you[3] + you[4] > dealer_hand_amount:
                    winning_statement()
                elif you[0] + you[1] + you[4] > dealer_hand_amount and you[2] + you[3] + you[4] < dealer_hand_amount:
                    winning_statement()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_2_split_dd()

def options_1():
    global bet
    global money
    global wager_bet
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? Split(only if you have 2 identical cards)? or Surrender? ').lower()
     
        if response == ('hit'):
            you[3] = random.choice(deck)
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if you[0] + you[1] + you[2] + you[3] == 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] > 21:
                losing_statement()
            else:
                game_display()
                options_2()
        if response == ('stand'):
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_2()
        if response == ('double-down'):
            bet = you_money*2 + dealer_money*2
            money = money - dealer_money - wager_bet
            you[3] = random.choice(deck)
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if you[0] + you[1] + you[2] + you[3] == 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] > 21:
                losing_statement()
            else:
                game_display()
                options_2_dd()
        if response == ('split'):
            if bet == you_money + dealer_money and you[0] == you[1] or you[1] == you[2] or you[0] == you[2]:
                bet = (you_money*2) + (dealer_money*2)
                money = money - dealer_money
                if you[0] == you[1]:
                    you[2] = random.choice(deck)
                    you[3] = random.choice(deck)
                if you[1] == you[2]:
                    you[3] = random.choice(deck)
                    you[4] = random.choice(deck)
                if you[0] == you[2]:
                    you[3] = random.choice(deck)
                    you[4] = random.choice(deck)
                dealer[2] = random.choice(deck)
                dealer[3] = ('X')
                game_display()
                options_2_splitted()
            else:
                print('*You cannot split unless you have two of the same identical cards. Please choose another option.*')
                options_1()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_1()

def options_2():
    global bet
    global money
    global wager_bet
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? or Surrender? ').lower()
     
        if response == ('hit'):
            you[4] = random.choice(deck)
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('stand'):
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('double-down'):
            bet = you_money*2 + dealer_money*2
            money = money - dealer_money - wager_bet
            you[4] = random.choice(deck)
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_2()

def options_1_dd():
    global bet
    global money
    global wager_bet
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? Split(only if you have 2 identical cards)? or Surrender? ').lower()
     
        if response == ('hit'):
            you[3] = random.choice(deck)
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if you[0] + you[1] + you[2] + you[3] == 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] > 21:
                losing_statement()
            else:
                game_display()
                options_2_dd()
        if response == ('stand'):
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            else:
                game_display()
                options_2_dd()
        if response == ('double-down'):
            bet = (you_money*2)*3/2 + (dealer_money*2)*3/2
            money = money - dealer_money - wager_bet
            you[3] = random.choice(deck)
            dealer[2] = random.choice(deck)
            dealer[3] = ('X')
            if you[0] + you[1] + you[2] + you[3] == 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] > 21:
                losing_statement()
            else:
                game_display()
                options_2_2dd()
        if response == ('split'):
            if bet == you_money + dealer_money and you[0] == you[1] or you[1] == you[2] or you[0] == you[2]:
                bet = (you_money*2)*3/2 + (dealer_money*2)*3/2
                money = money - dealer_money - wager_bet
                you[3] = random.choice(deck)
                you[4] = random.choice(deck)
                dealer[2] = random.choice(deck)
                dealer[3] = ('X')
                game_display()
                options_2_split_dd()
            else:
                print('*You cannot split unless you have two of the same identical cards. Please choose another option.*')
                options_1_dd()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_1_dd()

def options_2_dd():
    global bet
    global money
    global wager_bet
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? or Surrender? ').lower()
     
        if response == ('hit'):
            you[4] = random.choice(deck)
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('stand'):
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif dealer_hand_amount > you[0] + you[1] + you[2] + you[3] + you[4]:
                losing_statement()
            elif dealer_hand_amount < you[0] + you[1] + you[2] + you[3] + you[4]:
                winning_statement()
        if response == ('double-down'):
            bet = (you_money*2)*3/2 + (dealer_money*2)*3/2
            money = money - dealer_money - wager_bet
            you[4] = random.choice(deck)
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[s2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_2_dd()

def options_2_2dd():
    global bet
    global money
    global dealer_hand_amount
    response = False

    while response == False:

        response = input('Please type in what would you like to do? Hit? Stand? Double-Down? or Surrender? ').lower()
     
        if response == ('hit'):
            you[4] = random.choice(deck)
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[s2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('stand'):
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[s2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('double-down'):
            bet = (you_money*3)*4/3 + (dealer_money*3)*4/3
            money -= you_money
            you[4] = random.choice(deck)
            dealer[3] = random.choice(deck)
            dealer[4] = ('X')
            if you[0] + you[1] + you[2] + you[3] + you[4] == 21:
                winning_statement()
            elif dealer_hand_amount == 21:
                losing_statement()
            elif dealer_hand_amount > 21:
                winning_statement()
            elif you[0] + you[1] + you[s2] + you[3] + you[4] > 21:
                losing_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] > dealer_hand_amount:
                winning_statement()
            elif you[0] + you[1] + you[2] + you[3] + you[4] < dealer_hand_amount:
                losing_statement()
        if response == ('surrender'):
            surrender_statement()
##        else:
##            print('Please enter in a proper response.')
##            options_2_2dd()

def winning_statement():
    global bet
    global you
    global money
    global dealer
    global you_money
    global dealer_money
    the_dealers_fate = False

    while the_dealers_fate == False:
        game_display()
        the_dealers_fate = input('*You won! You have taken all the money you have bet against the dealer. Would you like to play against him again?* [Y/N]: ').lower() 
        if the_dealers_fate == ('y'):
            money += bet
            bet -= bet
            you_money = 0
            dealer_money = 0
            you = [0,0,0,0,0]
            dealer = [0,0,0,0,0]
        elif the_dealers_fate == ('n'):
            quit()
        else:
            print('Please type in Y(y) or N(n) to request what you would like to do. ("Y" to play again or "N" to quit the game)')
            winning_statement()

def losing_statement():
    global bet
    global you
    global money 
    global dealer
    global you_money
    global dealer_money
    next_step = False

    while next_step == False:
        game_display()
        next_step = input('*You have lost this round to the dealer. He takes all the money with him. Would you like to play against him again?* [Y/N]: ').lower() 
        if next_step == ('y'):
            bet -= bet
            you_money = 0
            dealer_money = 0
            you = [0,0,0,0,0]
            dealer = [0,0,0,0,0]
        elif next_step == ('n'):
            quit()
        else:
            print('Please type in Y(y) or N(n) to request what you would like to do. ("Y" to play again or "N" to quit the game)')
            losing_statement()

def surrender_statement():
    global bet
    global you
    global money
    global dealer
    global you_money
    global dealer_money
    next_step = False

    while next_step == False:
        game_display()
        next_step = input('*You have surrendered this round to the dealer. He takes most of the money with him but you got half of your bet back. Would you like to play against him again?* [Y/N]: ').lower() 
        if next_step == ('y'):
            money += bet*(1/4)
            bet -= bet
            you_money = 0
            dealer_money = 0
            you = [0,0,0,0,0]
            dealer = [0,0,0,0,0]
        elif next_step == ('n'):
            quit()
        else:
            print('Please type in Y(y) or N(n) to request what you would like to do. ("Y" to play again or "N" to quit the game)')
            surrender_statement()

def winning_insurance_statement():
    next_step = False

    while next_step == False:
        game_display()
        next_step = input('*You have lost this round to the dealer. However you have won the wager bet. Would you like to play against him again?* [Y/N]: ').lower() 
        if next_step == ('y'):
            bet -= bet
            money += wager_bet*2
            you_money = 0
            dealer_money = 0
            you = [0,0,0,0,0]
            dealer = [0,0,0,0,0]
        elif next_step == ('n'):
            quit()
        else:
            print('Please type in Y(y) or N(n) to request what you would like to do. ("Y" to play again or "N" to quit the game)')
            winning_insurance_statement()


print('Welcome to Blackjack!')

while True:
    J = 10
    Q = 10
    K = 10
    A1 = 1
    A = 11
    bet = 0
    wager_bet = 0
    you_money = 0
    dealer_money = 0
    money = 2000
    you = [0,0,0,0,0]
    dealer = [0,0,0,0,0]
    deck = [2,3,4,5,6,7,8,9,10,J,Q,K,A1,A]
    dealer_hand_amount = dealer[0] + dealer[1] + dealer[2] + dealer[3] + dealer[4]
    

    game_on = True

    while game_on:

        game_display()
        text()      
        shuffle()
        game_display()
        options_0()
