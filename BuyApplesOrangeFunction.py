def welcomeUser():
    nickname_ = input("Good day! Please enter your nickname: ")
    return nickname_

def display(nickname_):
    print(f"Good day {nickname_}!. Please enjoy your shopping.")

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

def displayAmount(totalAmount):
    print(f"The total amount is {totalAmount}.")

def continueTransaction():
    answer = input("Do you want to continue your transaction? ").upper()
    if answer == "YES":
        print("The parcel is on your way please prepare your cash. Thank you and come again!")
    elif answer == "NO":
        print("Thank you for your time please come again!")
    return answer

nickname = welcomeUser()
display(nickname)
costOfApple, costOfOrange, totalAmount = askForAppleOrange()
displayAmount(totalAmount)
continueTransaction()