from random import randint
monsters_outside = 1
var_health = 10
var_monster_health = 30
var_lives = 3
var_un = "bobo"
name = "Chaps"

import numpy as np
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
                if search == "no":
                    location = new_location
                    new_location = 0
                    break
                elif search =="yes":
                    if new_location == 27:
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
                            location = new_location
                            new_location = 0
                        boa=input("Would you like to read the back of it?: ")
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
                            location = new_location
                            new_location = 0
                    elif new_location == 31:
                        if dagger == 1:
                            dagger =0
                            backpack_list[3] = "Dagger"
                            print("You found the an old dagger!")
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






        elif new_location in grave_list:
            print("You found a grave!")
            while 1:
                search = input("Do you want to search it?: ")
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
                            print("      |                  | |")
                            print("      |                  | |")
                            print("      |                  | |")
                            print("      |                  | |")
                            print("      |                  | |")
                            print("      |                  | |")
                            print("  ~~~ |                  | |~~~~")
                            print("  ~~~ |                  | |~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
                            print("Nothing, but an unmarked headstone!")
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
                            backpack_list[2] = "Iron sword"
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
        if  str(random_return_damage) in ('2','4','6', '8'):
            return_damage = 4
    elif weapon == "iron sword":
        var_hit_damage = 3
        random_hits = randint(0, 2)
        if  str(random_return_damage) in ('2','4','6'):
            return_damage = 5
    elif weapon == 'lance':
        var_hit_damage = 5
        if  str(random_return_damage) in ('2','4','6','8'):
            return_damage = 4        
        random_hits = randint(0, 1)
    elif weapon == 'dagger':
        var_hit_damage = 1
        random_hits = randint(0, 7)
        if  str(random_return_damage) in ('2','4','6', '8'):
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
                input(str(monsters_outside) + " monsters remain in the 'Battle Swamp'!")
            else:
                input(str(monsters_outside) + " monster remains in the Battle Swamp'!")
                    
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

def searching_for_supplies(var_un, name,var_health, var_monster_health, var_lives, monsters_outside ):
    input("Wizard " + name + ": You have shown some great strength out here.")
    input("Wizard " + name + ": You are on the right path.")
    input( var_un + ": Thanks?")
    input("Wizard " + name + ": " + var_un + ", I believe that you have what it takes to be a great warrior. ")
    input("Wizard " + name + ": To succeed, you will need to stay on this road. ")
    input( var_un + ": What?")
    input("Wizard " + name + ": You will need to stay on this road to find your way back to the castle. ")
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
        input( var_un + ": Ok, there is a cave that way and that swampy graveyeard over there.")
        r= input( var_un + ": Should I search the cave or the graveyard?: ")
        if r =="cave":
            if c==0:
                input( var_un + ": Oh, I see a rusty sword atthe enterence, ") 
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
    input( "Gwenda: I sense that you are capable of helping me get rid of the monster.")
    input( "Gwenda: In this graveyard there are tools that you will need.")
    input( "Gwenda: If you are able to find your way through the graveyard,")
    print( "you will find six items.")
    input( "Gwenda: Walk through the enterence and i will meet you by the exit on the north wall.")
    maze()















def the_quick_way_back(var_un, name,var_health, var_monster_health, var_lives, monsters_outside ):
    input("")

def the_long_way_back(var_un, name,var_health, var_monster_health, var_lives, monsters_outside ):
    input("")
    




def looking_for_monsters(var_health, var_monster_health, var_lives, monsters_outside):
    input("")
    maze()
maze()    
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













