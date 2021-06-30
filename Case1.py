#Case 1
import sys
import time
from time import sleep
import typing

def typinginput(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.050)
    value = input()
    return value

c1int = typinginput("On a cold Sunday morning a young couple goes out jogging around a local park; as they round the corner to the isolated part of the park they neared the fountain.\nBlood trailed around the fountain towards the bushes where a recently killed person was hidden away.\nIn sheer horror and panic they ran to a near by booth and rang the police alerting them of the crime scene. \nAre you ready?\n")
if c1int == "No":
    print("Game Over.")
elif c1int == "Accept" or "Yes" or "Yeah":
    print("PC Plodder arrives on the scene; glancing around they can see a couple to the right near the entrance looking shaken up; a bunch of officers scattered around lazily glancing around and the body is laid out on the ground.\nThe first thing that PC Plodder has to do is investigate around the crime scene for a murder weapon.\nAfter the murder weapon has been found PC Plodder has to speak to the witnesses and gather more information.\nAfter finding the weapon and gathering more information from the witnesses PC Plodder will talk with officers to search the area for suspicious suspects.")

c1int_input=input("What is the first thing PC Plodder has to do?\n")
sweap="Search for weapon"
cwit="Check Witnesses"
coff="Check Officers"
def f1():
    global c1int_input
    if c1int_input == "Search for weapon" or "Weapon":
        x=input("Do you search the area to the left, right or check the fountain?\n")
        if x=="left":
            print("Searching to the left of the crime scene you look through the bushes and trees but find no evidence.")
            x=input("Where else do you look?\n")
        if x=="right":
            print("Searching around the body you don't find any new evidence.")
            x=input("Where else do you look?\n")
        if x=="fountain":
            print("You see the glint of a blade beneath the waters surface, picking it up you closely inspect it; soon realizing it is the murder weapon.\nYou quickly add it to the evidence and send it to the police station so they can start pulling information from it.")        
            x==input("Are you ready to move on and speak to the witnesses?\n")
    else:
        print("I don't understand that choice.")
        c1int_input=input("What shall PC Plodder do?\n")
        f1()
f1()

c1int_input=input("What does PC Plodder have to do with the Witnesses?\n")

def f2():
    global c1int_input
    if c1int_input == "Speak" or c1int_input== "Speak to Witnesses" or c1int_input== "question":
        c=input("Do you 'Ask if they recognise the victim', 'Ask if they are frequent runners in the park' or 'Ask if they've seen something suspicious elsewhere in the park'.\n")

        if c=="victim"or c == "recognise"or  c =="ask if they recognise the victim":
            print("They recognize the man as a common runner in the morning.")
            c=input("What else do you ask?\n")

        if c=="frequent"or c =="runners" or c== "runner" or c== "park"or c=="ask if they are frequent runners in the park":
            print("Yes they are common runners in the park.")
            c=input("What else do you ask?\n")

        if c=="suspicious"or c=="elsewhere"or c=="ask if they've seen something suspicious elsewhere in the park":
            print("Yes, they saw a small dark shadow down the right side of the body briefly.Before it disappeared down a narrowed path.")        
    else:
        print("I don't understand that choice.")
        c1int_input=input("What shall PC Plodder do?\n")
        f2()
f2()

c1int_input=input("Are you ready to move on and talk to the officers gathered?\n")

def f3():
    global c1int_input
if c1int_input == "Yes" or c1int_input == "yes":
    typinginput("\nReviewing the evidence gathered you walk over to the officers and then review it together,quickly deciding that it would be best for you to search the area\nwith the body and blood being so fresh it is a good guess that the murder didn't happen that so long ago; meaning the killer could still be in the park but hiding.\n\nThankfully you interviewed the Witnesses and got told about a suspicious shadow to the right side of the body near the narrowed path.\nGetting up you and a bunch of officers go down the narrowed path, quickly stumbling upon a small woman who looks to be in her mid 20's crouched in the bushes.\nHer clothes are covered in blood and it looks like shes been in a fight; because she looks suspicious she is taken away to the police station and questioned along with the evidence.\n\nWith the woman in custody you pile all of the evidence together.\n\nWith the DNA on her clothes matching the victim and the fingerprints on the knife that you found matching her prints it is safe to say that you caught the killer.\nShe quickly confesses to the murder after a quick background check shows that she worked in the same place as the victim.\n\nShe killed the Victim in a jealous and envy filled rage after finding out he was getting a promotion that she was promised.\nCase 1 has been solved; Good job detective.")
else:
    print("I don't understand that, try again.")
    c1int_input=input("Are you ready to move on and talk to the officers gathered?\n")
    f3()
f3()