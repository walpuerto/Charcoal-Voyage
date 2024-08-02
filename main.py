import time
import random
import os

import strings as gameStrings
os.system("")

def printByLine(string, duration, color):
    string = string.split('\n')
    for chop in string:
        time.sleep(duration)
        print(f"\033[38;5;{color}m {chop}\033[0m")

def elipses(duration, message):
    for _ in range(duration):  
        print(f"{message}...", end='\r')
        time.sleep(.5)
        print(f"{message}.. ", end='\r')
        time.sleep(.5)
    print(" "*(len(message)+3), end='\r')

def askIPAddress(stage):
    ipAdress = ""
    while ipAdress != "CLOSE" or ipAdress != "196.786.5.1":
        print("║Enter a IP to connect or CLOSE to go back:                             ║", end="\r")
        ipAdress = input("\033[45G").strip()

        if ipAdress == "CLOSE":
            return False
        
        elif ipAdress != "196.786.5.1" or stage == 1:
            print("║Error: Chat Room unreachable...                                        ║", end="\r")
            print("\033[12C\033[2F")
            continue

        else: return True
     
def formatMessage(sailorID, message):
    print(f"║{time.ctime().split(' ')[4]} | {sailorID}: {message}"+" "*(58-len(sailorID)-len(message))+"║")

def animateMessage(sailorID, message, speedMin, speedMax):
    for i in range(len(message)+1):
        print(f"║{time.ctime().split(' ')[4]} | {sailorID}: {message[0:i]}{' '*(58-len(sailorID)-len(message[0:i]))}║", end="\r")
        time.sleep(random.uniform(speedMin, speedMax))
    print()

def chatLogs(sailorID, stage):
    print()
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║Charcoal Voyage - Chat System | INDIEGO SyStems                        ║")
    print("╠═══════════════════════════════════════════════════════════════════════╣")
    elipses(2, "║Loading Chat Rooms")
    print("║Found Chat Rooms:                                                      ║")
    print("║    - IP: 196.786.5.1 | General                                        ║")
    print("║    - IP: 184.432.6.5 | HSS Space Station                              ║")
    print("║    - IP: 254.387.4.8 | ISS Solar Satelite                             ║")
    print("║    - IP: 200.810.0.7 | N-Point Stellar Hub                            ║")
    print("║    - IP: 111.000.1.1 | Earth                                          ║")
    print("║                                                                       ║")
    time.sleep(2)
    if askIPAddress(stage):
        print("║                                                                       ║")
        print("║Connection Successful!                                                 ║")
        time.sleep(1)
        animateMessage(sailorID, 'Hi! Is anyone there?', 0.05, 0.1)
        time.sleep(2)
        animateMessage(sailorID, '...', 0.05, 0.1)
        time.sleep(1)
        animateMessage(sailorID, 'HELLO! IS ANYONE ALIVE BACK THERE?!', 0.05, 0.07)
        time.sleep(1)
        animateMessage(sailorID, 'These idiots...', 0.1, 0.1)
        time.sleep(2)
        elipses(6, "║Incoming message...")
        formatMessage("Matthew-Go", "HI! I HAVE RECIEVED YOUR MESSAGE! THANK GOD")
        elipses(5, "║Incoming message...")
        formatMessage("Matthew-Go", 'THE LEGION IS ATTACKING OUR SHIP!!!')
        elipses(5, "║Incoming message...")
        formatMessage("Matthew-Go", 'PLEASE SEND HEPLP!!!')
        elipses(3, "║Incoming message...")
        formatMessage("Matthew-Go", 'I AND THE CREW ARE IN THE SAFE ROOM')
        elipses(2, "║Incoming message...")
        formatMessage("Matthew-Go", 'WE CAN HEAR THEM RAMMING OUR DOOR')
        elipses(2, "║Incoming message...")
        formatMessage("Matthew-Go", 'I DONT THINK WE CAN LAST ANY LONGER')
        elipses(3, "║Incoming message...")
        formatMessage("Matthew-Go", 'OH SH- THEY ARE HERE')
        elipses(3, "║Incoming message...")
        formatMessage("Matthew-Go", f'{sailorID} HELP ME PLEA-')
        time.sleep(2)
        animateMessage(sailorID, 'I AM COMING!', 0.1, 0.3)
        print("║                                                                       ║")
        print("║ Press any key to close chatlogs                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        input()
    return True

def controlShip(sailorID, stage):
    # if stage == 0:
    #     print()
    #     print("╔═══════════════════════════════════════════════════════════════════════╗")
    #     print("║Charcoal Voyage - Spaceship Control | INDIEGO SyStems                  ║")
    #     print("╠═══════════════════════════════════════════════════════════════════════╣")
    #     print("║                                                                       ║")
    #     print("║                              ╲╲   ╱╱                                  ║")
    #     print("║                               ╲╲ ╱╱                                   ║")
    #     print("║                                │╳│                                    ║")
    #     print("║                               ╱╱ ╲╲                                   ║")
    #     print("║                              ╱╱   ╲╲                                  ║")
    #     print("║                                                                       ║")
    #     print("║                       System Unavailable :(                           ║")
    #     print("║                                                                       ║")
    #     print("║ Press any key to close Spaceship Control                              ║")
    #     print("╚═══════════════════════════════════════════════════════════════════════╝")
    #     input()
    #     return

    scoreMax =  100
    score = 0
    while True and score <= scoreMax:
        enemyLocationX = random.randint(-35, 35)
        if enemyLocationX == 0: enemyLocationX + (lambda: 1 if random.randint(0,1) == 0 else -1)()

        enemyLocationY = random.randint(-100, 100)
        if enemyLocationY == 0: enemyLocationY + (lambda: 1 if random.randint(0,1) == 0 else -1)()

        print()
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║Charcoal Voyage - Spaceship Control | INDIEGO SyStems                  ║")
        print("╠═══════════════════════════════════════════════════════════════════════╣")
        print("║ Instructions:                                                         ║")
        print("║    1. Determine which quadrant the ENEMY from their coordinates       ║")
        print("║    2. Type the QUADRANT NUMBER into the machine                       ║")
        print("║    3. Press ENTER                                                     ║")
        print("║                                                                       ║")
        print("║ Destroy as many enemy space ships as you can in 60 seconds!           ║")
        print("║ Good luck!                                                            ║")
        print("╟───────────────────────────────────────────────────────────────────────╢")
        print("║Control Panel:                                                         ║")
        elipses(3, "║Loading Cameras")
        gameStrings.spaceCam()

        print(f"║ Enemy Location: {enemyLocationX}, {enemyLocationY}" +  (" "*(52 - len(str(enemyLocationX)) - len(str(enemyLocationY)))) +"║")
        input()
        return


def part1():
    skipAnimation = True
    sailorID = "T"
    choice = ""
    stage = 0
    while True:
        print("\033[2J\033[H", end="\r")

        if not skipAnimation: printByLine(gameStrings.logo, 0.1, "231")
        else: printByLine(gameStrings.logo, 0, "231")

        print("Charcoal Voyage - Version 0.1 | INDIEGO SyStems")
        if not skipAnimation: sailorID = input("Enter Pilot Name: ")
        else: print(f"Enter Pilot Name: {sailorID}")

        print()
        if not skipAnimation: elipses(2, "Gathering Spaceship Info")
        print("Settings: Normal, Hyper-Speed, Low-Fuel")
        if not skipAnimation: time.sleep(1)
        print("Distance from Earth: 26000 ly")
        if not skipAnimation: time.sleep(1)
        print("Remaining Fuel: 4200000 L")
        if not skipAnimation: time.sleep(3)
        print()
        print(f"Welcome back to Hyper-Deep Space, {sailorID}!")
        print("What would you like to do?")
        print("    1) Open Chat Logs")
        print("    2) Control Spaceship")
        print("    3) Quit")
        print()

        choice = input("Enter a number: ").strip()
        
        if choice == "" or not choice.isnumeric or int(choice) > 3:
            choice = "1"

        if choice == "1":
            chatLogs(sailorID, stage)
            skipAnimation = True
            stage = 1
            continue
            
        if choice == "2":
            controlShip(sailorID, stage)
            skipAnimation = True
            continue
            
        if choice == "3": quit()

def quit():
    print("\033[2J\033[H")
    printByLine(gameStrings.skull, .05, "255")
    time.sleep(1)
    exit()

def game():
    part1Result = part1()

if __name__ == '__main__':
    game()