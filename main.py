import random
import commands
hiscomman = []

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

def menuGetCommand():
    return input("Enter a command: ").lower().strip()

def executeCommand(command):
    global hiscomman
    success = True
   

    if command == 'i':
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

# main program
command = '_'

while command != 'q':
    printMenu()
    command = menuGetCommand()
    executeCommand(command)
