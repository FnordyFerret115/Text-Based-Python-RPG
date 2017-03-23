import os
import random
import time
from utilities import roll
from battle import *


class Character(object):
    # A Class for ALL characters - player, enemy etc.
    def __init__(self, name, maxhp, nowhp, armor, damage, strength,
                 intelligence, wisdom, dexterity, constitution, charisma,
                 inventory, profession):
        self.name = name
        self.maxhp = maxhp
        self.nowhp = nowhp
        self.armor = armor
        self.damage = damage
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity#agility
        self.constitution = constitution#endurance
        self.charisma = charisma
        self.inventory = inventory
        self.profession = profession
        

#class Fighter(Character):
    #Perks,imune to negitive status,increased damage,decreased recoil taken.

#class Tank(Character):
        #Perks,defence gives more recoil 25%, defence starts from higer number,doubled health pool. 
    
#class Cleric(Character):
    #Perks, positive status has increased potency, revive, increased healing.

#class Satianist(Character):
    #Perks, imunity to negitive status,attacks have a 33% chance to inflict negitive status,revive.
    

class Player(Character):
    # A class for the Player character only.
    # We will use a few parameters to set initial variables
    def __init__(self):
        super(Player, self).__init__(name="", maxhp=10,nowhp=10, armor=5, damage=10, strength=7,
                         intelligence=7, wisdom=7, dexterity=7, constitution=7,
                         charisma=7, profession="" ,inventory={})
        
 
    invertory = {}  # ["itemName"] = [weight, quantity, "type", value]
    perks = {'heart':False,'soul':False,'perk3':False}
    level = 1
    levelxp = 7
    nowxp = 0
    nowcarrywieght = 0
    maxcarrywieght = 50


class Enemy(Character):
    # a class for any enemy.
    def __init__(self):
        super(Enemy,self).__init__(name="", maxhp=10, nowhp=10, armor=5, damage=10,
                         strength=7, intelligence=7, wisdom=7, dexterity=7,
                         constitution=7, charisma=7, inventory=[],
                         profession="")
    
    level = 1
    exp = 0

def new_maxhp(character):
    maxhpset = int(round(10+character.constitution+(character.level*0.5*character.constitution),0))
    character.maxhp = maxhpset
    character.nowhp = maxhpset

def new_maxwieght():
    maxwieghtset = int(round(10+character.strength*10,0))
    playerchar.maxcarrywieght = maxwieghtset

def new_wieghtset():
    totalWieght = 0
    for key, value in playerchar.invertory.iteritems():
        totalWieght = totalWieght + (value[0] * value[1])

    playerchar.nowcarrywieght = len(playerchar.invertory)
    return totalWieght
    

playerchar = Player()
enemychar = Enemy()

# simply call playerchar rather than calling the Class each time


def menu():
                            # Running the Main Menu under a single Function.
                            # This is the simplest method of running the menu
    while True:
        print("|==================|")
        print("Welcome to Py RPG!")
        print("Please select an option!")
        print("1. Start a Game\n")
        print("2. Settings\n")
        print("3. Quit")
        choice = input("\n>")
        if choice == 1 or choice == "start":
            time.sleep(1)
            gameloop()
        elif choice == 2 or choice == "settings":
            time.sleep(1)
            settings()
        elif choice == 3 or choice == "quit":
            break
        else:
            print("Please select an option from the menu.")


def settings():
    # Settings page for all amendments
    # TODO - create a 'settings' file and have this read/amend it?
    print("Nothing exists here at the moment!")
    menu()


def gameloop():
    # the main game loop, contains all calls to relevant functions
    while True:
        print("This is the main game")
        print("Let's begin. What is your name?")
        playerchar.name = raw_input(">")
        print("Well then, " + playerchar.name + ", let us begin.")
        statchoice()


def choosestat(statname, max, min, stats):
    # Takes the name of the stat
    # as mentioned in the Player/Character class and
    # a min/max value for the length. Allows the player
    # to set their stats for the char.
    statname_2 = statname
    max_2 = max
    min_2 = min
    stats_2 = stats
    print("Your stat choices are: " + str(stats))
    choice = int(input("Please select a " + statname + " score \( " +str(min)+":"+str(max)+")\n"))
    if type(choice) == int and choice < (max+1) and choice > (min-1):
        setattr(playerchar, statname, stats[(choice-1)])
        stats.pop(choice-1)
    else:
        print("Please select a valid option.\n")
        choosestat(statname_2, max_2, min_2, stats_2)


def displaystats(entity):
            # quick function to display all relevant stats in-line.
        print("Are you happy with your choices?\n")
        print("Strength: " + str(entity.strength))
        print("Intelligence: " + str(entity.intelligence))
        print("Wisdom: " + str(entity.wisdom))
        print("Dexterity: " + str(entity.dexterity))
        print("Constitution: " + str(entity.constitution))
        print("Charisma: " + str(entity.charisma))


def statchoice():
    # Using the roll function, we get 6 ability scores, append them to 'stats',
    # and run the choosestat function for each to set stats.
    stats = []
    stats.append(roll(4, 6))
    stats.append(roll(4, 6))
    stats.append(roll(4, 6))
    stats.append(roll(4, 6))
    stats.append(roll(4, 6))
    stats.append(roll(4, 6))
    

    choosestat("strength", 6, 1, stats)
    choosestat("intelligence", 5, 1, stats)
    choosestat("wisdom", 4, 1, stats)
    choosestat("dexterity", 3, 1, stats)
    choosestat("constitution", 2, 1, stats)
    choosestat("charisma", 1, 1, stats)

    displaystats(playerchar)
    reroll = raw_input("Do you wish to re-roll?")
    if reroll == "yes" or reroll == "y":
        statchoice()
    else:
        new_maxhp(playerchar)
        new_maxhp(enemychar)
        new_maxwieght()
        text_1()


def text_1():
    print "|================|"
    print "Hello"
    time.sleep(1)
    print "I am here to teach you how your profession works."
    time.sleep(1)
    print "Each profession will give you differnt perks,"
    print "for example increased health, so choose wisely."
    time.sleep(1)
    profession()
    
def profession():
    while True:
        print "This is your choice of professions."
        print "Fighter"
        print "Tank"
        print "Cleric"
        print "Satianist"
        choice = raw_input(">")
        professionList = ["Fighter","Tank","Cleric","Satianist"]
        if choice.title() in professionList:
            profChoice = professionList.index(choice.title())
            playerchar.profession = str(professionList[profChoice])
            
            break
        else:
            print "Please select a valid option.\n"
            
    text_2()

def text_2():
    global battleOutcome
    battleOutcome = ""
    print "Now, " + playerchar.name +" lets battle now your a " + playerchar.profession + "."
    battle()
    print "Well done you " + battleOutcome
    print "let me heal you up"
    heal()
    print "So you are now level" + playerchar.level + "."
    print "So you have choosen a perk when you leveled up."
    print "Your perks effect how you battle and your hp aswell as your damage."
    print "But not all of them they also effect what you can do in the world as you explore."
    print "Using theese perks will give xp which is dependent on your intellegence"
    print "You can also increase the carry weight of your character."
    text_3()

def heal():
    playerchar.nowhp = playerchar.maxhp
    

def level_check(exp_gain):
    playerchar.nowxp = int(round(playerchar.nowxp  + exp_gain * (1+round(0.05 * playerchar.intelligence, 2))))
    #playerchar.level = int(round(playerchar.exp/10,0))
    #new_maxhp(playerchar)
    if int(playerchar.nowxp) >= int(playerchar.levelxp):
        print "wow you leveled up, well done!"
        playerchar.level += 1
        playerchar.nowxp =playerchar.nowxp - playerchar.levelxp
        playerchar.levelxp =playerchar.levelxp*1.5
        print "you are now level " + str(playerchar.level)
        new_maxhp(playerchar)
        perk_choice()
        playerchar.nowxp=round(playerchar.nowxp)
    else:
        print "You have " + str(playerchar.nowxp) + " xp."

def perk_choice():
    for key in playerchar.perks:
        if playerchar.perks[key] == False:
            print key
    choice = str(raw_input("\nPlease select a perk\n"))
    for key, value in playerchar.perks.iteritems():
        if key.startswith(str(choice)):
            value = True
            level_check(0)
            print(str(key) + str(value))
        else:
            print("Please select a valid option.\n")
            
def text_3():
    print "But you don't know what that is let em give you an item so you can find out"
    playerchar.invertory["Steak"] = [0.5, 5, "food", 15]
    new_wieghtset()
    open_invertory()
    print "You are carrying " + str(new_wieghtset()) + "Out of a maximum: " + str(playerchar.maxcarrywieght)




def open_invertory():
    for key in playerchar.invertory:
            print key
    choice = str(raw_input("\nPlease select a item\n type Close to close\n"))
    for key, value in playerchar.invertory.iteritems():
        if key.startswith(str(choice)):
            value = True
            print(str(key) + str(value))
        else:
            print("Please select a valid option.\n")
             

    

def printHealth(hp):
    print ("You have ") + str(hp) + (" Hitpoints\n")

def printEnemyHealth(hp):
    print ("Your enemy has ") + str(hp) + (" Hitpoints\n")

def printdamage(dam):
    print ("You did ") + str(dam) + (" Points of damage!\n")

def printEnemydamage(dam):
    print ("Enemy did ") + str(dam) + (" Points of damage!\n")

text_3()






##for key in inventory:
##    totalWeight = totalweight + (value[0] * value[1])
##
##enemies = {'Goblin' : [int,str,....] }
##
##def battle(enemy)
##battle(enemies['Goblin'])

