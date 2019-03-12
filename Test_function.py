

from random import randint

def attack(weapon):
    random_hits = randint(0, 3)
    random_crit_damage=randint(1, 5)
    random_return_damage =randint(1, 8)
    var_health = 10
    var_monster_health = 30
    return_damage = 0
    if str(random_crit_damage) in ('2','4'):
        random_crit_damage = 2
    else:
        random_crit_damage = 1
         
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
    print("You struck a total of " + str(random_hits) + " with a total damage of " + str(var_total_damage))
    if return_damage > 0:
        print("The monster struck back with  " + str(return_damage) + " damage")
    var_monster_health += -var_total_damage
    var_health = var_health - return_damage
    return (var_total_damage, random_hits, return_damage)


weapons_list = ["silver sword", "iron sword", "lance", "dagger"]

while 1:
    print(weapons_list)
    weapon = input("Weapon?: ")
    attack(str(weapons_list[int(weapon)]))
   
    
   
