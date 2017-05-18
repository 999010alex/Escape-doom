# Escape-doom
A final project for 12th grade computer science 
print("Welcome to Escape doom!")
print("You are a spy for the CIA and you got caught by Herozitovian terrorists!")
print("You manage to steal food from their kitchen, consisting of: one pizza, one taco, one sandwich, and one hot pocket. You also have one 2 liter bottle of water.")
print("Survive the escape and outrun the terrorists!")
done = False
you=20
terrorists=0
hunger=100
thirst=100
if done == True:
    print("You have finished the game, ethier you've died, or you made it out of Herozitovia. Restart to play again.")
while done == False:
    if you >= 200:
        print("You have won the game! You have made it out of the terrorist hideout! Congrats!")
        done=True
        break
    if terrorists >= you:
        print("The terrorist have caught up to you, and you are DEAD.")
        done=True
        break
    if hunger == 0:
        print("Your stomache grumbles as you pass out from hunger, the terrorists catch up to you, YOU ARE DEAD.")
        done=True
        break
    if thirst == 0:
        print("You have DIED of dehydration. Better luck next time!")
        done=True
        break
    print("The desert seems endless, what will you do?")
    print("A. Run at full speed")
    print("B. Drink some water")
    print("C. Eat one of your meals")
    print("D. Jog at a steady speed")
    print("E. Check in on your hunger and thirst, and use your GPS")
    choice=input('Your choice: ')
    if choice == "A" or choice == "a":
        print("You run 25 miles. Your have gotten hungrier, and you're slightly more thirsty.")
        you=you+25
        terrorists=terrorists+18
        hunger=hunger-20
        thirst=thirst-20

    elif choice == "b" or choice == "B":
        print("You drank water, your thirst goes down but the natives are getting closer.")
        you=you+5
        natives=natives+23
        camel=camel+5
        thirst=thirst+20
    elif choice == "c" or choice == "C":
        print("Which meal shall you eat?")
        print("A. Pizza")
        print("B. Taco")
        print("C. Sandwich")
        print("D. Hot Pocket")
        choice=input('Your choice: ')
        if choice == "A" or choice == "a":
            print("You unbox to pizza to find it uncooked, luckily, there happens to be a pizza oven nearby.")
            
            you=you+25
            terrorists=terrorists+18
            hunger=hunger-20
            thirst=thirst-20

        elif choice == "b" or choice == "B":
            print("You drank water, your thirst goes down but the terrorists are getting closer.")
            you=you+5
            terrorists=terrorists+23
            hunger=hunger+5
            thirst=thirst+20
        elif choice == "c" or choice == "C":
            print("Which meal shall you eat?")
            you=you+1
            terrorists=terrorists+20
            hunger=hunger+25
            thirst=thirst+5
        elif choice == "d" or choice == "D":
            you=you+1
            terrorists=terrorists+20
            hunger=hunger+25
            thirst=thirst+5
    elif choice == "d" or choice == "D":
        print("You ride 15 miles, but you get more thirsty, and your camel loses energy.")
        you=you+15
        natives=natives+20
        camel=camel-15
        thirst=thirst-20
    elif choice == "e" or choice == "E":
        print("You are ", you ," miles out of 200 miles.")
        print("The natives are ", you-natives , "miles away from you")
        print("The camel has ", camel ,"energy out of 100.")
        print("You are ", thirst, " thirst out of 100.")
    else:
        print("You have a wrong input")
