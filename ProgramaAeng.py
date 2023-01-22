import random
Characters = [
    ["Michael Jackson",  50, 175, "Male", "none", "black"],
    ["Albert Einstein", 76, 160, "Male", "glasses", "white"],
    ["Nicki Nicole", 22, 145, "Female", "hat", "black"],
    ["Princesa Diana", 36, 170, "Female", "earrings", "blond"],
    ["Steve Jobs", 56, 168, "Male", "glasses", "black"],
    ["Cristiano Ronaldo", 37, 187, "Male", "none", "black"],
    ["Bad Bunny",  28, 180, "Male", "earrings", "black"],
    ["Ronnie Coleman", 58, 180, "Male", "none", "bald"],
    ["Reina Letizia", 50, 170, "Female", "hat", "brown"],
    ["Aitana", 23, 160, "Female","earrings", "black"],
    ["Dwayne Douglas Johnson", 50, 196, "Male", "none", "bald"],
    ["Vin Diesel", 55, 182, "Male", "none", "bald"],
    ["Lionel Messi",  35, 169, "Male", "none",  "black"],
    ["Leonardo DiCaprio", 48, 183, "Male", "none", "blond"],
    ["Shakira", 45, 157, "Female", "earrings", "blond"]]


print("-------------------------------")
print("Welcome to the game Who's Who?")
print("-------------------------------")
 
 
player_name=input("¿What is your name? " )
print("Let's start playing", player_name, ", good luck <3." )

Character= ["Vin Diesel", 55, 182, "Male", "none", "bald"]
Character= random.choice(Characters)
name= Character[0]
age= Character[1]
height= Character[2]
gender= Character[3]
accessories= Character[4]
haircolor= Character[5]

print("His name is:", name)
print("His age is:", age)
print("His height is:", height)
print("Gender:", gender)
print("Use some accessory:", accessories)
print("His hair color is:", haircolor)