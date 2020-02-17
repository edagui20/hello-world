name= input("What's your name?")
print("Hello " + name + ". Welcome to easy quiz!")
print("Let's get started.")
answer= input("Type in GO to start the quiz")
if answer == "GO":
    print("This quiz consists of four easy questions. ")
else:
    print("Try again")

answer= input("What's 2+2?")
if answer == "4":
    print("Correct!")
else:
    print("Incorrect!")
ansr= input("What's the capital of the U.S.?(answer with punctuation) ")
if ansr == "Washington, D.C.":
    print("Correct!")
else:
    print("Incorrect!")

huh= input("What color is the sun?")
if huh == "Yellow":
    print("Correct!")
else:
    print("Incorrect!")

ugh= input("What is the last letter of the alphabet?(answer in caps)")
if ugh == "Z":
    print("Correct!")
else:
    print("Incorrect")
print("If you get them all right, congrats!")
print("If you got some wrong you can try to play again.")
print("THANKS FOR PLAYING!")
