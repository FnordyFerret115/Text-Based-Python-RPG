import os
from time import *
import random
from utilities import roll


def battle():
    global battleOutcome
    player_damage = int(round(playerchar.strength * 0.5 + playerchar.level,0))  
    enemy_damage = int(round(enemychar.strength * 0.5 + enemychar.level,0))
    while True:
        if playerchar.nowhp <= 0:
            print "You have died"
            battleOutcome = "tried your hardest."
            break
        elif enemychar.nowhp <= 0:
            print "You win!"
            battleOutcome = "beat me."
            level_check(enemychar.maxhp)
            break
        else:
            print "|==============|"
            print " Pick An Action"
            print " 1 - Attack"
            print " 2 - Defend"
            print " 3 - Run Away"
            print "|==============|"
            choice = input("\n" + "Select an Action" + "\n")
            choice = int(choice)

            if choice == 1:
                enemychar.nowhp = enemychar.nowhp - player_damage
                printdamage(player_damage)
                if enemychar.nowhp <=0:
                    printEnemyHealth(0)
                    time.sleep(2)
                else:
                    printEnemyHealth(enemychar.nowhp)
                    time.sleep(2)
                    playerchar.nowhp = playerchar.nowhp - enemy_damage
                    printEnemydamage(enemy_damage)
                    if playerchar.nowhp <= 0:
                        printHealth(0)
                        time.sleep(2)
                    else:
                        printHealth(playerchar.nowhp)
                        time.sleep(2)
            elif choice == 2:
                defence = int(round(enemy_damage-playerchar.armor))
                if (enemychar.damage - playerchar.armor) <=0:
                    print "You took no damage!"
                    enemychar.nowhp = int(round(enemychar.nowhp - playerchar.armor/2))
                    if enemychar.nowhp <= 0:
                        printEnemyHealth(0)
                        time.sleep(2)
                    else:
                        printdamage(defence)
                        printEnemyHealth(enemychar.nowhp)
                        time.sleep(2)
                else:
                    playerchar.nowhp = playerchar.nowhp - defence
                    print "You defended " + str(playerchar.armor) + " Points of damage!"
                    if playerchar.nowhp <= 0:
                        printHealth(0)
                        printdamage(playerchar.armour/2)
                        time.sleep(2)
                    else:
                        printHealth(playerchar.nowhp)
                        printdamage(playerchar.armour/2)
                        enemychar.nowhp = enemychar.nowhp - playerchar.armor/2
                        printEnemyHealth(enemychar.nowhp)
                        time.sleep(2)
            elif choice == 3:
                runawaychance = random.randint(1,10)
                if runawaychance >5:
                    print "You have fled the battle!"
                    break
                else:
                    playerchar.nowhp = playerchar.nowhp - (enemy_damage + 2)
                    print "You didn't get away!"
                    if playerchar.nowhp <= 0:
                        printEnemydamage(enemy_damage + 2)
                        printHealth(0)
                        time.sleep(2)
                    else:
                        printEnemydamage(enemy_damage + 2)
                        printHealth(playerchar.nowhp)
                        time.sleep(2)
            else:
                print("Please chose an option")
