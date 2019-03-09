import random

var_health = 10
var_dammage = 1
var_st_dammage = 3
var_heal = 3
var_potion = 1
var_response =  ''
var_un = input('Enter Nickname:')
      
input('It is a cold stormy night...')
input('In the forrest lives monsters. The monsters are prepairing to storm the castle.')
input('The castle is doomed and only  you can save it')
var_response = input('Should the king send his knights to battle the monsters?')
if var_response != 'no':
    var_health += - 1
    input('All but 3 knights have been defeated they are too strong. Lose 1 health.')
    input('your health is now ' + str(var_health))
print('The castle is also the home of...')
name = input('Please enter a  wizzard name')
input(name + ' is a powerful wizzard')
input(name + ' has a potion...')
if var_health !=10:
   
    input('The potion may increase your health up to 10')
    

    if input('Do you want to use it?') =='yes':
        var_health = 10
        var_potion += -1
if var_health ==10:
    print(str(var_potion) + ' potions remain, but you are full on health')
else:
    print(str(var_potion) + ' potions remain, but you are near full health')
input('oh no! the mosters broke through the gate')
x = input('would you like to run to the back exit?')
if x == 'no':
    input('you are pinned down')
    var_health=1
    x=input('will you try to escape?')
    if x=='no':
        input('GAME OVER!!!')
        exit()



input('would you like to evacuate the castle?')
y=(random.randint(1,3),)
if y == 1:
    input("You didn't escape in time!")
    input('The monsters ate you for dinner')
    exit()
elif y == 2:
    input('You and the wizzard escaped!')
else:
    input('You and the wizzard escaped!')
x=input("What would you like to do now?:")
if x =='burn the castle down':
    input("You are a bad ass!")
    print("Game Over")
    exit()
else:
    print("Ok, how about we look for supplies instead?")
y=(random.randint(1,3),)
if y == 1:
    input("You and the wizzard found a wizzard lightning potion")
    weapon ='wizzard lightning'
elif y == 2:
    input('You and the wizzard found a flame sword')
    weapon ='a flame sword'
else:
    input('You and the wizzard found a gernade!')
    weapon ='a gernade'
input("..")
input("...")
input("The monsters are chasing you!")
x=input("Should you hide? or attack with " + weapon +"?:")
if x== 'hide':
    print("RUMBLE! RUMBLE! RUMBLE! ... you're safe, but lost 2 health hiding in thorn bushes!")
    var_health += -2
    if var_health < 1:
        print("Game Over")
        exit()
elif x == 'attack':
    input ('your attack killed two out of five monsters and lost one health')
    var_health += -1
    if var_health ==0:
        print("Game Over")
        exit()
else:
    x = input("Please type hide or attack")







