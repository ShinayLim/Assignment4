def welcomeUser():
    nickname_ = input("Good day! Please enter your nickname: ")
    return nickname_

def display(nickname_):
    print(f"Good day {nickname_}!. Please enjoy your shopping.")

nickname = welcomeUser()
display(nickname)

def askForAppleOrange():
    global applePrice
    applePrice = 20
    global applesYouWantToBuy
    applesYouWantToBuy = int(input("How many apple/s you want to add in your cart?: "))
    costOfApple = int(applesYouWantToBuy) * applePrice
    global orangePrice
    orangePrice = 25
    global orangesYouWantToBuy
    orangesYouWantToBuy = input("How many orange/s you want to add in your cart?: ")
    costOfOrange = int(orangesYouWantToBuy) * orangePrice
    global totalAmount
    totalAmount = costOfApple + costOfOrange
    return costOfApple, costOfOrange, totalAmount

costOfApple, costOfOrange, totalAmount = askForAppleOrange()