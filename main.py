import random

print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@        Medieval life          @
@        &&&&&&&&&&&&&          @
@      And the smelly comb      @                    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                               
""")

input("enter any key to begin your journey: ")

intro = """
good day to you sire, may the maker be with you, i am the herald
assigned to you to assist in your quest to retrieve the sought after smelly hair comb,
the so called cure to human aging,from the hag of the tower.\n
Now, you will need a name so that all will sing your praises upon success of the quest.
name your character, a suitable name, one that shall be recognised and sung about through the ages
"""

# """
# below accepts users character name and weapon choice. these remain constant through the entire game.
# """

print(intro)
character_name = input("Your name: ").lower()
print("""
(a) a fine steel Greatsword with scabbard and all
(b) a child's wooden sparring sword, no doubt some dogs chew toy at some point in its life
(c) a fork from the local kings royal palace
""")
character_weapon = input("What shall be your weapon of choice: ").lower()

if character_weapon == "a":
    character_weapon = "steel Greatsword"
    print("\nthen it is to be set in stone. You shall be known as", character_name,"The swordmaster!")
elif character_weapon == "b":
    character_weapon = "child's sparring sword"
    print("\nthen it is to be set in stone. You shall be known as", character_name, "The warchild!")
elif character_weapon == "c":
    character_weapon = "mighty fork"
    print("\nthen it is to be set in stone. You shall be known as", character_name, "The fork bearer!")
else:
    character_weapon = "enchanted brass knuckles"
    print("you consider using your bare fists, but then remember "
          "you can use your enchanted brass knuckles gifted to you from a local wizard")

input("\nenter any key to continue your journey: ")

print("""
an excellent choice sire, i could not have picked a better name for you myself.
it is time to march on the hag tower, ready yourself,
gather the servants and make for glory.
""")

input("enter any key to take out your map and begin your quest:")

print("""
you arrive at the entrance to the catacomb and notice its tarnished stone masonry, which 
looks to be centuries old. Cob webbing and waste lay above and at your feet,
dangling above your war helm and there is an unforgiving stench about the place. 
""")

input("enter any key to continue your quest:")

# """
# first choice of the game below.
# """

print(""" \n what is your next move?

a) enter the catacomb

b) scream a horrendous and penetrating war cry,bolstering your morale strength before you enter the catacomb

c) you suddenly feel reluctant and give into the fear, abandoning said quest to someone of a braver nature
      """)

first_move = input("What is your choice, sir "+character_name+":").lower()

# """
# second choice below. game continues only if user selects (a). (b),(c) exit the program.
# """

if first_move == "a":
    print("""
you enter, finding yourself in a murky room, dripping with some foul ooze and wood crates scattered about.
in the center of the room lies a golden ceramic chalice, the sole source of light in a cloud of darkness. 
it looks to be of quite high quality and shall indeed fetch a good price at the local markets for any man
lucky enough to get his hands on it.

a) you reach for the cup, intending to make it your own

b) you take a sip from the cup using your mouth 

c) you leave it be
    """)

elif first_move == "b":
    print("""
you scream, attracting the attention of an ogre watchman who
is quickly awoken,notices you and squashes you beneath his enormous leather sandals.
your quest is over. Far and wide men and women speak of the man foolish enough
to undertake a quest only to die moments after doing so. Your name becomes some what of a folk tale
only to be referred to as """+character_name,"the imbecilic \n\n\n\n\n your quest is over.... my son")
    exit()

elif first_move == "c":
    print("""
no news is heard of the from surrounding 
kingdoms and keeps. you are sure to be dead but in your heart you know you are a coward. you become a lowly bum 
struggling to find work and sleep in a box on Fulkars lane for the rest of time. You take no comfort in the fact that
no one will ever take notice of you.
 \n\n\n\n\n your quest is over.... my son
    """)
    exit()
else:
    print("your quest is over, no choice made ")
    exit()

# """
# second choice
# """

second_move = input("\n\nWhat is your choice, sir " + character_name + ":").lower()

if second_move == "a":
    print("""
as you approach the table and lift the cup in order to place it in your satchel, the floor suddenly 
caves in and you find yourself falling into a never ending whirl not knowing when you shall hit the ground.
you had only just left the keep when others heard of your death.
only a fool would fall for such a trap, the locals would say.
\n\n\n\n\n your quest is over.... my son
    """)
elif second_move == "b":
    print("""
there is a liquid that has been seeping from the ceiling making home in the cup for centuries 
and you just swallowed it all. you cant help but gag as the swirling thick ooze races down the back of your throat 
into your belly sticking to all surfaces in your body. You begin to feel slightly ill as you ascend the nearest stairs
coming to a large wooden door. Wrestling a creaking handle, you enter the mysterious chamber. Suddenly you are face to 
face with a murder hornet, so large in fact,that you have seen smaller horses in your travels
and its buzzing is more of a wood saw than that of your common hornet
    """)

elif second_move == "c":
    print("""
you refuse the chalice and ascend the nearest stairs coming to a large wooden door. Wrestling a creaking
handle, you enter the mysterious chamber. Suddenly you are face to face with a murder hornet, so large in fact,
that you have seen smaller horses in your travels and its buzzing is more of a wood saw than that of your common hornet
    """)
else:
    print("your quest is over, no choice made ")
    exit()

input("press enter to draw your " + character_weapon + " and face the beast! ")

# """
# third choice of the game below. all choices keep the game going.
# """

print("""
(a) attack
(b) defend
(c) you are terrified and you instinctually cover your head with your arms
""")

third_move = input("what is your first choice of attack: ").lower()

# """
# Here a random % chance of 20% death and 80% survive is generated through number ratios.
# wanted to do each a or b or c selection is a different weight % depending on choice
# but doesn't work for some reason. a,b would have been higher chance of survival and c less % chance.
# """

roll = random.randint(1,5)
print(roll)
if roll != 1:
    print("""
Its stinger is quick as you cut and slash at your foe
and soon you stand above it the victor. it has however managed to puncture your armoured wrist guards, as 
the bearings rupture and fly out in violent fashion...You have survived the battle! 
         """)
else:
    print("""
Your foe charges you and since you put up little of a fight,
one hundred sting wounds are inflicted on your helpless body...you have been slain... 
if only you were not so cowardly \n\n\n your quest is over.... my son""")
    exit()

input("enter any key to assess the situation: ")

# """
# fourth choice of the game below. Only selecting (a) ends the game.
# """

print("""
\nyou begin to bleed profusely as your wrist swells slightly. you know its venom could be lethal, but
you do not know if the poison will spread and kill you.

(a) amputate the limb to stop the poison from spreading. 

b) suck the poison from the wound and dress what you can to stop the bleeding. 

c) do nothing and hope that the poison is less harmful than you think
""")

fourth_move = input("\n\nWhat is your choice, sir " + character_name + ":").lower()

if fourth_move == "a":
    print("""
you swiftly decapitate your limb and the small bleed which you had before turns into 
a fast flowing river. you begin to bleed out and by the end you are face first in a pool
of your own matter. how foolish knowing you did not have anything to stop the bleeding... what a shame
\n\n\n your quest is over.... my son """)
    exit()
elif fourth_move == "b":
    print("""
you begin to suck the poison from the wound. you
seem fine but soon your lips,cheeks and face swell considerably. you begin to look
like the caricatures drawn by the jesters in the local fairs and are a bit dizzy but you have survived.
You begin climbing the nearest set of stairs to continue your quest, all wounds covered.
    """)
elif fourth_move == "c":
    print("""
by the maker... you should have been a doctor instead of a knight sire, you inspect your swelling
and bleeding and intelligently decipher that the poison is no more harmful than a few bee stings,
as you cover the bleed and continue on in your quest. 
    """)
else:
    print("your quest is over, no choice made ")
    exit()

input("enter any key to continue on in your quest ")

# """
# fifth choice of the game below. Only selecting (c) ends the game.
# """

print("""\n\nas you are about to reach the final step in the staircase, a well groomed grey dog
greets you at the top. Its hair is fine and silvery grey in nature, a bearded creature, youthful, though the dog
looks to be as old as time itself. it paws at its empty water bowl in the corner and begins to whine silently.
there is no evidence to suggest it is aggressive,but you have very little water left for yourself.
 
a) spare it for the dog instead
b) mockingly growl at the dog and continue on in your quest
c) kick the dog down the stairs to cheer yourself up
""")

fifth_move = input("\n\nWhat is your choice, sir " + character_name + ":").lower()

if fifth_move == "a":
    print("""
the dog barks in excitement licking your hand as you full its water bowl whilst emptying
your flask. You grin as the dog begins drinking as you say your goodbyes.
    """)
elif fifth_move == "b":
    print("""
you screech and howl and the dog, not expecting such a reaction, raises its ears in amazement.
as you push past the animal it whimpers as it watches you walk away.
    """)
elif fifth_move == "c":
    print("""
you position yourself carefully behind the dog and prepare to kick it for a good laugh.
as you gesture your leg in its violent motion, the dog realises what you are intending and quickly
bites down on your leg and begins to jerk you downwards. Not expecting it, You reach and grab
at the walls for something to hold onto as you topple down the stairs like a dogs bouncy ball.
you have been slain sire, by a common hound. How embarrassing. \n\n\n your quest is over.... my son
    """)
    exit()
else:
    print("your quest is over, no choice made ")
    exit()

input("enter any key to continue on in your quest ")

print("""
You enter the room that the stairs has lead to. and its clear to you
that you have reached your final destination. Ahead of you stands the hag of the tower,
hair eerie and dangling,a repulsive sight, who is yet to notice your presence and behind the creature, 
the only object in the room, a glass case. Surely this is what you seek.
""")

input("press enter to draw your " + character_weapon + " and suprise the creature! ")

print("""
You muster your courage and charge the creature. You slash and just manage
to strike a blow on her torso as you duck under her swiping fingernails,deadly
weapons of the hag. You swipe again but this time she anticipates from your previous
move. She strikes, knocking you to the floor.Your chainmail skids and
sparks against the floor with violent force and luckily you manage to hold onto your 
""",character_weapon)

input("\n\nenter any key to face your possible end: ")

# """
# sixth choice of the game below. Only selecting (b) ends the game.
# """

print("""
a) repeat attack 
b) you flee like a little child,screaming the entire way
c) you choose to face your near certain demise, grip your sword tightly,
   but make no more attempts to kill the vile beast
""")

sixth_move = input("\nWhat is your choice, sir " + character_name + ":").lower()

end = """
As you face your enemy she does not deliver a killing blow, but instead stands staring hopelessly at you.
you get to your feet but she seems to only be irascible when provoked.you slowly make ur way to the case and find it, 
self iron clips crackle as you open the container and hold up the comb but something is amiss to you. 
it seems to be nothing more than a common peasants comb with fine gray hairs and a strange smell.
no doubt the possession of your earlier run in. you stare down the hag as you pace out of the room 
but she does not react. you return home thinking your quest has been for nothing,however, 
though many view the comb and find it to be truly worthless, it is the journey that 
you took that many still talk about today. You were also rewarded handsomely by the local king 
and became something of a folk hero written about for ages to come.
huzzah for """ + character_name +"! they sang, huzzah!\n\nquest completed sire """

# """
# random % chance of 20% death same as previous % chance. only if you select (a) is % chance generated.
# if you select (a) and survive or (c) the end paragraph is printed.
# """

if sixth_move == "a":
    roll = random.randint(1,5)
    print(roll)
    if roll != 1:
        print(end)
    else:
        print("you have been slain\n\n\nyour quest is over.... my son")
elif sixth_move == "b":
    print("""
You run all the way home , cackling maniacally with tears on your cheeks.
you took comfort in the fact that your helm hid them from view but all came
to know of"""+ character_name,"the coward \n\n\n\n\n your quest is over.... my son")
    exit()
elif sixth_move == "c":
    print(end)









