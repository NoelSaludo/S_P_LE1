userDB = {}
isLogin = False
currUser = ''
adLogIn = False
gameLib = {"Donkey Kong":{"cost":9.99, "copies": 10},"Tetris":{"cost":0.99, "copies": 15},"Super Mario Bros":{"cost":4.99, "copies": 15},}

def LogIn():
    while True:
        try:
            usnm = input("Enter username: ")
            if not usnm:
                return
            passw = input("Enter password: ")
            if not userDB[usnm]:
                print("User not found")
                continue
            if userDB[usnm]["pass"] != passw:
                print("Wrong Password try again")
                continue
            global isLogin
            isLogin = True
            global currUser
            currUser = usnm
        except ValueError as e:
            print(e)
        break
    pass
def RegisterUser():
    while True:
        try:
            newusnm = input("Enter new Username: ")
            if not newusnm:
                return
            newpass = input("Enter new Password: ")
            if newusnm in userDB:
                print("User Already in System")
                continue
            userDB[newusnm] = {"pass": newpass, "balance": 10.0, "points":0, "rentedGame": []}
        except ValueError as e:
            print(e)
        break
def DisplayGameLib():
    for game, attr in gameLib.items():
        print(f"{game}\n\t>Cost: {attr["cost"]}\n\t>Copies: {attr["copies"]}")
def RentGame():
    DisplayGameLib()
    while True:
        try:
            gameList = list(gameLib)
            c = int(input(f"Enter your choice from 1 to {len(gameList)}"))
            if not c:
                return
            c -= 1
            game = gameLib[gameList[c]]
            if game["cost"] > userDB[currUser]["balance"]:
                print("Insufficient Balance")
                continue
            if game["copies"] <= 0:
                print("NO available copies")
                continue
            userDB[currUser]["rentedGame"].append(gameList[c])
            userDB[currUser]["balance"] -= game["cost"]
            userDB[currUser]["points"] += game["cost"] // 5
            gameLib[gameList[c]]["copies"] -= 1
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        break
def DisplayRented():
    if not userDB[currUser]["rentedGame"]:
        print("Not Rented any games yet")
    for i, game, in enumerate(userDB[currUser]["rentedGame"]):
        print(f"{i+1}. {game}")
def ReturnGame():
    DisplayRented()
    while True:
        try:
            i = int(input(f"Enter Choice from {len(userDB[currUser]["rentedGame"])}"))
            if not i:
                return
            if i <= 0 or i > len(userDB[currUser]["rentedGame"]):
                print("Enter a proper input")
                continue
            i -= 1
            game = userDB[currUser]["rentedGame"][i]
            gameLib[game]["copies"] += 1
            userDB[currUser]["rentedGame"].pop(i)
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        break
def DisplayBal():
    print(f"Balance: {round(userDB[currUser]["balance"], 2)}\nPoints: {userDB[currUser]["points"]}")
def TopUp():
    DisplayBal()
    while True:
        try:
            dep = float(input("How much do you want to Deposit? "))
            if not dep:
                return
            if dep <= 0:
                print("Enter a Positive Amount")
                continue
            userDB[currUser]["balance"] += dep
        except ValueError as e:
            print(e)
        break
def LogOut():
    try:
        x = input("Do you wish to log out? Y/n ")
        if not x:
            return
        elif x == 'Y':
            global isLogin
            isLogin = False
            global currUser
            currUser = ''
        elif x == 'n':
            return
        else:
            print("Invalid input")
    except ValueError as e:
        print(e)
def adminLogIn():
    while True:
        try:
            usnm = input("Enter username: ")
            if not usnm:
                return
            passw = input("Enter password: ")
            if usnm != "admin" and passw != "adminpass":
                print("Wrong username or password")
                continue
            global adLogIn
            adLogIn = True
        except ValueError as e:
            print(e)
        break


def UpdateDetails():

    DisplayGameLib()

    while True:
        try:
            i = int(input(f"Enter Choice from 1 to {len(gameLib)}"))
            if not i: 
                return
            
            if i <= 0 or i > len(gameLib):
                print("Enter a proper input")
                continue
            i -= 1

            game = list(gameLib)[i]
            
            y = input("Input the new cost: ")

            z = input("Input the new count of copies: ")


            if not y:
                y = gameLib[game]["cost"]

            if not z:
                z = gameLib[game]["copies"]

            gameLib[game]["cost"] = y
            gameLib[game]["copies"] = z

        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        break


def AddGame():

    DisplayGameLib()

    while True:
        try:
           x = input("Input the name of the game: ")
           if not x:
                return
           if x in gameLib:
               print("Game already exists.")
               continue

           y = float(input("Input the cost of the game: "))

           if y <= 0:
               print("Invalid value. Please input a nonzero positive number (we need to make money).")
               continue

           z = int(input("Input the amount of the copies of the game: "))

           if z <= 0:
               print("Invalid value. Please input a nonzero positive number.")
               continue
           

           gameLib[x] = {"cost" : y, "copies": z}

        

        except ValueError as e:
            print(e)


        break


def RemoveGame():
   
   DisplayGameLib()


   while True:
        try:
            i = int(input(f"Enter Choice from 1 to {len(gameLib)}"))
            if not i: 
                return
            
            if i <= 0 or i > len(gameLib):
                print("Enter a proper input")
                continue
            i -= 1

            game = list(gameLib)[i]

            del gameLib[game]

            
            

        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        break






def main():
    while True:
        try:
            while not isLogin and not adLogIn:
                print("Welcome to the Game Rental System")
                print("1. Display Available Games\n2. RegisterUser\n3. Login\n4. Admin Login\n5. Exit")
                i = int(input("Enter your choice"))
                if i > 5 or i < 1:
                    print("Enter a proper choice")
                if i == 1:
                    DisplayGameLib()
                    pass
                if i == 2:
                    RegisterUser()
                if i == 3:
                    LogIn()
                if i == 4:
                    adminLogIn()
                    pass
                if i == 5:
                    exit(0)
            
            while isLogin:
                print("Welcome {}".format(currUser))
                print("1. Rent Game\n2. Return Game\n3. Inventory\n4. Top-up\n5. Check Balance\n6. Log out")
                i = int(input("Enter Choice"))
                if i > 6 or i < 1:
                    print("Enter a proper choice")
                if i == 1:
                    RentGame()
                    pass
                if i == 2:
                    ReturnGame()
                    pass
                if i == 3:
                    DisplayRented()
                    pass
                if i == 4:
                    TopUp()
                    pass
                if i == 5:
                    DisplayBal()
                    pass
                if i == 6:
                    LogOut()
                    pass
            while adLogIn:
                print("Hello Admin")
                print("1. Update Game Details \n2. Add a game\n3. Remove a Game\n4. Log-Out")
                choice = int(input("Input your choice: "))

                if choice < 1 or choice > 5:
                    print("Provide a valid input")
                    continue
                
                if choice == 1:
                    UpdateDetails()

                if choice == 2:
                    AddGame()

                if choice == 3:
                    RemoveGame()

                if choice == 4:
                    LogOut()







        except ValueError as e:
            print(e) 
    pass

if __name__ == "__main__":
    main()