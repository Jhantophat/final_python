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
            print(lastCommand)
            hiscomman.append(lastCommand)
        else:
            print("No commands to redo")

    elif command == 'u':
        if hiscomman:
            hiscomman.pop()
        else:
            print("No commands to undo")

    elif command == 'h':
        print(hiscomman)

    elif command == 'q':
        print("Thank you for using the star wars movie qoutes")

    elif command == 'l':
        for command in comman:
            print(command)

    else:
        print("ERROR: Unknown command")
        success = False

    return success


command = '_'

while command != 'q':
    printMenu()
    command = menuGetCommand()
    executeCommand(command)
