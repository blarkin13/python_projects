import random

var_health = 10
var_dammage = 1
var_st_dammage = 3
var_heal = 3
var_potion = 1
var_response =  ''
while 1:
    var_un = input('Enter Nickname:')
    if var_un != "":
        break
      
input('It is a cold stormy night...')
input('In the forest lives monsters. The monsters are prepairing to storm the castle.')
input('The castle is doomed and only you can save it')
input(" ")
print("****** LEVEL I ******")
print("**** The Castle *****")
input(" ")
while 1:
    var_response = input('Should the king send his knights to battle the monsters?: ')
    if var_response =='yes':
        break
    
    elif var_response =='no':
        break
    
if var_response != 'no':
    var_health += - 1
    input('All but 3 knights have been defeated they are too strong. Lose 1 health.')
    input('Your health is now ' + str(var_health))
print('The castle is also the home of...')
while 1:
    name = input('Please enter a  wizard name: ')
    if name != "":
        break
input(name + ' is a powerful wizard')
input(name + ' has a potion to restore health...')
if var_health !=10:
   
    input('The potion may increase your health up to 10')
    

    if input('Do you want to use it?: ' ) =='yes':
        var_health = 10
        var_potion += -1
if var_health ==10:
    print(str(var_potion) + ' potions remain, but you are full on health')
else:
    print(str(var_potion) + ' potions remain, but you are near full health')
input('Oh no! the monsters broke through the gate')
x = input('would you like to run to the back exit?: ')
if x == 'no':
    input('You are pinned down')
    var_health += -3
    x=input('Will you try to escape?: ')
    if x=='no':
        input('GAME OVER!!!')
        exit()


while 1:
    r = input('Would you like to evacuate the castle?: ')

    if r == "yes":

        y=(random.randint(1,3))
        
        if y == '1':
            input("You didn't escape in time!")
            input('The monsters ate you for dinner')
            exit()
        elif y == '2':
            input('You and the wizard escaped! But you tripped over a rock. Lose 1 health')
            var_health += -1
            if var_health < 1:
                input("Wizard " + name + ": I thought that your name was " + var_un + " the brave, not " + var_un - " the clumsy!")
                input("Wizard " + name + ": I will find a potion to turn back time.")
                input("Wizard " + name + ": A time before the monsters entered the castle.")
                input("Wizard " + name + ": Until then...")
                input("Game over")
                exit()
            input("Wizard " + name + ": Your health is: " + str(var_health))
        else:
            input('You and the wizard escaped!')
        break        
    else:

        
           
        y=str((random.randint(1,5)))
        if y == '1':
            var_object = "a barrel of gunpowder."
        elif y == '2':
            var_object = "your mommy."
        elif y == '3':
            var_object = "a trash can."
        elif y == '4':
            var_object = "a skinny pole, really? how would that work?"        
        else:
            var_object = "a cannon"   
        var_health += -2
        input("A monster found you hiding behind " +var_object+ " Luckily, you got a way and only lost 2 health.")
        
        if var_health < 1:

            input("Wizard " + name + ": You were brave " + var_un + "! Luck was not with you on this adventure")
            input("Wizard " + name + ": I will find a potion to turn back time.")
            input("Wizard " + name + ": A time before the monsters entered the castle.")
            input("Wizard " + name + ": Until then...")
            input("Game over")
            exit()
        input("Wizard " + name + ": Your health is: " + str(var_health))
       
        
input(" ")                     
print("****** LEVEL II ******")
print("** The Dark Forest ***")
input(" ")
x=input("Wizard " + name + ": What would you like to do now?: ")
if x =='burn the castle':
    input("You are a bad ass!")
    print("Game Over")
    exit()
else:
    input("Wizard " + name + ": " + x +"? Ok, how about we look for supplies instead?")
y=str((random.randint(1,3)))
if y == '1':
    input("Wizard " + name + ": You found a wizard lightning potion")
    weapon ='wizard lightning'
elif y == '2':
    input("Wizard " + name + ": You found a flame sword")
    weapon ='a flame sword'
else:
    input("Wizard " + name + ": You found a gernade!")
    weapon ='a grenade'
input("..")
input("...")
monsters_outside = 5
input("The monsters are chasing you!")
x=input("Should you hide? or attack with " + weapon +"?: ")
if x== 'hide':
    print("RUMBLE! RUMBLE! RUMBLE! ... you're safe, but lost 2 health hiding in thorn bushes!")
    var_health += -2
    if var_health < 1:
        input("Wizard " + name + ": You were brave " + var_un + "! Luck was not with you on this adventure")
        input("Wizard " + name + ": I will find a potion to turn back time.")
        input("Wizard " + name + ": A time before the monsters entered the castle.")
        input("Wizard " + name + ": Until then...")
        input("Game over")
        exit()
    input("Wizard " + name + ": Your health is: " + str(var_health))
elif x == 'attack':
    input ('your attack killed two out of five monsters and lost one health')
    monsters_outside = 3
    var_health += -1
    if var_health < 1:
        input("Wizard " + name + ": You were brave " + var_un + "! Luck was not with you on this adventure")
        input("Wizard " + name + ": I will find a potion to turn back time.")
        input("Wizard " + name + ": A time before the monsters entered the castle.")
        input("Wizard " + name + ": Until then...")
        input("Game over")
        exit()
    input("Wizard " + name + ": Your health is: " + str(var_health))

    
else:
    x = input("Please type hide or attack")
    input("Too late...")
    input("You didn't react quick enough")
    input("The monsters ate you for Dinner")
    print("Game Over")
    exit()


input("Wizard " +name+": We are both still alive...")
input(var_un+": YEAH, it was close though.")
input("Wizard " +name+": so true...")
input(var_un+": I wonder whats going on inside the castle")       
input("Wizard " +name+": We can check my crystal ball!")
input(var_un+": OK, let's check!")
input("..")    
input("Wizard " +name+": I see the castle...")
input("..")
input("Wizard " +name+": I see the king is trapped in his throne room.")
input("..")
input("King: Where is that kid " + var_un + " and that wizard " + name +"?")
input("King: I could really use thier help  right now!")
input("..")
input("Back in the cold stormy forrest...")
input(var_un +  ": lets get back to the to the castle to fight some monsters!")
input("Wizard " + name + ": Sure, but first we need to look for some supplies to fight these monsters out here")
input(" ")                     
print("****** LEVEL II ******")
print("** The Dark Forest 2 *")
input(" ")

if x =='attack':
    weapons = 0
else:
    weapons = 1
input("wizard " +name+": We have " + str(weapons) + " weapon(s).")
r ="yes"
backpack = ["","","" ]

while r != "no":
    r = input("Wizard " + name +": Do you want to search for more items? If we find Mandrake Root, Moleyarrow, and Nostrix, I can make a potion to defeat the monsters out here: ")
    if r == 'no':
        break
    
    items_list = ["an apple! They are delicious, they only give you ", "a radish! Although they are small, they still give you ", " a suit of armor! This will give you ", "a monster hide! This will give you ", "a monsters empty nest! At least you can move on and lose ", "a poison berry, Yuck! lose ", "oh no! a cave with monsters, you lose " , "a thorn bush, ouch! That took away ","Mandrake ","Moleyarrow ","Nostrix "]
    y=str((random.randint(0,10)))
    if y == '0':
        bonus = 1
    elif y == '1':
        bonus = 1
    elif y == '2':
        bonus = 3
    elif y == '3':
        bonus = 2
    elif y == '4':
        bonus = 0
    elif y == '5':
        bonus = -2
    elif y == '6':
        bonus = -4
    elif y == '7':
        bonus = -1     
    elif y == '8':
        bonus = 0  
        backpack[0]="Mandrake"
    elif y == '9':
        bonus = 0
        backpack[1]="Moleyarrow"  
    elif y == '10':
        bonus = 0
        backpack[2]="Nostrix"                                            
    input("You found: " + str(items_list[int(y)]) + "" + str(bonus)+ " health bonus.")
    var_health = var_health + bonus
    if var_health < 1:
        input("Wizard " + name + ": I thought that your name was " + var_un+ ", not Icarus!")
        input("Wizard " + name + ": I will find a potion to turn back time.")
        input("Wizard " + name + ": A time before the monsters entered the castle.")
        input("Wizard " + name + ": Until then...")
        input("Game over")
        exit()
    input("Wizard " + name + ": Your health is: " + str(var_health))
    if all(x in backpack for x in ['Mandrake', 'Moleyarrow', 'Nostrix']) == True:
        input("Wizard " + name + ": We have all items needed to create our potion.")
        r2 = input("Wizard " + name + " Do you want to spend 2 health to cast the spell?: ")
        if r2 == "yes":
            var_health += -2
            if var_health < 1:
                input("Wizard " + name + ": You were brave " + var_un + "! You didn't have enough health to cast that spell.")
            else:
                input("Wizard " + name + ": Lorem ipstum")
                input("Wizard " + name + ": Lorem ipstum dolor sit")
                input("Wizard " + name + ": Lorem ipstum dolor sit amet!")
                input(".")
                input("..")
                input("...")
                backpack[0]=""
                backpack[1]=""
                backpack[2]=""              
                x2 = str((random.randint(0,5)))
                if x2 in ('2','4'):
                    input("Wizard " + name + ": That didn't work properly. We must continue to search.")
                    
 
                else:
                    input("All monster outside of the castle are now defeated!")
                    monsters_outside = 0
                    break

    x3 = input("Wizard " + name + ": Do you want to see what's in your backpack?")
    if x3 == 'yes':
        for items in backpack:
            print(items)

input("Wizard " + name + ": There are " + str(monsters_outside) + " monsters out here. ")     
input( var_un + ": Let's hurry back to the castle to save everyone else!")     
if monsters_outside > 0:
    input("Wizard " + name + ": I don't see us making it back to the castle with out defeating the monsters first.")
    input( var_un + ": I'm not scared!") 
    input( var_un + ": The " + str(monsters_outside) + " monsters can be dealt with later!") 
    input("Wizard " + name + ": The chance of us both making it back to the castle is 1 and 5.")
    while 1:
        r = input("Wizard " + name + ": Do you want to risk it?")
        if r == 'yes':
            y=str((random.randint(0,5)))
            if y != '4':
                input(".")
                input("..")
                input("...")
                input("Wizard " + name + ": You were brave " + var_un + "!")
                input("Wizard " + name + ": I will find a potion to turn back time.")
                input("Wizard " + name + ": A time before the monsters entered the castle.")
                input("Wizard " + name + ": Until then...")
                input("Game over")
                exit()
            break        
        elif r == 'no':
            input("** LEVEL III episode **")
            print("** The long way home **")
            input("")
            input("this needs to be filled out with a new quest")   
            exit()
            break
    
                 
if monsters_outside >0:
    input(" ")
    print("****** LEVEL II episode ******")
    print("** It's good to be lucky **")
    input("")


input(" ")
print("****** LEVEL III ******")
print("* The quick way back *")
input("")

input ("Headed back to the castle with 0 monsters chasing you!")
exit()






