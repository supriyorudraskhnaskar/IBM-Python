Finalcart= []
Finalquantity= []
Finalamount= []
Product = ["1: Shampoo", "2: Toothpaste", "3: Soap"]
CategoryShampoo = {"1: Loreal": 65, "2: Pantene": 60, "3: Head & Shoulder": 75}
CategoryToothpaste = {"1: Colgate": 45, "2: OralB": 75, "3: Close Up": 70}
CategorySoap = {"1: Dove": 25, "2: Pears": 20, "3: Nivea": 30}
while True:
    WelcomeTxt= ('''**********Welcome to NaskarMart**********
    Type 1. Show Items
    Type 2. Go to cart
    Type 3. Exit\n''')
    print(WelcomeTxt)
    UserInput= int(input("Please select your response: " ))
    if UserInput == 1:
        for a in Product:
            print(a)
    elif UserInput == 2:
        print(Finalcart, Finalquantity)
        userinputgocart= input("Press 'Y' to continue or press any key to end: ").lower()
        if userinputgocart == 'y':
            continue
        else:
            print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            print("Grand Total: ", sum(Finalamount))
            break
    elif UserInput == 3:
        recheck= input("Are you sure to quit? Press 'Y' to quit else any key to continue: ").lower()
        if recheck == 'y':
            quit()
        else:
            continue
    UserInputR= int(input("\nPlease select your response: " ))
    if UserInputR == 1:
        for x, y in CategoryShampoo.items():
            print(str(x) + ': ' + str(y))
        userinputshampoo = int(input("\nSelect your product from above Product Number: "))
        if userinputshampoo == 1:
            quantity = int(input("Quantity you want to purchase: "))
            cost = CategoryShampoo.get("1: Loreal")
            Finalamount.append(cost * quantity)
            Finalcart.append("Loreal")
            Finalquantity.append(quantity)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, quantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, quantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
        elif userinputshampoo == 2:
            quantity = int(input("Quantity you want to purchase: "))
            cost = CategoryShampoo.get("2: Pantene")
            Finalamount.append(cost * quantity)
            Finalcart.append("Pantene")
            Finalquantity.append(quantity)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
        elif userinputshampoo == 3:
            quantity = int(input("Quantity you want to purchase: "))
            cost = CategoryShampoo.get("3: Head & Shoulder")
            Finalamount.append(cost * quantity)
            Finalcart.append("Head & Shoulder")
            Finalquantity.append(quantity)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
    elif UserInputR == 2:
        for x, y in CategoryToothpaste.items():
            print(str(x) + ': ' + str(y))
        userinputtoothpaste = int(input("\nSelect your product from above Product Number: "))
        if userinputtoothpaste == 1:
            quantity1 = int(input("Quantity you want to purchase: "))
            cost1 = CategoryToothpaste.get("1: Colgate")
            Finalamount.append(cost1 * quantity1)
            Finalcart.append("Colgate")
            Finalquantity.append(quantity1)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
        elif userinputtoothpaste == 2:
            quantity1 = int(input("Quantity you want to purchase: "))
            cost1 = CategoryToothpaste.get("2: OralB")
            Finalamount.append(cost1 * quantity1)
            Finalcart.append("OralB")
            Finalquantity.append(quantity1)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
        elif userinputtoothpaste == 3:
            quantity1 = int(input("Quantity you want to purchase: "))
            cost1 = CategoryToothpaste.get("3: Close Up")
            Finalamount.append(cost1 * quantity1)
            Finalcart.append("Close Up")
            Finalquantity.append(quantity1)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
    elif UserInputR == 3:
        for x, y in CategorySoap.items():
            print(str(x) + ': ' + str(y))
        userinputsoap = int(input("\nSelect your product from above Product Number: "))
        if userinputsoap == 1:
            quantity2 = int(input("Quantity you want to purchase: "))
            cost2 = CategorySoap.get("1: Dove")
            Finalamount.append(cost2 * quantity2)
            Finalcart.append("Dove")
            Finalquantity.append(quantity2)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
        elif userinputsoap == 2:
            quantity2 = int(input("Quantity you want to purchase: "))
            cost2 = CategorySoap.get("2: Pears")
            Finalamount.append(cost2 * quantity2)
            Finalcart.append("Pears")
            Finalquantity.append(quantity2)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue
        elif userinputsoap == 3:
            quantity2 = int(input("Quantity you want to purchase: "))
            cost2 = CategorySoap.get("3: Nivea")
            Finalamount.append(cost2 * quantity2)
            Finalcart.append("Nivea")
            Finalquantity.append(quantity2)
            print("This is your Current Cart: {}\nThis is your Current Quantity: {}\nThis is your Current Amount: {}".format(Finalcart, Finalquantity, Finalamount))
            continuationInput = input("\nWould you like to purchase another item?\nPress any key for yes or 'n' for no: ")
            if continuationInput == 'n':
                print("This is your Final Cart: {}\nThis is your Final Quantity: {}\nThis is your Final Amount: {}".format(Finalcart, Finalquantity, Finalamount))
                print("Grand Total: ", sum(Finalamount))
                break
            else:
                continue