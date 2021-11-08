def welcomeUser():
    nickname_ = input("Good day! Please enter your nickname: ")
    return nickname_

def display(nickname_):
    print(f"Good day {nickname_}!. Please enjoy your shopping.")

nickname = welcomeUser()
display(nickname)

def askMoneyAndApple():
    global money
    money = int(input("How much money do you have on hand?: "))
    global priceOfApple
    priceOfApple = int(input("What is the current cost of an apple?: "))
    return money, priceOfApple

def applesAndChange():
    global numOfApple_
    numOfApple_ = money//priceOfApple
    global change_
    change_ = money%priceOfApple
    return numOfApple_, change_

money, priceOfApple = askMoneyAndApple()
numOfApple_, change_ = applesAndChange()
