print("One Night , You Get Out With Your Friends In A Pub , You Get Wasted , Somehow You get Home.")
print("The Next Day You Woke Up , You Realise That This Is Not Your House And You Are Not Alone.")
print("Find Out What's Happening!")
print("Room 1")
print("You Should Look Around.")
#Action = input("What Will You Do Next?:")
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
        turns +=3
        print ("You've spent",turns,"Turn(s) Doing This Action.")
        break
    elif turns == 5:
        print ("You Lost!")
        break
    else:
        print ("This Is Not A Valid Action!")
        print ("You've spent",turns,"Turn(s) Doing This Action.")

print("As You Escaped The First Room , You Make Your Way To The Second Room.")
print("You Hear A Lot Of Sounds , You Get Restless.")
print("You Should Look Around!")

continuedt = turns - 3

while continuedt < 5:
    Action = (input("What Will You Do Next?:"))
    continuedt +=1
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
    elif Action == "feed cat":
        print("You Feed Her.")
        print("She Seems To Like You.")
        print("Cat: Meow , Meow , Meow.")
        print("Yourself:Maybe She Is Trying To Tell me Something...")
        print("You've spent",continuedt,"Turn(s) Doing This Action.")
        continuedt +=2
    elif Action == "meow,meow,meow":
        print("You've Opened A Secret Door Leading To Exit.")
        print("Congratulation , You've Finished The Game!")
    elif Action == "break window":
        print("You Break The Window , Making A Lot Of Noise , But You Did Found A Key.")
        print("You Now Have A Key.")
        print("Yourself:WHY DO I ALWAYS HAVE TO BREAK SOMETHING???")
        break
    else:
        print ("This Is Not A Valid Action!")
        print ("You've spent",continuedt,"Turn(s) Doing This Action.")
