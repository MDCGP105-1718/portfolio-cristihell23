def end_game():
    print("Game Over.")
    exit()
def izi_game():
    print("That Was Easy.")
    exit()

print("One Night , You Get Out With Your Friends In A Pub , You Get Wasted , Somehow You get Home.")
print("The Next Day You Woke Up , You Realise That This Is Not Your House And You Are Not Alone.")
print("Find Out What's Happening!")
print("Room 1 - 5 Turns Available")
print("Main Quest - Find A Way To Get Out Of The House.")
print("Tip-You Should Look Around.")

turns = 0
while turns < 5:
    Action = (input("What Will You Do Next?:"))
    turns +=1
    if Action == ("look around"):
        print ("You See A Table , A Chair And A Wooden Door.")
        print ("Yourself:Should I Try To Move The Table? Maybe the Chair? Or I Might Even Break The Door.")
        print ("Available Actions = 'move table','move chair','break door'")
        print ("You've spent",turns,"turn(s) Doing This Action.")
    elif Action == ("move table"):
        print ("You Move The Table")
        print ("Yourself:I Can See Something , It Looks Like A Key")
        print ("You Now Have A Key.")
        print ("You've spent",turns,"turn(s) Doing This Action.")
        break
    elif Action == ("move chair"):
        print ("You Move The Chair")
        print ("Yourself:I Moved The Chair , Found Nothing , Did That Really Worth?")
        print ("You've spent",turns,"turn(s) Doing This Action.")
    elif Action == ("break door"):
        print ("You Did It , But Is That Really Ok?")
        print ("Yourself:I Broke The Door , I Feel Insecure.")
        print ("I should procced to the next room.")
        turns +=2
        print ("You've spent",turns,"Turn(s) Doing This Action.")
        break
    elif turns == 5:
        print ("You Lost!")
        break
    elif Action == "turns":
        turns -=1
        print("You've Spent",turns,"turn(s)")
    else:
        print ("This Is Not A Valid Action!")
        print ("You've spent",turns,"Turn(s) Doing This Action.")

if turns == 5:
    end_game()

print("As You Escaped The First Room , You Make Your Way To The Second Room.")
print("You Hear A Lot Of Sounds , You Get Restless.")
print("Room 2 - 5 Turns Available")
print("Main Quest - Updated")
print("Tip-You Should Look Around!")
continuedt = turns - 3

while continuedt <= 5:
    Action = (input("What Will You Do Next?:"))
    continuedt +=1
    if continuedt < 0:
        continuedt = 1
    if Action == "look around":
        print("You Can See A Cat , A Window , A Metal Door , And Some Cat Food.")
        print("Available Actions = 'play with cat','break window','break door','feed cat'")
        print("You've spent",continuedt,"Turn(s) Doing This Action.")
    elif Action == "play with cat":
        print("You Play With Her.")
        print("She Seems To Like You.")
        print("Cat : Meow , Meow , Meow!")
        print("Yourself:Maybe She Is Trying To Tell Me Something...")
        print("You've spent",continuedt,"Turn(s) Doing This Action.")
        print("Secondary Quest - Meow?")
        print("Tip-Secondary Quests Are Hard To Complete But They Are Rewarding.")
    elif Action == "feed cat":
        print("You Feed Her.")
        print("She Seems To Like You.")
        print("Cat: Meow , Meow , Meow.")
        print("Yourself:Maybe She Is Trying To Tell me Something...")
        print("Secondary Quest - Meow?")
        print("Tip-Secondary Quests Are Hard To Complete But They Are Rewarding.")
        continuedt +=2
        print("You've spent",continuedt,"Turn(s) Doing This Action.")
    elif Action == "meow,meow,meow":
        print("You've Opened A Secret Door Leading To Exit.")
        print("Congratulation , You've Finished The Game!")
        izi_game()
    elif Action == "break window":
        print("You Break The Window , Making A Lot Of Noise , But You Did Found A Key.")
        print("You Now Have A Key.")
        print("Yourself:WHY DO I ALWAYS HAVE TO BREAK SOMETHING???")
        continuedt +=2
        print("You've spent",continuedt,"Turn(s) Doing This Action.")
        break
    elif Action == "break door":
        print("You Tried To Break A Metal Door , You Failed.")
        print("Yourself:Have I Really Tried That? My Shoulder Hurts.")
        continuedt +=2
        print("You've spent",continuedt,"Turn(s) Doing This Action.")
    elif Action == "turns":
        continuedt -=1
        print("You've Spent",continuedt,"turn(s)")
    else:
        print ("This Is Not A Valid Action!")
        print ("You've spent",continuedt,"Turn(s) Doing This Action.")

if turns == 5:
    end_game()

print("You've Escaped The Second Room , But Will You Be Able To Make It To The Finish?")
print("You're Making Your Way To Third Room.")
print("Room 3 - 5 Turns Available")
print("Main Quest - Updated")
print("Tip-You Should Look Around!")

continuedtt = continuedt - 2

while continuedtt < 5:
    Action = (input("What Will You Do Next?:"))
    continuedtt +=1
    if continuedtt < 0:
        continuedtt = 1
    if Action == "look around":
        print("You Can See A Hammer , A Dark Shadow , And A Flashlight")
        print("Available Actions 'use hammer' ,'inspect shadow','use flashlight','find an exit'")
        print ("You've spent",continuedtt,"Turn(s) Doing This Action.")
    elif Action == "use hammer":
        print("Yourself:Ok , I Have A Hammer Now , What Will I Use It For?")
        print("You Now Have Hammer.")
        print ("You've spent",continuedtt,"Turn(s) Doing This Action.")
    elif Action == "inspect shadow":
        print("Yourself:I Would Go Closer... But Im Too Afraid.")
        print("Yourself:I Feel Like There's Something Important.")
        continuedtt +=2
        print ("You've spent",continuedtt,"Turn(s) Doing This Action.")
    elif Action == "use flashlight":
        print("You Got A Flashlight")
        print("Yourself:Let's Light The Dark.")
        print("Yourself:WHAT?IT HAS NO BATTERY.")
        print("Secondary Quest - Find battery")
        print("Tip-Secondary Quests Are Hard To Complete But They Are Rewarding.")
    elif Action == "meow,meow,meow?":
        print("Seems Like That Cat Had A Spare Battery , You Just Had To Ask!")
        print("Secondary Quest Complete!")
        print("You Turn The Flashlight On And Inspect The Dark Shadow.")
        print("You Found An Hidden Passage.")
        print("Yourself:That Cat Is Really Helpful!")
        izi_game()
    elif Action =="find an exit":
        print("You Search For An Exit.")
        print("You Found One!")
        print("Yourself:That Was.... Easy??")
        break
    elif Action == "turns":
        continuedtt -=1
        print("You've Spent",continuedtt,"turns")
    elif Action == "turns":
        continuedtt -=1
        print("You've Spent",continuedtt,"turn(s)")
else:
    print ("This Is Not A Valid Action!")
    print ("You've spent",continuedtt,"Turn(s) Doing This Action.")

if turns == 5:
    end_game()

print("You've Made It To The Last Room")
print("Now Be Carefull Because You're NOT ALONE")
print("You Hide Somewhere.")
print("Tip - If You Don't Exit In 3 Turns , Something Evil Will Happen.")
print("Room 4 - 3 Turns Available")
print("Main Quest-Updated")
print("Tip - You Should Look Around!")

continuedttt = continuedtt -1

while continuedttt < 3:
    Action =(input("What Will You Do Next?:"))
    continuedttt +=1
    if continuedttt <0:
        continuedttt = 1
    if Action == "look around":
        print("You Are Not Able To See Anything Because You Are Hidden!")
        print("You Decide That You Can Do This:")
        print("Available Actions : 'make a run','elaborate a plan',try to be friendly,'try to fight'")
    elif Action == "make a run":
        print("Despite Your Efforts , Something Scared You Really Bad.")
        print("You Died. It Was A Rabbit Tho'.")
        print ("You've spent",continuedttt,"Turn(s) Doing This Action.")
        break
    elif Action == "elaborate a plan":
        print("You Decide To Elaborate A Plan.")
        print("It Took A While.")
        print("But You Didn't Really Came Up With One.")
        continuedttt +=3
        print ("You've spent",continuedttt,"Turn(s) Doing This Action.")
        print("You Lost!")
    elif Action == "try to be friendly":
        print("You Give Up Hidding , And You Find Out That The Monster Is A Rabbit.")
        print("You Were Just Paranoic.")
        print("You Won The Game.")
        print("Congratulation!")
        break
    elif Action == "try to fight":
        print("You Are Prepared To Fight.")
        print("You Found Out That Your Enemy Is A Rabbit.")
        print("You Trip And Die.")
        print("You Lost!")
        break
    elif Action == "turns":
        continuedttt -=1
        print("You've Spent",continuedttt,"turn(s)")
else:
    print ("This Is Not A Valid Action!")
    print ("You've spent",continuedtt,"Turn(s) Doing This Action.")

if turns == 3:
    end_game()
if not end_game():
    print("True")
