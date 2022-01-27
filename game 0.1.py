from random import randint as ri

def cash():
    cash = 
print("Welcome to the game")
cash = 0
def game():
    print("Chose thing to do:")
    print("Work| casino | Bank | Stock market")
    choice_1 = input()
    if choice_1 == "Work":
        print("You work hard and you gain 100$")
        cash = cash + 100
        game()
    elif choice_1 == "Casino":
        print("How much do you want to play for?")
        choice_2 = int(input())
        if choice_2 > cash:
            print("You dont have that much money")
            game()
        elif choice_2 > cash:
            fate = ri(1,1000)
            if fate < 2:
                print("You won jackpot")
                cash = choice_2 * 5
                ()
            elif 2 < fate <  400:
                print("You won")
                
                cash = choice_2 * 2
            elif 400 < fate < 900:
                cash = cash - choice_2
            elif 900 < fate < 1000:
                print("You won mini jackpot")
                cash = choice_2 * 3
    elif choice_1 == "Bank":
        print("Bank acount: ",cash,"$")
    elif choice_1 == "Stock market":
        print("Welcome to stock market")
        print("Your stocks are worth x right now")
        print("How many shares you want to buy")
        net_1 = ri(0,8)
        net_2 = ri(0,8)
        net_3 = ri(0,8)
        net_4 = ri(0,8)
        if 3 < net_1 < 5:
            net_1 = 2
            s = True
        elif 0 < net_1 < 3:
            net_1 = 4
            s = True
        elif 5 < net_1 < 7:
            net_1 = 2
            s = False
        elif 7 < net_1 < 10:
            net_1 = 4
            s = False

        if 3 < net_2 < 5:
            net_2 = 2
            s = True
        elif 0 < net_2 < 3:
            net_2 = 4
            s = True
        elif 5 < net_2 < 7:
            net_2 = 2
            s = False
        elif 7 < net_2 < 10:
            net_2 = 4
            s = False

        if 3 < net_3 < 5:
            net_3 = 2
            s = True
        elif 0 < net_2 < 3:
            net_3 = 4
            s = True
        elif 5 < net_2 < 7:
            net_3 = 2
            s = False
        elif 7 < net_2 < 10:
            net_3 = 4
            s = False

        if 3 < net_4 < 5:
            net_4 = 2
            s = True
        elif 0 < net_4 < 3:
            net_4 = 4
            s = True
        elif 5 < net_4 < 7:
            net_4 = 2
            s = False
        elif 7 < net_4 < 10:
            net_4 = 4
            s = False
        if s == True:
            
            print("| Company 1| +", net_1,"%")
        elif s == False:
            print("| Company 1| -", net_1,"%")
        stock = ri(0,1)
        if stock == 0:
            stock_2 = ri(0,1)
            if stock_2 == 0:
                print("The value of your shares has dropped by 2%")
                cash = cash + 0,96 * stock_cash
cash = 0

game()
def coś():
    print("")
