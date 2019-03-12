from random import randint
monsters_outside = 1
var_health = 10
var_monster_health = 30
var_lives = 3
var_un = "bobo"
name = "Chaps"

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
    input("Wizard " + name + ": The non-magical beings ran back to the castle before they lost to many knights.")
    input("Wizard " + name + ": When the Witches found out what had happened at the graveyard...")
    input("Wizard " + name + ": they blammed the Warlocks for not getting their monsters to attack quick enough.")
    input("Wizard " + name + ": The Warlocks blammed the Witches of casting week spells.")
    input( var_un + ": Seems like they both suck!")
    input("Wizard " + name + ": No, The Warlocks were powerful, the Witches ruined everything.")
    input("Wizard " + name + ": It wasn't the spells, it was the plan that failed them.")
    input("Wizard " + name + ": The Witches and Warlocks battled for years after.")
    input("Wizard " + name + ": The battle lasted until the Wizards stepped in to defeat the monsters and cast all of the witches and Warlocks ...")
    input("Wizard " + name + ": to a different realm.")
    input( var_un + ": So there aren't anymore witches or warlocks here?")
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









def the_quick_way_back(var_un, name,var_health, var_monster_health, var_lives, monsters_outside ):
    input("")

def the_long_way_back(var_un, name,var_health, var_monster_health, var_lives, monsters_outside ):
    input("")
    




def looking_for_monsters(var_health, var_monster_health, var_lives, monsters_outside):
    input("")

searching_for_supplies(var_un, name,var_health, var_monster_health, var_lives, monsters_outside )

#input("Engaging in battle!")
#while monsters_outside >0:
#    if str(var_lives) in ("0","2","3","4","5"):
#        input("You have " + str(var_lives) + " 'Amulets of life'")
#    else:
#        input("You have " + str(var_lives) + " 'Amulet of life'")
#    input("With " + str(var_health) + " health")
#    (monsters_outside, var_lives, var_health) = battle(var_health, var_monster_health, var_lives, monsters_outside)
#    input("Nice victory!")   













