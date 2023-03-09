import random as r
o=["Rock","Paper","Scissor"]
play=True
while play==True:
    p=input("Choose ROCK PAPER SCISSOR:")
    c=o[r.randint(0,2)]
    print("Computer:",c)
    if p.lower()!=c.lower():
        if p.lower()=="rock":
            if c.lower()=="paper":
                print("You lose. Rock covers paper!")
            else:
                print("You win! Rock breaks scissors.")
        if p.lower()=="paper":
            if c.lower()=="rock":
                print("You win! Rock covers paper!")
            else:
                print("You lose. Scissor cuts paper!")
        if p.lower()=="scissor":
            if c.lower()=="rock":
                print("You lose. Rock breaks scissors.")
            else:
                print("You win! Scissor cuts paper!")
                
    else:
        print("Tie!!")
    q=(input("Do you want to continue ? Y/N"))
    if q.lower()=="y":
        play=True
    else:
        play=False
