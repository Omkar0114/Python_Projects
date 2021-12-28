print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("welcome to Treasure Island Game !!")
print("Your mission is to find the treasure !!")

choice1 = input('you\'re on the cross word. There are two roads where do you want to go "left" or "right"').lower()

if choice1 == "left":
    choice2 = input('Congo! Now you are on the lake. what do you want to do, "swim" or "wait" ')
    if choice2 == "wait":
        choice3 = input('Now you\'ve 3 doors in front of you. which you want to open "Red" or "yellow" or "blue" ')
        if choice3 == "yellow":
            print("Congratulations ! YOu win !!")
        elif choice3 == "blue":
            print("eaten by beast .......Game Over" )
        elif choice3 == "Red":
            print("You're Burned by fire Game over !!")
        else:
            print("Game Over!!")
    else:
        print("You are attacked by trout !\n GAME OVER ! ")
else:
    print("You fall into a hole\n GAME OVER!!")