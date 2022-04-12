"""
Ryan Brock
May 2019
CS 303E

This is a demo for a text-based resource collection game
developed in Python as a final project for CS 303E
(Elements of Computers and Programming). As one of my first
programming projects I have ever completed, it helped to
launch my passion for Computer Science and taught me the
fundamental conects of OOP, data structures, documentation,
and good software development processes.
"""

# Import time and title menu modules
import time
import titleMenus

# Class for handling the player's inventory
# Demo contains amount of wood and stone
# as well as the "level" of axe and pickaxe
class Inventory:  # A Class
    def __init__(self, woodInv, axe, stoneInv, pickaxe):
        self.woodInv = int(woodInv)
        self.axe = int(axe)
        self.stoneInv = int(stoneInv)
        self.pickaxe = int(pickaxe)

# Class for handling the player's main quest
class CurrentQuests:
    def __init__(self, mainQuest):
        self.mainQuest = int(mainQuest)

# Function for handling title screen
# Loops through title menu options until
# player starts game or quits
def titleScreenInputCheck():
    while True:
        titleResult = titleMenus.titleScreen()
        if titleResult == 1:
            newGameConfirmation = titleMenus.newGameConfirm()
            if newGameConfirmation:
                titleMenus.newGameIntro()
                character, currentQuest = newGameSave()
                mainIsland(character, currentQuest)
        elif titleResult == 2:
            saveDataExists = titleMenus.continueGame()
            if saveDataExists == 1:
                character, currentQuest = continueGameSetup()
                time.sleep(2)
                mainIsland(character, currentQuest)
        elif titleResult == 3:
            titleMenus.creditScreen()
        elif titleResult == 4:
            break

# Function that creates a new Inventory object of default values
# Sets up save file with default values and sets the current quest
# Returns the Inventory object and current quest
def newGameSave():
    character = Inventory(0, 0, 0, 0)
    currentQuest = CurrentQuests(0)
    saveFileWrite = open("save.txt", "w")
    saveFileWrite.write("SaveData: True\n")
    saveFileWrite.write("WoodInv: 0\n")
    saveFileWrite.write("Axe: 0\n")
    saveFileWrite.write("StoneInv: 0\n")
    saveFileWrite.write("Pickaxe: 0\n")
    saveFileWrite.write("MainQuest: 0")
    saveFileWrite.close()
    return character, currentQuest

# Function that retrieves save data from save file when an old
# game is continued by populating an Inventory object with the
# save file values
# Returns the Inventory object and current quest
def continueGameSetup():
    saveFileRead = open("save.txt", "r")
    currentSaveList = saveFileRead.readlines()
    for x in range(0, len(currentSaveList)):
        currentSaveList[x] = currentSaveList[x].strip("\n")
    saveFileRead.close()
    woodInvRaw = currentSaveList[1]
    woodInv = woodInvRaw[9:]
    axeRaw = currentSaveList[2]
    axe = axeRaw[5:]
    stoneInvRaw = currentSaveList[3]
    stoneInv = stoneInvRaw[10:]
    pickaxeRaw = currentSaveList[4]
    pickaxe = pickaxeRaw[9:]
    mainQuestRaw = currentSaveList[5]
    mainQuest = mainQuestRaw[11:]
    character = Inventory(woodInv, axe, stoneInv, pickaxe)
    currentQuest = CurrentQuests(mainQuest)
    return character, currentQuest

# Function for handling the player menu
# Contains options for viewing inventory, continuing game, or saving
def characterMenu(character, currentQuest):
    while True:
        try:
            print("\nWelcome to the menu! From here, you can view your inventory, continue the game, or save and return to the Title Screen!")
            print("\n1) Inventory")
            print("2) Continue Game")
            print("3) Save and Return to Title")
            choice = eval(input("Please select a number: "))
            if choice == 1:
                showInventory(character, currentQuest)
            elif choice == 2:
                break
            elif choice == 3:
                return True
            else:
                print("Please enter a 1, 2, or 3!")
        except:
            print("Please enter a 1, 2, or 3!")

# Function for showing inventory
# Demo displays values for wood and stone amount
# as well as which "level" of axe or pickaxe the player has
def showInventory(character, currentQuest):
    if currentQuest.mainQuest == 0:
        print("\nInventory Empty")
    if currentQuest.mainQuest >= 1:
        axeType = ""
        if character.axe == 1:
            axeType = "Wood"
        elif character.axe == 2:
            axeType = "Stone"
        print("\nWood: {0}".format(character.woodInv))
        print("Axe: {0}".format(axeType))
    if currentQuest.mainQuest >= 5:
        pickaxeType = ""
        if character.pickaxe == 1:
            pickaxeType = "Wood"
        elif character.pickaxe == 2:
            pickaxeType = "Stone"
        print("Stone: {0}".format(character.stoneInv))
        print("Pickaxe: {0}".format(pickaxeType))
    else:
        print("\nInventory!!!")

# Function for handing the saving of the game
# Writes save data to save.txt
def saveGame(character, currentQuest):
    time.sleep(1)
    print("\nGame Saving...")
    saveFileWrite = open("save.txt", "w")
    saveFileWrite.write("SaveData: True\n")
    saveFileWrite.write("WoodInv: {0}\n".format(character.woodInv))
    saveFileWrite.write("Axe: {0}\n".format(character.axe))
    saveFileWrite.write("StoneInv: {0}\n".format(character.stoneInv))
    saveFileWrite.write("Pickaxe: {0}\n".format(character.pickaxe))
    saveFileWrite.write("MainQuest: {0}".format(currentQuest.mainQuest))
    saveFileWrite.close()
    time.sleep(2)
    
def mainIsland(character, currentQuest):
    while True:  # While Loop
        if currentQuest.mainQuest == 0:
            while True:
                try:
                    print("\nYou appear to be on a large island floating through the vast expanse of emptiness. There is nothing on the island, save for the strange idol and the 5 trees nearby.")
                    print("\n0) Menu")
                    print("1) Examine Trees")
                    print("2) Examine Idol")
                    choice = eval(input("Please select a number: "))
                    if choice == 0:
                        saveAndExit = characterMenu(character, currentQuest)
                        if saveAndExit == True:
                            saveGame(character, currentQuest)
                            return
                    elif choice == 1:
                        print("\nThe trees look stare down upon you, offering nothing.")
                        time.sleep(2)
                    elif choice == 2:
                        print("\nUpon further inspection, the idol seems ancient, carved entirely out of stone.")
                        time.sleep(2)
                        print("Its figure is humanoid, but not; its figure is far too square to be a human.")
                        time.sleep(2)
                        print("The only part that doesn't appear to be like the rest is what seems to be a large screen in the chest of the idol.")
                        time.sleep(3)
                        print("The screen seems modern and has a small button.")
                        time.sleep(2)
                        print("Upon pressing the button, the screen displays a new message:")
                        time.sleep(2)
                        print('"Collect wood from 5 trees"')
                        time.sleep(2)
                        print("Upon turning around, you notice an wooden axe is now lying on the ground behind you.")
                        time.sleep(2)
                        print("You pick it up.")
                        character.axe = 1
                        currentQuest.mainQuest = 1
                        time.sleep(1)
                        break
                    else:
                        print("Please enter a 0, 1, or 2!")
                except:
                    print("Please enter a 0, 1, or 2!")
        elif currentQuest.mainQuest == 1:
            while True:
                try:
                    currentTrees = 5 - character.woodInv
                    print("\nYou appear to be on a large island floating through the vast expanse of emptiness. There is nothing on the island, save for the strange idol and the {0} trees nearby.".format(currentTrees))    # Using Formatting For Strings
                    print("\n0) Menu")
                    print("1) Cut down a tree")
                    print("2) Examine Idol")
                    choice = eval(input("Please select a number: "))
                    if choice == 0:
                        saveAndExit = characterMenu(character, currentQuest)
                        if saveAndExit == True:
                            saveGame(character, currentQuest)
                            return
                    elif choice == 1:
                        print("\nCutting down tree...")
                        time.sleep(5)
                        print("\nYou cut down one tree.")
                        time.sleep(2)
                        woodInv = character.woodInv + 1
                        character.woodInv = woodInv
                        if woodInv == 5:
                            currentQuest.mainQuest = 2
                            break
                    elif choice == 2:
                        print("\nThe screen on the idol says:")
                        print('"Collect wood from 5 trees"')
                        time.sleep(2)
                    else:
                        print("Please enter a 0, 1, or 2!")
                except:
                    print("Please enter a 0, 1, or 2!")
        elif currentQuest.mainQuest == 2:
            while True:
                try:
                    print("\nYou appear to be on a large island floating through the vast expanse of emptiness. There is nothing on the island, save for the strange idol.")
                    print("\n0) Menu")
                    print("1) Build House")
                    print("2) Examine Idol")
                    choice = eval(input("Please select a number: "))
                    if choice == 0:
                        saveAndExit = characterMenu(character, currentQuest)
                        if saveAndExit == True:
                            saveGame(character, currentQuest)
                            return
                    elif choice == 1:
                        print("\nUsing wood to build house...")
                        time.sleep(10)
                        character.woodInv = 0
                        print("\nUpon finishing, you notice something rise from the darkness...")
                        time.sleep(2)
                        print("\nYou notice that it is another floating island...")
                        time.sleep(2)
                        print("\nThe new island is covered in uncountable trees!")
                        time.sleep(2)
                        print("\nA bridge appears that connects it to your island.")
                        currentQuest.mainQuest = 3
                        break
                    elif choice == 2:
                        print("\nThe screen on the idol states:")
                        print("\nUse the wood to build a house")
                        time.sleep(2)
                    else:
                        print("Please enter a 0, 1, or 2!")
                except:
                    print("Please enter a 0, 1, or 2!")
        elif currentQuest.mainQuest == 3:
            while True:
                try:
                    print("\nThe main island contains the strange idol and your newly built house!")
                    print("\nThere is a connected island covered in trees!")
                    print("\n0) Menu")
                    print("1) Enter House")
                    print("2) Examine Idol")
                    print("3) Travel to Tree Island")
                    choice = eval(input("Please select a number: "))
                    if choice == 0:
                        saveAndExit = characterMenu(character, currentQuest)
                        if saveAndExit == True:
                            saveGame(character, currentQuest)
                            return
                    elif choice == 1:
                        house(character, currentQuest)
                        if currentQuest == 4:
                            break
                    elif choice == 2:
                        print("\nThe screen on the idol states:")
                        print("\nCraft a workbench")
                        time.sleep(2)
                    elif choice == 3:
                        treeIsland(character)
                    else:
                        print("Please enter a 0, 1, 2, or 3!")
                except:
                    print("Please enter a 0, 1, 2, or 3!")
        elif currentQuest == 4:
            while True:
                try:
                    print("\nThe main island contains the strange idol and your newly built house!")
                    print("\nThere is a connected island covered in trees!")
                    print("\n0) Menu")
                    print("1) Enter House")
                    print("2) Examine Idol")
                    print("3) Travel to Tree Island")
                    choice = eval(input("Please select a number: "))
                    if choice == 0:
                        saveAndExit = characterMenu(character, currentQuest)
                        if saveAndExit == True:
                            saveGame(character, currentQuest)
                            return
                    elif choice == 1:
                        house(character, currentQuest)
                        if currentQuest == 4:
                            break
                    elif choice == 2:
                        print("\nThe screen on the idol states:")
                        print("\nCraft a wooden pickaxe")
                        time.sleep(2)
                    elif choice == 3:
                        treeIsland(character)
                    else:
                        print("Please enter a 0, 1, 2, or 3!")
                except:
                    print("Please enter a 0, 1, 2, or 3!")
        elif currentQuest == 5:
            while True:
                try:
                    print("\nThe main island contains the strange idol and your newly built house!")
                    print("\nThere are two connected islands!")
                    print("\n0) Menu")
                    print("1) Enter House")
                    print("2) Examine Idol")
                    print("3) Travel to Tree Island")
                    print("4) Travel to Stone Island")
                    choice = eval(input("Please select a number: "))
                    if choice == 0:
                        saveAndExit = characterMenu(character, currentQuest)
                        if saveAndExit == True:
                            saveGame(character, currentQuest)
                            return
                    elif choice == 1:
                        house(character, currentQuest)
                        if currentQuest == 4:
                            break
                    elif choice == 2:
                        print("\nThe screen on the idol states:")
                        print("\nCraft a wooden pickaxe")
                        time.sleep(2)
                    elif choice == 3:
                        treeIsland(character)
                    else:
                        print("Please enter a 0, 1, 2, or 3!")
                except:
                    print("Please enter a 0, 1, 2, or 3!")

def house(character, currentQuest):
    while True:
        if currentQuest.mainQuest == 3:
            try:
                print("\nYour house is very empty...")
                print("\n1) Build Workbench")
                print("2) Exit House")
                choice = eval(input("Please select a number: "))
                if choice == 1:
                    if character.woodInv >= 5:
                        time.sleep(2)
                        print("\nYou craft a marvelous workbench!")
                        time.sleep(2)
                        character.woodInv -= 5
                        currentQuest.mainQuest = 4
                    else:
                        time.sleep(2)
                        print("\nYou need at least 5 wood!")
                if choice == 2:
                    break
                else:
                    print("Please enter a 1 or 2!")
            except:
                print("Please enter a 1 or 2!")
        elif currentQuest.mainQuest == 4:
            try:
                print("\nYour house has a workbench!")
                print("\n1) Use Workbench")
                print("2) Exit House")
                choice = eval(input("Please select a number: "))
                if choice == 1:
                    while True:
                        try:
                            time.sleep(2)
                            print("\nYou can craft things!")
                            print("\n1) Craft a wooden pickaxe")
                            print("\n2) Leave workbench")
                            choice = eval(input("Please select a number: "))
                            if choice == 1:
                                if character.woodInv >= 5:
                                    print("\nCrafting wooden pickaxe...")
                                    time.sleep(3)
                                    character.woodInv -= 5
                                    character.pickaxe = 1
                                    currentQuest.mainQuest = 5
                                    print("\nYou have crafted a wooden pickaxe!")
                                    time.sleep(2)
                                    print("You feel a slight rumbling and look outside to see a new island has appeared!")
                                    time.sleep(2)
                                    print("The new island seems to have a stone mountain on top!")
                                    time.sleep(2)
                                    break
                                else:
                                    print("\nYou need at least 10 wood!")
                                    time.sleep(2)
                            elif choice == 2:
                                break
                            else:
                                print("Please enter a 1 or 2!")
                        except:
                            print("Please enter a 1 or 2!")
                if choice == 2:
                    break
                else:
                    print("Please enter a 1 or 2!")
            except:
                print("Please enter a 1 or 2!")
        elif currentQuest.mainQuest == 5:
            try:
                print("\nYour house has a workbench!")
                print("\n1) Use Workbench")
                print(") Exit House")
                choice = eval(input("Please select a number: "))
                if choice == 1:
                    while True: # Nested Loop
                        try:
                            time.sleep(2)
                            print("\nYou can craft things!")
                            print("\n1) Craft a Stone Axe")
                            print("2) Craft a Stone Pickaxe")
                            print("3) Leave Workbench")
                            choice = eval(input("Please select a number: "))
                            if choice == 1:
                                if character.woodInv >= 5 & character.stoneInv >= 5:
                                    print("\nCrafting stone axe...")
                                    time.sleep(3)
                                    character.woodInv -= 5
                                    character.stoneInv -= 5
                                    character.axe = 2
                                    print("\nYou have crafted a stone axe!")
                                    time.sleep(2)
                                    break
                                else:
                                    print("\nYou need at least 5 wood and 5 Stone!")
                                    time.sleep(2)
                            elif choice == 2:
                                if character.woodInv >= 5 & character.stoneInv >= 5:
                                    print("\nCrafting stone pickaxe...")
                                    time.sleep(3)
                                    character.woodInv -= 5
                                    character.stoneInv -= 5
                                    character.pickaxe = 2
                                    print("\nYou have crafted a stone pickaxe!")
                                    time.sleep(2)
                                    print("You feel another rumble and look outside to see a new island has appeared!")
                                    time.sleep(2)
                                    print("The new island has a large sign on it!")
                                    time.sleep(2)
                                    break
                                else:
                                    print("\nYou need at least 5 wood and 5 Stone!")
                                    time.sleep(2)
                            elif choice == 3:
                                break
                            else:
                                print("Please enter a 1, 2, or 3!")
                        except:
                            print("Please enter a 1, 2, or 3!")
                if choice == 2:
                    break
                else:
                    print("Please enter a 1 or 2!")
            except:
                print("Please enter a 1 or 2!")


def treeIsland(character):
    while True:
        try:
            print("\nThere are seemingly infinite trees on tree island!")
            print("\n1) Chop down Tree")
            print("2) Return to Main Island")
            choice = eval(input("Please select a number: "))
            if choice == 1:
                print("\nChopping down tree...")
                if character.axe == 1:
                    time.sleep(5)
                    character.woodInv += 1
                    print("\nYou have received 1 wood!")
                    time.sleep(2)
                elif character.axe == 2:
                    time.sleep(4)
                    character.woodInv += 2
                    print("\nYou have received 2 wood!")
            elif choice == 2:
                print("\nYou return to the main island")
                time.sleep(2)
                break
            else:
                print("Please enter a 1 or 2!")
        except:
            print("Please enter a 1 or 2!")


def stoneIsland(character):
    while True:
        try:
            print("\nThere is a large mountain of stone!")
            print("\n1) Mine stone")
            print("2) Return to Main Island")
            choice = eval(input("Please select a number: "))
            if choice == 1:
                print("\nMining stone...")
                if character.pickaxe == 1:
                    time.sleep(5)
                    character.stoneInv += 1
                    print("\nYou have received 1 stone!")
                    time.sleep(2)
                elif character.pickaxe == 2:
                    time.sleep(4)
                    character.stoneInv += 2
                    print("\nYou have received 2 stone!")
            elif choice == 2:
                print("\nYou return to the main island")
                time.sleep(2)
                break
            else:
                print("Please enter a 1 or 2!")
        except:
            print("Please enter a 1 or 2!")

def demoIsland():
    print("\nThere is a large sign on the new island that states:")
    time.sleep(2)
    print("'End of Demo!'")
    time.sleep(2)
    print("Feel free to mine and chop to your heart's content!")
    time.sleep(2)
    print("You return to the main island...")
    time.sleep(2)

# Main function that calls the title screen input
def main():
    titleScreenInputCheck()

# Call to main function
main()
