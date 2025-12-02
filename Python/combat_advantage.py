#Just a code example where I got confused and had to ask for help
player_power = 101
enemy_defense = 100
advantage, disadvantage, evenly_matched = False, False, False

# Do not touch above this line, this is where I got confused... should have read the instructions

if player_power > enemy_defense:
    advantage = True
    
elif enemy_defense < player_power:
    disadvantage = True
else: 
    evenly_matched = True

# Do not touch below this line

if advantage:
    print("You have the advantage!")
elif disadvantage:
    print("You have the disadvantage!")
else:
    print("You are evenly matched!")
