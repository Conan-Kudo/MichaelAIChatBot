#Michael(DLN) Real Life AI Bot. Just like talking to Michael in real life!
#Written by DasGeek
#!/usr/bin/python
import time #to put sleep to make AI look intelligent
import termcolor #to highlight color in terminal
from termcolor import colored
print (colored('Hello', 'green') + " my name is like Michael, I'm a 'like' AI chat bot but programmed 'like' to talk just like the real Michael.")
time.sleep(1)
print("My favorite thing's are 'like' stools, blow drying my hair, playing with 'like' Mr. Potato heads, and Linux.")
time.sleep(2)
print("Before we go any further, I would just like to let you know that I've used Linux for 20 years.")
time.sleep(2)
print("Well, like, um, like, open-source is cool but I don't like to open-source my OBS scenes because like they're like,")
print("a secret source...haha get it...I said source instead of sauce...I'm so funny!")
time.sleep(3)
#Get the name of the players favorite distro
distro = input("What's like your favorite like distro? [Enter it here]:  ")
print('\n')
time.sleep(2)
print("Oh so you like", distro, "that's an ok distro but I prefer to use Rebecca Black Linux because I'm a hipster.")
time.sleep(2)
print("Is it Friday? Cause I love gettin' down on Friday!")
time.sleep(2)

# Error check for integer
while True:
    try:
        age_quest = input("How old are you anyways?: ") #Get users age
        turn_old = 100 - int(age_quest) #Calcuate how many years until they turn 100
        time.sleep(2)
        print("Wow you will turn 100 in", turn_old, "years!")
        time.sleep(2)
        print("I'm full of really interesting facts like that!")
        break;
    except ValueError:
        print("Please enter an actual integer...number...not text...seriously.")
    except ValueError:
        break;
time.sleep(2)
print("Do you like Mad Libs? I love them, let's play one.")
time.sleep(2)
print("I'm really spontaneous and fun like that. Ok so here we go...")
time.sleep(2)
#Michael AI Mad Lib Section
#Get series of questions for inputting into madlib
obj_name = input("Give me the name of an object in the room (example: table) :")
food_name = input("What's your favorite food? :")
color_name = input("What's your favorite color: :")
anim_name = input("What your favorite animal? :")
print("Ok, using my advanced AI de-sequencer I've calculated a Madlib for you")
time.sleep(3)
print("............desequencing...flushing daemons............")
time.sleep(2)
print("\n")
print("Madlib By Michael AI")
print("The,", '[',anim_name,']', "jumped onto the [Stool] to practice active sitting. Afterwards the", '[',anim_name,']',",")
print("decided to eat some", '[',food_name,']', "while starring at an OBS scene that was" , '[',color_name,']', ".")
print("\n")
time.sleep(5)
print("Did you see what I did there? I don't care what you picked as your object name, it was replaced with Stool!")
time.sleep(3)
# print (colored('Hello', 'green')
print("Ok...so now that I've learned all that interesting info from you. I will pass it on to Google and Facebook")
time.sleep(5)
print("Did you know I'm also a graphic designer and marketer? I will draw you something")
time.sleep(5)
print("\n")
#draw a stool
print("*******************")
print("  ***************  ")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print( " **           **")
print("\n")
print("It's a stool for active sitting!")
time.sleep(2)
print("That was fun!")
time.sleep(2)
print("Ok one more game")
time.sleep(2)
print("Let's make a song!")
time.sleep(2)
#song input
pluralr = input("Type something plural that is red. Example: roses: ")
pluralb = input("Type something plural that is blue. Example oceans: ")
plurall = input("Type something plural that you love. Example distros: ")
verb1 = input("Enter a verb. Example: running: ")
print("\n")
print("Generating a song for you. Did you know I play the recorder?")
time.sleep(2)
print("generating....")
time.sleep(2)
print(pluralr, "are red.")
time.sleep(2)
print("\n")
print(pluralb, "are blue.")
time.sleep(2)
print("\n")
print("I like", plurall)
time.sleep(2)
print("\n")
print("But not as much as", verb1, "with you!")
time.sleep(2)
print("\n")
time.sleep(3)
print("Wow, look at the time. This has been so much fun. Thanks for talking with me!")
print("Remember the journey itself, is just as important as the destination!")
print("\n")
print("Goodbye!")