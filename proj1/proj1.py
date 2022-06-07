# File:    proj1.txt
# Author:  Muhammed Muktar
# Date:    10/18/2018
# Section: 30
# E-mail:  mmuktar1@umbc.edu
# Description:
#   Project game based on the user running away from a monster, they have to survive 7 days or travel 150 miles to the nearest city. The Demogorgon.

##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed  #

seed(100)  #
##################################

#constants for player and monster health
MAX_HEALTH = 100
MIN_HEALTH = 0

DEM_MAX_HEALTH = 300

#constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#constant lists of food and items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]

ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys", "Walkman", "Laser Cannon","Rubber Band"]

### put any other constants you want here ###

#constant for fight options
FIGHT = ["Fight", "Flail", "Flee"]

#constants to check different options in menu
OPTION_1 = 1
OPTION_2 = 2
OPTION_3 = 3
OPTION_4 = 4

#constants for item damage
DMG_FLASHLIGHT = 5
DMG_WALKIE_TALKIE = 10
DMG_RUBBER_BAND = 25
DMG_SWORD = 50
DMG_LASER_CANNON = 100

#constants for food health
HEALTH_EGGO = 10
HEALTH_REESES = -30
HEALTH_POP_ROCKS = -5
HEALTH_OVALTINE = 15
HEALTH_WONDER_BREAD = 25
HEALTH_TWINKIES = 30

#constants for distance multi
BIC_MULTI_ = 1.5
HEELYS_MULTI = 1.25


# getUserChoice() asks the user to select a choice from a list of choices
#                 continuously prompts the user until the choice is valid
#                 a valid choice is one that is a valid index in the list
# Input:          choices; a list of all the possible choices available
# Output:         choice; the validated choice that the user made
def getUserChoice(choiceList):
    #asks user for choices
    getChoice = int(input("Enter a choice: "))

    #makes sure choice is valid
    while getChoice < 1 or getChoice > len(choiceList):
        getChoice = int(input("Enter a valid choice: "))
    print("")
    return getChoice


### put the rest of your function headers here ###


#displayMenu() displays a list of options to the user
#Input:        choices; a list, filled with options
#Output:       no output
def displayMenu(choices):
    count = 0
    print("Your options are:")
    while count < len(choices):
        print(count + 1, "-", choices[count])
        count += 1
    print("")


#viewInventory() displays the user's current inventory
#Input:          inventoryList; a list of user's inventory
#Output:         no output
def viewInventory(inventoryList):
    print("This is what your inventory looks like:")
    print(inventoryList, "\n")


#viewStats() displays the users health, distance, and equipped
#Input:      health; player health. distance; current distance. equipped; current equipped
#Output:     no output
def viewStats(health, distance, equipped):
    print("Health: ", health)
    print("Distance traveled: ", distance)
    print("Equipped: ", equipped, "\n")


#eatBreakFast() Adds 10 health to the user
#Input:         player_health; player's health
#Output:        newPlayerHealth; health plus 10 or plus the remaining health
def eatBreakfast(player_health):
    #adds health to player health
    newPlayerHealth = player_health + HEALTH_EGGO

    #calculates the increased health
    if newPlayerHealth > MAX_HEALTH:
        increasedBy = MAX_HEALTH - player_health
        newPlayerHealth = MAX_HEALTH
    else:
        increasedBy = newPlayerHealth - player_health

    print("You ate the Eggo Waffle. So bad, yet so good.")
    print("Your health increased by", int(increasedBy), "\n")

    return newPlayerHealth


#equalRandom() gives an equally random chance to pull something out a list
#Input:        checklist; a list of items
#Output:       checklist[num]; equally random item in the list
def equalRandom(checklist):
    #gets ran from 0 to lenlist -1
    num = randint(0, len(checklist) - 1)
    return checklist[num]


#findBackPack() event to find a food in a back pack
#Input:         no input
#Output:        foodFound; equally randomized food found in a backpack
def findBackPack():
    foodFound = equalRandom(FOODS)
    print("As you were walking you found a backpack.")
    print("Inside the backpack, there is some", foodFound)
    print("Do you want to eat it? \n")

    return foodFound


#findShack() event to find an item in a shack
#Input       no input
#Output      itemFound; equally randomized item found in shack
def findShack():
    itemFound = equalRandom(ITEMS)
    print(
        "You passed by an old shed and decided to go inside. Something on the shelf catches your eye. You reach up to grab the item. It's a",
        itemFound)
    print("The", itemFound, "has been added to your inventory. \n")

    return itemFound


#fallInDitch() event to fall in a ditch. Prints out event
#Input       no input
#Output      no output
def fallInDitch():
    print(
        "You fell into a trench because you weren't paying attention to the gigantic hole right infront of you."
    )
    print("It took a whole extra day for you to climb out")


#calcuDistance() calculates the distance for each day/event
#Input           health; player health. inventoryList; player's inventory
#Output          distance; calculated distance
def calcuDistance(health, inventoryList):
    #calculates distancess
    distance = (health / 4) + 5
    #gives the multiplier
    if "Bicycle" in inventoryList:
        distance *= BIC_MULTI_
    elif "Heelys" in inventoryList:
        distance *= HEELYS_MULTI
    return distance


#fight() event for fighting the monster
#Input   player_health; player's health, item; item equipped. inventory; player's inventory
#Output  health; the remaining health of the player after the fight
def fight(player_health, item, inventory):
    monsterHealth = DEM_MAX_HEALTH
    monsterDamage = 20
    #halfs health if Hi-C is in inventory
    if ("Hi-C" in inventory):
        monsterHealth /= 2
    health = player_health
    #while player is alive and monster is alive
    while (health > MIN_HEALTH and monsterHealth > MIN_HEALTH):
        print("Your health:", health)
        print("Monster health:", monsterHealth, "\n")
        print("What do you do now? \n")
        displayMenu(FIGHT)
        askChoice = getUserChoice(FIGHT)
        #fight
        if askChoice == OPTION_1:
            print("You strike the Demogorgon with your", item, "for",
                  str(calcDamage(item)) + ".")
            monsterHealth -= calcDamage(item)
            if ("Walkman" in inventory):
                monsterDamage *= .75
            print("The Demogorgon strikes you back for",
                  str(monsterDamage) + ". \n")
            health -= monsterDamage
        #give up
        elif askChoice == OPTION_2:
            print(
                "You throw your life less body at the huge Demogorgon in front of you."
            )
            return MIN_HEALTH
        #flee
        elif askChoice == OPTION_3:
            rannum = randint(1, 10)
            if rannum <= 3:
                print(
                    "You try to run away from the fight. You are successful, and you live to die another day."
                )
                return health
            else:
                print(
                    "You try to run away from the fight. You are not successful. The Demogorgon hits you for",
                    str(monsterDamage / 2) + ".")
                health -= monsterDamage / 2


#calcuDamage() calculates the damage from an item
#Input:        item; current equipped item
#Output:       damag; the damage that items does
def calcDamage(item):

    #returns the damage from item equipped
    if (item == "Sword"):
        damag = DMG_SWORD
    elif (item == "Laser Cannon"):
        damag = DMG_LASER_CANNON
    elif (item == "Rubber Band"):
        damag = DMG_RUBBER_BAND
    elif (item == "Flashlight"):
        damag = DMG_FLASHLIGHT
    elif (item == "Walkie Talkie"):
        damag = DMG_WALKIE_TALKIE
    else:
        return 0

    return damag


#eat() calculates the health the players after they eat food from backpack
#Input food; food the player has chosen to eat. player_health; player's health
#Output newPlayerHealth; health after player eats food
def eat(food, player_health):

    #prints output for eating a certain food
    print("You ate the", food + ".", end="")
    if (food == "Reese's Pieces"):
        newPlayerHealth = player_health + HEALTH_REESES
        print("A perfect blend of chocolate, peanut butter, and posion.")
    elif (food == "Pop Rocks"):
        newPlayerHealth = player_health + HEALTH_POP_ROCKS
        print("If only you knew how deadly they popped.")
    elif (food == "Ovaltine"):
        newPlayerHealth = player_health + HEALTH_OVALTINE
        print(
            "A work of rich delicios chocolate malt, too bad you dont have milk."
        )
    elif (food == "Wonder Bread"):
        newPlayerHealth = player_health + HEALTH_WONDER_BREAD
        print("It's bread, just eat it.")
    elif (food == "Twinkies"):
        newPlayerHealth = player_health + HEALTH_TWINKIES
        print("An American snack, just dont eat too many.")

    #calculates the changed health
    if newPlayerHealth > MAX_HEALTH:
        changedBy = MAX_HEALTH - player_health
        newPlayerHealth = MAX_HEALTH
    else:
        changedBy = newPlayerHealth - player_health

    #prints changed health statement
    if (changedBy < 0):
        print("Your health decreased by", int((changedBy**2)**(1 / 2)), "\n")
    else:
        print("Your health was increased by", int(changedBy), "\n")

    return newPlayerHealth


def main():
    #list for menu options
    daily_choices = [
        "View Inventory", "View Current Stats", "Eat an Eggo Waffle",
        "Nothing Else"
    ]
    equiq_menu = ["Equip", "Unequip", "I forgot. What was I doing again?"]
    eat_menu = ["Eat possibly molded food", "Waste it, you swine"]
    leave_stay = ["Pack up camp", "Stay"]

    #default values needed to begin game
    inventory = ["Walkie Talkie", "Flashlight"]
    currentHealth = MAX_HEALTH
    currentDistance = 0
    currentEquipped = "N/A"
    currentDay = 1

    #start of game
    print(
        "After miles and miles of hiking in the woods, you finally set up camp"
    )
    print("Your phone buzzes *dramatically*,")
    print("\t THE DEMOGORGON HAS ESCAPED. \tRUN.\n")
    # while the player isn't dead and hasn't made it far enough
    while (currentHealth > MIN_HEALTH and currentDistance < SURVIVE_DIST
           and currentDay < SURVIVE_DAYS):
        print("The sun rises on day", currentDay, "in the forest \n")
        rannum = randint(1, 10)
        finishedMorning = False
        ateBreakfast = False

        # show menu with the daily choices you can make
        print("What would like to do this morning? \n")
        while (not finishedMorning):

            displayMenu(daily_choices)
            askChoice = getUserChoice(daily_choices)

            #view the inventoey
            if askChoice == OPTION_1:
                viewInventory(inventory)
                print("Do you want to equip an item?")
                displayMenu(equiq_menu)
                askChoice = getUserChoice(equiq_menu)

                #equipping an item
                if askChoice == OPTION_1:
                    displayMenu(inventory)
                    askChoice = getUserChoice(inventory)
                    currentEquipped = inventory[askChoice - 1]
                    print("You have equipped", currentEquipped)
                #unequpping an item
                elif askChoice == OPTION_2:
                    print("You unequipped the", currentEquipped)
                    currentEquipped = "N/A"
                elif askChoice == OPTION_3:
                    print("Thats fine")

                print("What else would like to do this morning? \n")
            #view the player's stats
            elif askChoice == OPTION_2:
                viewStats(currentHealth, currentDistance, currentEquipped)
                print("What else would like to do this morning? \n")
            #allow player to eat breakfast
            elif askChoice == OPTION_3:
                if (not ateBreakfast):
                    currentHealth = eatBreakfast(currentHealth)
                    ateBreakfast = True
                else:
                    print("You already ate breakfast")

                print("What else would like to do this morning? \n")
            elif askChoice == OPTION_4:
                finishedMorning = True
                displayMenu(leave_stay)
                askChoice = getUserChoice(leave_stay)

        #asks to pack up or stay
        if askChoice == OPTION_1:
            print(
                "You decide to pack up camp and go into the directions of the nearest town\n"
            )

            #20% chance for backpack event
            if (rannum <= 2):
                currentDistance += calcuDistance(currentHealth, inventory)
                foundFood = findBackPack()
                displayMenu(eat_menu)
                askChoice = getUserChoice(eat_menu)

                #asks user if they want to eat it
                if askChoice == OPTION_1:
                    currentHealth = eat(foundFood, currentHealth)
                elif askChoice == OPTION_2:
                    print("Starve.")

            #20% chance for shed event
            elif (rannum <= 4):
                inventory.append(findShack())
                currentDistance += calcuDistance(currentHealth, inventory)

            #20% chance for trench event
            elif (rannum <= 6):
                fallInDitch()
                currentDistance += calcuDistance(currentHealth, inventory) / 2
                currentDay += 1

            #30% for fighting the monster
            elif (rannum <= 9):
                currentDistance += calcuDistance(currentHealth, inventory)
                currentHealth = fight(currentHealth, currentEquipped,
                                      inventory)
            else:
                currentDistance += calcuDistance(currentHealth, inventory)
                print("Nothing has happened, you live another day \n")

            #prints if the itmes in the inventory helped the user
            if "Bicycle" in inventory:
                print("The Bicycle you found improved your distance")
            elif "Heelys" in inventory:
                print("The Heelys you found improved your distance")

            print("You have now traveled", currentDistance, "\n")
        #if user stays
        elif askChoice == OPTION_2:
            #70% chance to fight
            if (rannum <= 7):
                currentHealth = fight(currentHealth, currentEquipped,
                                      inventory)
            #10% chance to rest
            else:
                print(
                    "Nothing has happened, you live another day. Enjoy your rest \n"
                )
                currentHealth = MAX_HEALTH
        #next day
        currentDay += 1
    #if player has died
    if (currentHealth <= 0):
        print("You died, try again. \n")
    #if days is >= 7 or distance is >= 150
    else:
        #won game
        print("Congragulations!")
        print("You made it to civilization alive.")
        print("It took you", currentDay, "to go",
              str(currentDistance) + ". \n")

    #prints stats
    print("Finial Stats: \n")
    print("Distance traveled:", currentDistance)
    print("Equipped Item:", currentEquipped)


main()
