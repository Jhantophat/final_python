import random
import commands
hiscomman = []
#main menu code
def printMenu():
    print("-----------------------------------------")
    print("star wars movie quotes ")
    print("-----------------------------------------")
    print("i\trandom quotes")
    print("l\tlist of quotes")
    print("u\tundo last quotes")
    print("r\tredo last quotes")
    print("h\thistory of quotes used")
    print("q\tQuit")
    print("------------------------------------------")

#insert command code
def menuGetCommand():
    return input("Enter a command: ").lower().strip()
#where command gets excuted
def executeCommand(command):
    global hiscomman
    success = True
   
#the if states that make produce the the out come
    if command == 'i':
        #here is where we get the code from the outside file
        word = random.choice(commands.comman)
        print("********************************")
        print(word)
        print("********************************")
        hiscomman.append(word)

   elif command == 'r':
        if hiscomman:
            lastCommand = hiscomman[-1]
            print("********************************")
            print(lastCommand)
            print("********************************")
            hiscomman.append(lastCommand)
        else:
            print("********************************")
            print("No commands to redo")
            print("********************************")

    elif command == 'u':
        if hiscomman:
            hiscomman.pop()
        else:
            print("********************************")
            print("No commands to undo")
            print("********************************")

    elif command == 'h':
        print(hiscomman)

    elif command == 'q':
        print("********************************")
        print("Thank you for using the star wars movie qoutes")
        print("********************************")

    elif command == 'l':
        for command in commands.comman:
            print("********************************")
            print(command)
            print("********************************")

    else:
        print("********************************")
        print("ERROR: Unknown command")
        print("********************************")
        success = False

    return success


command = '_'

while command != 'q':
    printMenu()
    command = menuGetCommand()
    executeCommand(command)
