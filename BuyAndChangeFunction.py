def welcomeUser():
    nickname_ = input("Good day! Please enter your nickname: ")
    return nickname_

def display(nickname_):
    print(f"Good day {nickname_}!. Please enjoy your shopping.")

nickname = welcomeUser()
display(nickname)

def askMoneyAndApple():
    money = input("How much money do you have on hand?: ")
    priceOfApple = input("What is the current cost of an apple?: ")
    return money, priceOfApple

money, priceOfApple = askMoneyAndApple()