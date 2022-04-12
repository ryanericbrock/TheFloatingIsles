"""
Ryan Brock
May 2019
CS 303E

This file contains all of the user interfaces for the
various title screen menus in the game demo. This includes
the main title screen, a new game confirmation screen,
the new game introduction, a continue game screen, a function
to verify save files, and a credits screen.
"""

# Import modules
import time

def titleScreen():
    print("\nThe Floating Isles Demo\n")
    print("1) New Game")
    print("2) Continue")
    print("3) Credits")
    print("4) Quit")
    while True:
        try:
            titleInput = eval(input("Please select a number: "))
            if titleInput == 1:
                return 1
            elif titleInput == 2:
                return 2
            elif titleInput == 3:
                return 3
            elif titleInput == 4:
                return 4
            else:
                print("Please enter a 1, 2, or 3!")
        except:
            print("Please enter a 1, 2, or 3!")


def newGameConfirm():
    while True:
        try:
            print("\nWARNING!")
            print("STARTING A NEW GAME WILL OVERWRITE ANY SAVE DATA!")
            print("ARE YOU SURE YOU WISH TO START A NEW GAME?")
            time.sleep(1)
            print("\n1) Yes")
            print("2) No")
            newGameConfirmation = eval(input("Please select a number: "))
            if newGameConfirmation == 1:
                print("\nStarting New Game...")
                time.sleep(2)
                return True
            elif newGameConfirmation == 2:
                print("\nReturning to Title Screen...")
                time.sleep(2)
                return False
            else:
                print("Please enter a 1 or 2!")
        except:
            print("Please enter a 1 or 2!")


def newGameIntro():
    print("\nNothing but pure darkness surrounds you...")
    time.sleep(2)
    print("\nFloating through the empty void...")
    time.sleep(2)
    print("\nWho are you? Where are you? No memories resurface...")
    time.sleep(2)
    print("\nThen, you feel the ground. Your vision clears and you realize the truth...")
    time.sleep(2)
    print(
        "\nYou are alone. On what appears to be an empty island. Except instead of water, there is a vast nothing surrounding you.")
    time.sleep(3)
    print("\nAll that you see on the island is a few trees and a large idol.")
    time.sleep(2)
    print("\nWhat mysteries does this island hold?")
    time.sleep(2)
    print("\nWelcome to...The Floating Isles!")
    time.sleep(2)


def continueGame():
    saveDataExists = checkSaveFile()
    if saveDataExists == 1:
        return 1


def checkSaveFile():
    print("\nChecking for save data...")
    time.sleep(2)
    try:
        saveFileRead = open("save.txt", "r")
        saveDataStateRaw = saveFileRead.readline()
        saveDataState = saveDataStateRaw.strip("\n")
        saveDataState = saveDataState[10:]
        saveFileRead.close()
        if saveDataState == "False":
            print("\nNo Save Data Exists!")
            print("Returning to Title Screen!")
            time.sleep(1)
            return 0
        elif saveDataState == "True":
            print("\nLoading Save...")
            return 1
        else:
            print("\nSave Data Corrupt")
            print("Returning to Title Screen!")
            return 0
    except:
        print("\nSave Data Corrupt")
        print("Returning to Title Screen!")
        return 0


def creditScreen():
    print("\nCredits:")
    print("Ryan Brock")
    print("Berkin Kutluk\n")
    print("1) Return to Title")
    while True:
        try:
            creditInput = eval(input("Select 1 to return to title: "))
            if creditInput == 1:
                break
            else:
                print("Please enter a 1!")
        except:
            print("Please enter a 1!")
