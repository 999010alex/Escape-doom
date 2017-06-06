# Escape-doom
#A final project for 12th grade computer science 
print("Welcome to Escape doom!")
print("You are a spy for the CIA and you got caught by Herozitovian terrorists!")
print("You manage to steal food from their kitchen, consisting of: one pizza, one taco, one sandwich, and one hot pocket. You also have one 2 liter bottle of water.")
print("Survive the escape and outrun the terrorists!")
done = False
you=20
terrorists=0
hunger=100
thirst=100
ingredient = 'chicken parm'

def mix_and_cook():
    print("Flatten out dough")
    print("put tomato sauce on dough")
    print("put cheese and ingredients on dough")
    print("put pizza in oven")
    print("take pizza out of oven in 20 minutes")
def make_pizza(ingredient):
    print("How to make an pizza:")
    mix_and_cook()
    pizza = 'a {} pizza!'.format(ingredient)
    return pizza
def mix_and_cook2():
    print("Grill meat and cheese")
    print("Put meat and cheese in taco shell")
    print("Put rice and beans in taco shell")
    print("put lettuce and tomatoes in taco shell")
    print("put sour cream and guacamole in taco shell")
def make_taco(ingredient):
    print("How to make a taco!")
    mix_and_cook2()
    taco = 'a {} taco!'.format(ingredient)
    return taco
def mix_and_cook3():
    print("Put mustard or mayo and cheese on bread")
    print("Put meat on bread")
    print("toast sandwhich")
    print("put lettuce and tomatoes on bread")
def make_sandwich(ingredient):
    print("How to make a sandwich!")
    mix_and_cook3()
    sandwich = 'a {} sandwich!'.format(ingredient)
    return sandwich
def mix_and_cook4():
    print("take hot pocket out of package")
    print("put hot pocket in conviently nearby microwave")
    print("cook for 3 minutes")
def make_hot_pocket(ingredient):
    print("How to make a hot pocket!")
    mix_and_cook4()
    hot_pocket = 'a {} hot pocket!'.format(ingredient)
    return hot_pocket
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
        print("You drank water, your thirst goes down but the terrorists are getting closer.")
        you=you+5
        terrorists=terrorists+23
        hunger=hunger+5
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
            print(make_pizza(ingredient))
            you=you+25
            terrorists=terrorists+18
            hunger=hunger+25
            thirst=thirst+5

        elif choice == "b" or choice == "B":
            print(make_taco(ingredient))
            you=you+5
            terrorists=terrorists+23
            hunger=hunger+20
            thirst=thirst+20
        elif choice == "c" or choice == "C":
            print("Which meal shall you eat?")
            print(make_sandwich(ingredient))
            you=you+1
            terrorists=terrorists+20
            hunger=hunger+15
            thirst=thirst+5
        elif choice == "d" or choice == "D":
            print(make_hot_pocket(ingredient))
            you=you+1
            terrorists=terrorists+20
            hunger=hunger+10
            thirst=thirst+5
        else:
            print("you have a wrong input")
    elif choice == "d" or choice == "D":
        print("You run 15 miles, but you get more thirsty, and you get hungrier.")
        you=you+15
        terrorists=terrorists+20
        hunger=hunger-15
        thirst=thirst-20
    elif choice == "e" or choice == "E":
        print("You are ", you ," miles out of 200 miles.")
        print("The terrorists are ", you-terrorists , "miles away from you")
        print("Your hunger level is ", hunger ,"energy out of 100.")
        print("You are ", thirst, " thirst out of 100.")
    else:
        print("You have a wrong input")


#trademark Alex Castillo
