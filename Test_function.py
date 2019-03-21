import random
from random import randint

monsters_outside = 1
var_health = 10
var_monster_health = 30
var_lives = 3
var_potion = 1
var_un = "bobo"
name = "Chaps"
var_wizard_side = 0
var_warlock_side = 0 
backpack_list = ""
import numpy as np
def lowercase(x):
    x =x.lower()
    return x


def escape_the_castle(var_health,var_potion,var_wizard_side,var_warlock_side):

    
      
    print('It is a cold stormy night...')
    print('In the forest lives monsters. The monsters are prepairing to storm the castle.')
    print('The castle is doomed and only you can save it')

    input("Press enter to continue... ")
    print("****** LEVEL I ******")
    print("**** The Castle *****")
    input("Press enter to continue... ")


    while 1:
        print("You will need a username to continue.")
        print("Enter your username: ")
        var_un = input(' ')
        if var_un != "":
            print("Your username is set to " + var_un + ".")
            break
    while 1:
        print("Should the king send his knights to battle the monsters?: yes or no")
        var_response = input(' ')
        if var_response =='yes':
            var_warlock_side += 1
            break
        
        elif var_response =='no':
            var_wizard_side += 1
            break
        
    if var_response != 'no':
        var_health += -1
        input('All but 3 knights have been defeated they are too strong. Lose 1 health.')
        input('Your health is now ' + str(var_health))
    print('The castle is also the home of a powerful wizard.')
    
    while 1:
        print("Please enter a  wizard name: ")
        name = input(' ')
        if name != "":
            break
    input(name + ' is a powerful wizard')
    
    if var_health !=10:
        input(name + ' has a potion to restore health...')
       
        input('The potion may increase your health up to 10')
        
        print("Do you want to use it?: yes or no")
        if input(' ' ) =='yes':
            var_health = 10
            var_potion += -1
    
    input('Oh no! the monsters broke through the gate')
    print("Would you like to run to the back exit?: yes or no")
    x = input(' ')
    if x == 'no':
        input('You are pinned down')
        var_health += -3
        print("Will you try to escape?: yes or no")
        x=input('Will you try to escape?: ')
        if x=='no':
            input('GAME OVER!!!')
            exit()
    
    
    while 1:
        print("Would you like to evacuate the castle?: yes or no")
        r = input('')
    
        if r == "yes":
    
            y=(random.randint(1,3))
            
            if y == 1:
                input("You didn't escape in time!")
                input('The monsters ate you for dinner')
                exit()
            elif y == 2:
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
    return (var_un, name, var_health,var_wizard_side,var_warlock_side)
def dark_forest(var_health, var_monster_health, var_lives, monsters_outside, var_un, name,var_wizard_side,var_warlock_side):#(var_health, var_monster_health, var_lives, monsters_outside,var_un, name)
    input("Press enter to continue... ")
    print("****** LEVEL II ******")
    print("** The Dark Forest ***")

    input(" ")
    print("Wizard " + name + ": What would you like to do now?: ")
    x=input(" ")
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
    while 1:

        print("Should you hide or attack with " + weapon +"?: hide or attack")
        x=input(" ")
        if x== 'hide':
            var_warlock_side += 1
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
            break
        elif x == 'attack':
            input ('Your attack killed two out of five monsters and lost one health')
            monsters_outside = 3
            var_health += -1
            if var_health < 1:
                var_wizard_side += 1
                input("Wizard " + name + ": You were brave " + var_un + "! Luck was not with you on this adventure")
                input("Wizard " + name + ": I will find a potion to turn back time.")
                input("Wizard " + name + ": A time before the monsters entered the castle.")
                input("Wizard " + name + ": Until then...")
                input("Game over")
                exit()
            input("Wizard " + name + ": Your health is: " + str(var_health))
            break
        
        
       
    
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
    input("King: I could really use their help  right now!")
    input("..")
    input("Back in the cold stormy forest...")
    input(var_un +  ": lets get back to the castle to fight some monsters!")
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
        print("Wizard " + name +": If we find Mandrake Root, Moleyarrow, and Nostrix, ")
        print("        I can make a potion to defeat the monsters out here.")
        print("Wizard " + name +": Do you want to search for more items?: press enter to search or no to quit")
        r = input(" ")
        if r == 'no':
            var_warlock_side += 1
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
                        var_wizard_side += 1
                        break
        print("Wizard " + name + ": Do you want to see what's in your backpack?: yes or press enter ")
        x3 = input(" ")
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
            r = input("Wizard " + name + ": Do you want to risk it? yes or exit: ")
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
            elif r == 'exit':
                y = input("** Are you sure? yes or no: **")
                if y == "yes":
                    exit()
                    break
        
                     
       
    
    input(" ")
    print("****** LEVEL III ******")
    print(" ** The journey back **")
    input("")
    
    input ("Headed back to the castle with "+str(monsters_outside)+" monsters chasing you!")
    
    return(var_health, var_monster_health, var_lives, monsters_outside,var_un, name,var_wizard_side,var_warlock_side)
    



def searching_for_supplies(var_un, name,var_health, var_monster_health, var_lives, monsters_outside,var_wizard_side,var_warlock_side):
    input("Wizard " + name + ": You have shown some great strength out here.")
    input("Wizard " + name + ": You are on the right path.")
    input( var_un + ": Thanks?")
    input("Wizard " + name + ": " + var_un + ", I believe that you have what it takes to be a great warrior. ")
    input("Wizard " + name + ": To succeed, you will need to stay on this road. ")
    input( var_un + ": What?")
    input("Wizard " + name + ": You will need to stay on this road to find your way to the battle swamp.")
    print(" There you may be able to find items to help us back at the castle. ")
    input("Wizard " + name + ": I will be on my own journey. ")
    input("Wizard " + name + ": I must find out why the monsters have come back! ")
    input( var_un + ": Come back?")
    input( var_un + ": Are you telling me that this has happened before?")
    input("Wizard " + name + ": Years ago... ")
    input("Wizard " + name + ": Wizards, Witches, and Warlocks battled. ")
    input("Wizard " + name + ": They battled in the swamp.")
    input("Wizard " + name + ": The king had just died and the Witches decided that they would take over the throne. ")
    input("Wizard " + name + ": They made an aliance with the Warlocks. ")
    input("Wizard " + name + ": They were to work together to take over the throne and live without non-magical beings. ")
    input( var_un + ": How were they going to do that?")
    input("Wizard " + name + ": The Witches cast a spell on the non-magical beings. Convincing them that... ")
    input("Wizard " + name + ": The Warlocks were behind the kings death and that they should battle them in the swamps graveyard. ")
    input("Wizard " + name + ": The non-magical beings got so upset and they whent to the swamp to find the Warlocks, but ... ")
    input("Wizard " + name + ": the Warlocks plan was to cast a rise from the ground spell in the grave yard...")
    input("Wizard " + name + ": They turned the dead into monsters.")
    input("Wizard " + name + ": A group of Wizards found out what was happening and reversed the spell that the Witches cast.")
    input("Wizard " + name + ": The non-magical beings ran back to the castle before they lost too many knights.")
    input("Wizard " + name + ": When the Witches found out what had happened at the graveyard...")
    input("Wizard " + name + ": they blammed the Warlocks for not getting their monsters to attack quick enough.")
    input("Wizard " + name + ": The Warlocks blammed the Witches of casting weak spells.")
    input( var_un + ": Seems like they both suck!")
    input("Wizard " + name + ": No, The Warlocks were powerful, the Witches ruined everything.")
    input("Wizard " + name + ": It wasn't the spells, it was the plan that failed them.")
    input("Wizard " + name + ": The Witches and Warlocks battled for years after.")
    input("Wizard " + name + ": The battle lasted until the Wizards stepped in to defeat the monsters and cast all of the witches and Warlocks ...")
    input("Wizard " + name + ": to a different realm.")
    input( var_un + ": So there aren't witches or warlocks here anymore?")
    input("Wizard " + name + ": That's what I'm going to find out.")
    input("Wizard " + name + ": I will meet you at pass by the edge of the forest and the swamp.")
    input( var_un + ": See ya later.")
    input(".")
    input("..")
    input("...")


    print("****** LEVEL III ******")
    print("**** The Battle Swamp *****")
    input("Press enter to continue... ")


    input( var_un + ": This place is creepy.")
    input( "Swamp Noises?: kiiick chiiick... kih kih ...")
    input( var_un + ": What was that?")
    input(".")
    input("..")
    input("...")
    input( "Swamp Noises?: kiiick... chiiick... kih kih kih chih chih chih chiiiick!")
    input(".")
    input("..")
    input("...")
    input( var_un + ": I just need to ignore that, and find some weapons.")
    r=""
    z=0
    c=0
    g=0
    
    while z<2:
        input( var_un + ": Ok, there is a cave to the right and a swampy graveyeard to the left.")
        print( var_un + ": Should I search the cave or the graveyard?: cave or graveyard")
        r= input(" ")
        if r =="cave":
            if c==0:
                input( var_un + ": Oh, I see a rusty sword at the enterence, ") 
                print( "but that cave itself is small and nothing else is in there")
                z += 1
                c+=1
            else:
                input( var_un + ": I already checked the cave!") 


        elif r=="graveyard":
            if g==0:
                input( var_un + ": Oh, I see a lance at the enterence of the graveyard.")
                if c == 0:
                    print( var_un + ": I'd rather check the cave before I enter the graveyard.")
                z += 1
                g+=1
            else:
                print( var_un + ": I already checked the enterence")
    
    input( var_un + ": Let's see whats in the backpack.")
    print("|| " + "rusty sword" + " || " + "Missing" + " || " + "lance" + "  || " + "Missing" + " || " )            
    input( "Swamp Noises?: kiiick chiiick... kih kih ...")
    input( var_un + ": Not that again.")
    input(".")
    input("..")
    input("...")
    input( "Swamp Noises?: kiiick... chiiick... kih kih kih chih chih chih chiiiick!")
    input(".")
    input("..")
    input("...")
    input( "Female voice: Who are you?")
    input(".")
    input("..")
    input( "Female voice: Hurry up and answer me!")
    input( var_un + ": I am just a traveler, looking for supplies to rid this area of the monsters.")
    input( var_un + ": Who are you?")
    input( "Female voice: I protect this graveyard from scavengers.")
    input( "Female voice: This graveyard is a sacred place.")
    input( "Female voice: I sense that you are not just a lone traveler!")
    input( var_un + ": I was with my friend.")
    input( var_un + ": We split up before I entered the swamp.") 
    input( "Female voice: This is not just a swamp. This is called the 'Battle Swamp' for a reason!")
    input( "Female voice: A long time ago...")
    input( var_un + ": I already heard this story.")
    input( var_un + ": My friend is a wizard and he told me.")
    input( var_un + ": He told me about the witches and warlocks trying to take over the castle")
    print( "and how they battled each other when it didn't work.")
    input( "Female voice: Your wizard friend is wrong.")
    print( "Female voice: The witches did not try to take over the castle.")
    print( "The witches came here to protect the area from the darkness.")
    print( "The warlocks were never able to get to the castle, because the witches were able to stop them;")
    print( "that is until the wizards stepped in. The warlocks cast a spell on the wizards.")
    print( "a spell that made them believe that the witches casted a spell on the people of the castle.")
    input( var_un + ": How do you know this?")
    input( "Female voice: I have been here longer than the castle.")
    print( "I have protected this land from the darkness.")
    print( "I will stay here until the darkness is gone.")
    input( var_un + ": Darkness?")
    input( "Female voice: 'The Darkness' is the energy that comes from having evil warlocks in the area.")
    input( var_un + ": I thought that the wizards got rid of all of the witches and warlocks.")
    input( "Female voice: That was part of the spell that the warlock casted on the wizards.")
    input( "Female voice: To make them believe that they were able to send all of the warlocks to a different realm.")
    print( "A few of us witches and evidently at least one warlock are still here.")
    print( "When the wizards thought that we were all gone.")
    print( "They left this area because they thought that all evil was gone.")
    input( var_un + ": You are a witch?")
    input( "Gwenda: I am the Witch of truth. ")
    input( var_un + ": 'Evidently at least one warlock'?")
    input( "Gwenda: Monsters are back in the area!")
    input( var_un + ": Oh, yeah, good point.")
    input( "Gwenda: I sense that you are capable of helping me get rid of the monsters.")
    input( "Gwenda: In this graveyard there are tools that you will need.")
    input( "Gwenda: If you are able to find your way through the graveyard,")
    print( "you will find six items.")
    input( "Gwenda: Walk through the enterence and i will meet you by the exit on the north wall.")
    input("Press enter to continue... ")
    print("****** LEVEL IV ******")
    print("****** The Maze ******")
    input("Press enter to continue... ")
    




def maze():
  location_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56)
  wall_list = (1, 2, 4, 5, 6, 7, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 51, 52, 53, 54, 55, 56)

    
  north_wall_list = (51,52,53,54,55)
  east_wall_list = (16,24,32,40,48,56)
  south_wall_list= (2,4,5,6,7)
  west_wall_list = (1,9,17,25,33,41,49)
  tree_list = (27,31,45)
  grave_list = (10,13,34,46)
  wet_area_list = (15,18,30,42,47)
  
  
  inside_list = np.setdiff1d(location_list,wall_list, assume_unique=True)
  tomb_list = (19,20,22,23,26,28,38,43)
                  #  ||Rusty Sword || Missing || Iron sword || Dagger || Amulet of life 2 of 3 || Amulet of Unknown ||
  backpack_list = ['Rusty Sword' , 'Missing', 'Lance', 'Missing', 'Missing', 'Missing']

  x = 19
  #if x in location_list:
  # print(location_list)
  location = 3
  new_location = 0
  response = ""
  amulet_of_life1 = 1
  amulet_of_life2 = 1
  amulet_of_life3 = 1
  iron = 1
  dagger = 1
  amulet_of_de = 1
  items = 6
  search = ""
  while response != 'exit':
    missing_items =  amulet_of_life1 + amulet_of_life2 + amulet_of_life3  + iron + dagger + amulet_of_de
    print("------------------------------------Choose a direction------------------------------------")
    response = input("|| North = 8 || East = 6 || South = 2 || West = 4 || bp = Backpack contents || ")
   
    response = lowercase(response)
    if response == "bp":
        s = (str(backpack_list)[1:-1])
        s = s.replace("', ", " || ")
        s = s.replace("'", "")
        s="||" + s + " ||"
        bp = "backpack contents"
        string3=s
        string_length=len(string3)   # will be adding 10 extra spaces
        string_revised=bp.center(string_length)

        print(string_revised)
        print(s)
        

    elif response in ('2','4','6','8'):
        if int(response) ==8:
            print("moving north")
            new_location = location + 8
        elif int(response) ==6:
            print("moving east")
            new_location = location + 1
        elif int(response) ==2:
            print("moving south")
            new_location = location - 8
        elif int(response) == 4:
            print("moving west")
            new_location = location - 1
        
        if new_location in north_wall_list:
            print("You found the North wall and can't go this way!")
        elif new_location in east_wall_list:
            print("You found the East wall and can't go this way!")
        elif new_location in south_wall_list:
            print("You found the South wall and can't go this way!")
        elif new_location in west_wall_list:
            print("You found the West wall and can't go this way!")
        elif new_location in tomb_list:
            print("You found a tomb and can't go this way!")

        elif new_location in tree_list:
            print("You found a tree!")
            while 1:
                search = input("Do you want to search it?: ")
                search = lowercase(search)
                if search == "no":
                    location = new_location
                    #new_location = 0
                    break
                elif search =="yes":

                    if new_location == 27:
                        location = new_location
                        #ew_location = 0
                        if amulet_of_de == 1:
                            amulet_of_de = 0
                            backpack_list[5] = "Amulet of Unknown"
                            print("     ___________________")
                            print("    |                   |")
                            print("    |         _         |")
                            print("    |         |         |")
                            print("    |         |         |")
                            print("    |   <----{O}---->   |")
                            print("    |         |         |")
                            print("    |         |         |")
                            print("    |___________________|")
                            print("You found the 'Amulet of unknown'!")
                            
                        boa=input("Would you like to read the back of it?: ")
                        boa = lowercase(boa)
                        if boa=="yes":
                            print("     ___________________")
                            print("    |                   |")
                            print("    |   When you find   |")
                            print("    |  that you are in  |")
                            print("    |  trouble, repeat  |")
                            print("    |    These words    |")
                            print("    |  sudo apt get do  |")
                            print("    |       break       |")
                            print("    |___________________|")

                        else:
                            print("Nothing")
                            
                    elif new_location == 31:
                        if dagger == 1:
                            dagger =0
                            backpack_list[3] = "Dagger"
                            print("You found the an old dagger!")
                            location = new_location
                            #new_location = 0
                        else:
                            print("Nothing")
                            location = new_location
                            #new_location = 0
                    else:
                        print("Nothing")
                        location = new_location
                        #new_location = 0            
                break






        elif new_location in grave_list:
            print("You found a grave!")
            while 1:
                search = input("Do you want to search it?: ")
                search = lowercase(search)
                if search == "no":
                    location = new_location
                    new_location = 0
                    break
                elif search =="yes":
                    
                    if new_location == 10:
                        
                        if amulet_of_life1 == 1:
                            amulet_of_life1 = 0
                            print("        ___________________")
                            print("       /__________________/|")
                            print("      |                  | |")
                            print("      |     Here lies    | |")
                            print("      |                  | |")
                            print("  |   |  Vasl Nemsicoff  | |")
                            print("  |   |                  | |")
                            print("  ^   |   -Power comes-  | |")
                            print("{'O'} |   to those with  | |")
                            print("      |     patience.    | |")
                            print("      |                  | |")
                            print("  ~~~ |                  | |~~~~")
                            print("  ~~~ |                  | |~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                            print("You found the 'Amulet of life'!")
                            backpack_list[4] = 'Amulet of life ' +str(3 - amulet_of_life1-amulet_of_life2-amulet_of_life3) + ' of 3'
                            location = new_location
                            new_location = 0
                        else:
                            print("        ___________________")
                            print("       /__________________/|")
                            print("      |                  | |")
                            print("      |     Here lies    | |")
                            print("      |                  | |")
                            print("      |     XEXXXXXX     | |")
                            print("      |     XOTOOOOX     | |")
                            print("      |     XOOOOTTX     | |")
                            print("      |     XTOTOOOX     | |")
                            print("      |     XOTTOTTX     | |")
                            print("      |     XOOOOOOX     | |")
                            print("  ~~~ |     XXEXXXXX     | |~~~~")
                            print("  ~~~ |                  | |~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                            print("Nothing, but an unmarked headstone?")
                            location = new_location
                            new_location = 0
                    elif new_location == 13:
                        
                        if amulet_of_life2 == 1:
                            amulet_of_life2 =0
                            print("        ___________________")
                            print("       /__________________/|")
                            print("      |                  | |")
                            print("      |     Here lies    | |  |   ")
                            print("      |                  | |  |   ")
                            print("      |    Gren Taspin   | |  ^   ")
                            print("      |                  | |{'O'} ")
                            print("      | -Patience comes- | |")
                            print("      |   to those with  | |")
                            print("      |   a clear mind.  | |")
                            print("      |                  | |")
                            print("  ~~~~|                  | |~~~~")
                            print("  ~~~ |                  | |~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                            print("You found the 'Amulet of life'!")
                            backpack_list[4] = 'Amulet of life ' +str(3 - amulet_of_life1-amulet_of_life2-amulet_of_life3) + ' of 3'
                            location = new_location
                            new_location = 0
                        else:
                            print("        ___________________")
                            print("       /__________________/|")
                            print("      |                  | |")
                            print("      |     Here lies    | |")
                            print("      |                  | |")
                            print("      | 4950515253545556 | |")
                            print("      | 4142434445464748 | |")
                            print("      | 3334353637383940 | |")
                            print("      | 2526272829303132 | |")
                            print("      | 1718192021222324 | |")
                            print("      | 0910111213141516 | |")
                            print("  ~~~ | 0102030405060708 | |~~~~")
                            print("  ~~~ |                  | |~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                            print("Nothing, but an unmarked headstone!")
                            location = new_location
                            new_location = 0
                    else:
                        print("        ___________________")
                        print("       /__________________/|")
                        print("      |                  | |")
                        print("      |     Here lies    | |")
                        print("      |                  | |")
                        print("      |                  | |")
                        print("      |                  | |")
                        print("      |                  | |")
                        print("      |                  | |")
                        print("      |                  | |")
                        print("      |                  | |")
                        print("  ~~~~|                  | |~~~~")
                        print("  ~~~ |                  | |~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                        print("Nothing, but an unmarked headstone!")
                        location = new_location
                        new_location = 0            
                break
                    
        elif new_location in wet_area_list:
            print("You found a watery grave!")
            while 1:
                search = input("Do you want to search it?: ")
                search = lowercase(search)
                if search == "no":
                    location = new_location
                    new_location = 0
                    break
                elif search =="yes":
                    
                    if new_location == 42:
                        if amulet_of_life3 ==1:
                            amulet_of_life3 = 0
                            print("You found the 'Amulet of life'!")
                            backpack_list[4] = 'Amulet of life ' +str(3 - amulet_of_life1-amulet_of_life2-amulet_of_life3) + ' of 3'
                            location = new_location
                            new_location = 0
                        else:
                            print("Nothing")
                            location = new_location
                            new_location = 0    
                    elif new_location == 47:
                        if iron ==1:
                            iron = 0
                            print("You found an iron sword!")
                            backpack_list[1] = "Iron sword"
                            location = new_location
                            new_location = 0
                        else:
                            print("Nothing")
                            location = new_location
                            new_location = 0    
                    else:
                        print("Nothing")
                        location = new_location
                        new_location = 0                    
                                

                break       


        elif new_location == 58:
            if missing_items > 0:
                print("You found the exit and can't go this way yet! You are still missing some items")
            else:
                print("You found the exit!")    
                break           
        
        elif new_location == -5:
            print("You found the enterance and can't go this way!")         

        else:
            location = new_location
            new_location = 0

        #print(location)

    print("Your current location is: " + str(location))
    
    
    if response not in ('2','4','6','8','bp','exit'):
        print("Invalid response, no movement was taken.")   


  return(backpack_list)



def attack(weapon):
    
    print(weapon)
    random_hits = randint(0, 3)
    random_crit_damage=randint(1, 5)
    random_return_damage =randint(1, 8)
    random_return_health =randint(1, 8)
    random_return_movement =randint(1, 8)
    return_damage = 0

    if str(random_crit_damage) in ('2','4'):
        random_crit_damage = 2
    else:
        random_crit_damage = 1


    if str(random_return_health) in ('2','4'):
        return_health = 2
    elif str(random_return_health) in ('2','4', '6'):
        return_health = 1
    else:
        return_health = 0

    var_hit_damage = 0
    random_hits = 0
    if weapon == "silver sword":
        var_hit_damage = 2
        random_hits = randint(0, 4)
        if  str(random_return_damage) in ('2', '4', '6', '8'):
            return_damage = 4
    elif weapon == "iron sword":
        var_hit_damage = 3
        random_hits = randint(0, 2)
        if  str(random_return_damage) in ('2', '4', '6'):
            return_damage = 5
    elif weapon == 'lance':
        var_hit_damage = 5
        if  str(random_return_damage) in ('2', '4', '6', '8'):
            return_damage = 4        
        random_hits = randint(0, 1)
    elif weapon == 'dagger':
        var_hit_damage = 1
        random_hits = randint(0, 7)
        if  str(random_return_damage) in ('2', '4', '6', '8'):
            return_damage = 6        
    else:
        print("Weapon not found")
        return_damage = 8
        
    var_total_damage = var_hit_damage * random_hits * random_crit_damage
    print("You struck a total of " + str(random_hits) + " hits with a total damage of " + str(var_total_damage))

    if return_damage > 0:
        print("The monster struck back with  " + str(return_damage) + " damage.")
    if return_health > 0:
        return_health_text = " While hiding you found " + str(return_health) + " health coins."
    else:
        return_health_text = ""
        
    if str(random_return_movement) == '1':
        if return_damage > 0:
            return_movement = "To avoid taking more damage, you dove behind a gravestone." + return_health_text
        else:
            return_movement = "You dove behind a gravestone to avoid taking any damage." + return_health_text
                
    elif str(random_return_movement) == '2':
        if return_damage > 0:
            return_movement = "You crawled behind a creepy old tree to avoid taking more damage." + return_health_text
        else:
            return_movement = "You dove behind a creepy old tree to avoid taking any damage." + return_health_text
        
    elif str(random_return_movement) == '3':
        if return_damage > 0:
            return_movement = "You limped behind a large rock to avoid taking more damage." + return_health_text
        else:
            return_movement = "You side stepped behind a large rock to avoid taking any damage." + return_health_text
    elif str(random_return_movement) == '4':
        if return_damage > 0:
            return_movement = "You rolled into a hole to avoid taking more damage." + return_health_text
        else:
            return_movement = "You dove into a hole rock to avoid taking any damage." + return_health_text
    elif str(random_return_movement) == '5':
        if return_damage > 0:
            return_movement = "You jumped into the water to avoid taking more damage." + return_health_text
        else:
            return_movement = "You dove into the water to avoid taking any damage." + return_health_text
    elif str(random_return_movement) == '6':
        if return_damage > 0:
            return_movement = "To avoid taking anymore damage, you dove behind the monster." + return_health_text
        else:
            return_movement = "You dove behind the monster to avoid taking any damage." + return_health_text
    elif str(random_return_movement) == '7':
        if return_damage > 0:
            return_movement = "To avoid taking anymore damage, you jumped over the monster." + return_health_text
        else:
            return_movement = "You dove over the monster to avoid taking any damage." + return_health_text
    elif str(random_return_movement) == '8':
        if return_damage > 0:
            return_movement = "To avoid taking anymore damage, you attacked the monster again with your lance +5 damage. Then you ran to the closest tree." + return_health_text
            var_total_damage +=5
        else:
            return_movement = "To avoid taking any damage, you attacked the monster again with your lance +5 damage. Then you ran to the closest tree." + return_health_text
            var_total_damage +=5



    return (var_total_damage, random_hits, return_damage, return_health, return_movement)






def battle(var_health, var_monster_health, var_lives, monsters_outside):
 
    weapons_list = ["silver sword", "iron sword", "lance", "dagger"]
    while 1:
        print("|| " + weapons_list[0] + " = 0 || " + weapons_list[1] + " = 1 || " + weapons_list[2] + " = 2 || " + weapons_list[3] + " = 3 || " )
        while 1:
            weapon = input("Weapon?: ") 
            if weapon in ("0","1","2","3"):
                break
    
        int(weapon) + 0
        (var_total_damage, random_hits, return_damage, return_health, return_movement) = attack(str(weapons_list[int(weapon)]))
        var_monster_health += -var_total_damage
        var_health = var_health - return_damage + return_health
        if var_health > 0:
            print(return_movement)
        if var_monster_health < 1:
            input("The monster has been defeated!")
            input("+ 10 health bonus!")
            var_health +=10
            monsters_outside += -1
            if str(monsters_outside) in ("0","2","3","4","5"):
                input(str(monsters_outside) + " monsters remain in the 'Dark Forest'!")
            else:
                input(str(monsters_outside) + " monster remains in the Dark Forest'!")
                    
            break
        if var_health < 1:
            input("The monster was too strong! You lost.")
            var_lives +=-1
            if var_lives > 0:
                input("Using the Amulet of life to regeneate health " + str(var_lives) + " remain")
                input("Health restore to 10")
                var_monster_health +=  randint(10, 25)
                input("The monster regained health up to " + str(var_monster_health) + ".")
    
                var_health = 10
            else:
                input("Game over!")
                exit()    
              
        print("Monster health: " + str(var_monster_health) + " || Your health: " + str(var_health) )
    print(" || Your health: " + str(var_health) +  " ||" )
    return(monsters_outside, var_lives, var_health)
    #exit()










def the_quick_way_back(var_un, name,var_health, var_monster_health, var_lives, monsters_outside ):
    input("")


    




def looking_for_monsters(var_health, var_monster_health, var_lives, monsters_outside):
    input("")
    maze()

def learning_the_way(var_health, var_monster_health, var_lives, monsters_outside,var_un, name,backpack_list):
    #print(str(var_health)+ str(var_monster_health)+ str(var_lives)+ str(monsters_outside)+str(var_un)+ str(name))
    input("Press enter to continue... ")
    print("****** LEVEL V ******")
    print("*** The Training ****")
    input("Press enter to continue... ")

    input( "Gwenda: You made it through the graveyard!")
    input( "Gwenda: Let's see what you found.")
    print("||Rusty Sword || Iron sword || Lance || Dagger || Amulet of life 3 of 3 || Amulet of Unknown ||")
    #["silver sword", "iron sword", "lance", "dagger"]
    input( var_un + ": A rusty sword!")
    input( "Gwenda: That sword will not help you very much.")
    print( "It is effective against castle people, but not against")
    print( "monsters.")
    print( "I will change it into something more powerful!")
    input("")
    input( var_un + ": Thanks!")
    input( var_un + ": I also found an iron sword, a lance, a dagger, 3 amulets of life, and an amulet of something.")
    print( "I dont remember the name of it.")
    input("")
    print( "Gwenda: In battle, you will choose an item to attack with.")
    print( "Depending on which item you attack with, the chances of ")
    print( "landing a hit, multiple hits, landing critical hits, and return damage ")
    print( "are different.")
    input( "")
    print( "Gwenda: An iron sword will inflict 3 damage every hit.")
    print( "with the possibility of hitting 3 times per attack.")
    print( "The chance of return damage is about 40%.")
    input("")
    print( "Gwenda: Attacking with the lance, has a higher hit chance and more damage dealt per hit,")
    print( "but you will only be able to hit the monster once per attack")
    input("")
    print( "Gwenda: Attacking with the dagger, has a low damage dealt per hit,")
    print( "but since it is small and you will need to be close to the monster, ")
    print( "it has a high chance of hitting multiple times causing massive damage.")
    print( "Being close to a monster can also have a negative affect!")
    input("")
    print( "Gwenda: If you lose a battle and you have an amulet of life;")
    print( "the amulet will restore your life.")
    input( "")
    input( "Gwenda: I must go find the warlock.")
    print( "I have long suspected that the king was behind all of this.")
    print( "The monsters came back to this area shorlty after he took the throne")
    print( "and seem to protect the castle in a way...")
    print("")
    input( var_un + ": The monsters attacked the castle while I was in it!")
    input( var_un + ": I can't imagine that the king has anything to do with this.")
    input( "Gwenda: That may be what he wants you to think.")
    input( "Gwenda: I will search the area for another reason why they are here.")
    print( "If I can't find another warlock, then the king must be the one behind this. ")
    input( "")
    input( "Gwenda: I will meet up with you again someday...")

    input( "")
    input( var_un + ": Back to the forest to meet the wizard I guess")
    print("")
    input(".")
    input("..")
    input("...")
    print("Noises in the forest")
    input("")
    if monsters_outside == 0:
        input( var_un + ": I thought that monsters were all dead out here!")
        
    input( var_un + ": So I guess that I will get some practice in before the castle!")

    input("")
    print("You are near the edge of the battle swamp and the dark forest.")
    print("")
    if monsters_outside == 0:
        input("The noise that you heard was another monster comming for you.")
        monsters_outside = 1
    else:
        input("The noises that you heard, were the monsters comming for you.")  
        input("They are lining up and will attack. and attack until thay are all defeated.")  

    return(var_health, var_monster_health, var_lives, monsters_outside,var_un, name)



def the_way_back(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side):
    input("")
    input( var_un + ": That wasn't too hard!")
    input( var_un + ": I wonder if I can trust that witch.")
    input( var_un + ": Wizard " + name  + " and her don't seem to tell the same story.")
    print(" Both stories seem possible, but they can't both be true.")
    input("")
    print(" Or could they?")
    input("")
    print(" If the witches did cast the spell on the castle people,")
    print(" why would she help me?")
    input("")
    print(" If the story that the wizard told me wasn't true,")
    print(" that means that the warlocks are powerful enough to ")
    print(" defeat the wizards.")
    input("")
    print(" How could I help them against someone that powerful?")
    input(" ")
    print( var_un + ": Or could the wizard be the one that is lying?")
    input(" ")
    print( var_un + ": I wonder what a warlock would have to say about this.")
    input("")
    print("Who should you trust? wizard, witch, or neither")
    ff = input(" ")
    if ff == 'wizard':
        var_wizard_side +=2
    elif ff == 'witch':
        var_wizard_side +=3
    elif ff=='neither':
        var_warlock_side += 3
    else:
        var_warlock_side += -1
    input(" ")
    print("Wizard side: " + str(var_wizard_side) + " || Warlock side: " + str(var_warlock_side)) 
    input("")
    print( var_un +": I'm going to go with my gut on this one")
    if var_wizard_side >= var_warlock_side:
        
        print(" and assume that both the wizard and witch are not evil.")
        if ff == "witch":
            print("Especialy that witch!")
        elif ff == "wizard":    
            print("Especialy " + name + "!")
        else:
            print("But should I trust them?") 
    else:
        print(" and say they are both confused!")  

    input("")
    print( var_un +": I need to hurry and find " + name + " before anymore monsters find me")
    input("")
    input(".")
    input("..")
    input("...")
    if ff != "wizzard":
        print( var_un + ": " + name + ", there you are!")
        print("Wizard " + name + ": Is that what you call me now? ")
        input( var_un + ": It's your name isn't it?")
    else:
        input( var_un + ": Wizard " + name + ", there you are!")

    print("Wizard " + name + ": Did you find any supplies? ")  
    input( var_un + ": Yes, I found a bunch of things.") 
    print(" 2 swords, a lance, a dagger, and 2 types of amulets.")
    input("")
    print("Wizard " + name + ": What kind of amulets did you find?")
    input("")
    input( var_un + ": 3 amulets of life and one...")
    print("That I don't remember the name of.")
    input("")
    print("Wizard " + name + ": That looks like... ")
    input("")
    input( var_un + ": The witch didn't know...")
    input("Wizard " + name + ": Witch?")
    input("")
    input("Boom!")
    input("")
    print("Wizard " + name + ": That came from the castle.")
    print("We must hurry")
    input("")
    print("Wizard " + name + ": I will set up a time trap.")
    print("If I feel that you are in danger, I will send you")
    print("back to this point in our journey!")
    input("")
    input( var_un + ": Sounds good!")
    input("")
    input("Boom!")
    input("Crack!")
    input("")
    input( var_un + ": More monsters?")
    print("Oh no!")
    input("")
    print("Wizard " + name + ": You take care of the monsters ")
    print("and I will meet you inside.")
    return (var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side)


def the_battle_outside(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side,source):
    monsters_outside = (random.randint(2,5))
    input("")
    if source == 'inside':
        input( var_un + ": He sent me back here!")
        print("I know what is about to happen!")
        print("I just wish it was after the monsters")
        input("")

    dialog = (random.randint(1,4))
    if dialog ==1:
        input( var_un + ": More monsters? I can do this!")
    elif dialog == 2:
        input( var_un + ": More monsters? I think this should be easy!")

    elif dialog == 3:
        input( var_un + ": MONSTERS, come out, come out") 
        print("wherever you are!")   
            
    input("")
    
    while monsters_outside != 0:
        var_monster_health += (random.randint(0,10))
        (monsters_outside, var_lives, var_health) = battle(var_health, var_monster_health, var_lives, monsters_outside)
    return(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side)

    





(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side) = the_way_back(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side)

(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side)=the_battle_outside(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side,'outside')
exit()

(var_un, name, var_health,var_wizard_side,var_warlock_side) = escape_the_castle(var_health,var_potion,var_wizard_side,var_warlock_side)
print("Wizard side: " + str(var_wizard_side) + " || Warlock side: " + str(var_warlock_side)) 
quit = input("Do you want to quit here? yes or no: ")
if quit == "yes":
    exit()
(var_health, var_monster_health, var_lives, monsters_outside,var_un, name,var_wizard_side,var_warlock_side) = dark_forest(var_health, var_monster_health, var_lives, monsters_outside,var_un, name,var_wizard_side,var_warlock_side)
print("Wizard side: " + str(var_wizard_side) + " || Warlock side: " + str(var_warlock_side)) 
quit = input("Do you want to quit here? yes or no: ")
if quit == "yes":
    exit()
searching_for_supplies(var_un, name,var_health, var_monster_health, var_lives, monsters_outside,var_wizard_side,var_warlock_side)
print("Wizard side: " + str(var_wizard_side) + " || Warlock side: " + str(var_warlock_side))    
quit = input("Do you want to quit here? yes or no: ")
if quit == "yes":
    exit()
  
(backpack_list) = maze()  
quit = input("Do you want to quit here? yes or no: ")
if quit == "yes":
    exit()
(var_health, var_monster_health, var_lives, monsters_outside,var_un, name) = learning_the_way(var_health, var_monster_health, var_lives, monsters_outside,var_un, name,backpack_list)
input("Press enter to continue... ")
print("***** LEVEL VI ******")
print("**** The Attack *****")
input("Press enter to continue... ")



(monsters_outside, var_lives, var_health) = battle(var_health, var_monster_health, var_lives, monsters_outside)


(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side) = the_way_back(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side)
(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side)=the_battle_outside(var_un, name,var_health, var_monster_health, var_lives,var_wizard_side,var_warlock_side,'outside')





#searching_for_supplies(var_un, name,var_health, var_monster_health, var_lives, monsters_outside )

#input("Engaging in battle!")
#while monsters_outside >0:
#    if str(var_lives) in ("0","2","3","4","5"):
#        input("You have " + str(var_lives) + " 'Amulets of life'")
#    else:
#        input("You have " + str(var_lives) + " 'Amulet of life'")
#    input("With " + str(var_health) + " health")
#    (monsters_outside, var_lives, var_health) = battle(var_health, var_monster_health, var_lives, monsters_outside)
#    input("Nice victory!")   













