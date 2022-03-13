print("---------------******ROLL THE DIE*****-------------".center(50))
print("")
p1=input("name of player1  :")
print("")
p2=input("name of player2  :")
print("")
print("@@@@@@@@@@@@let's begin the game@@@@@@@@@@@@@@".center(24))
print("")
n=input("write CODE to start the game:")
print("")
if n=="don is here":    
    print("you are right") 
    import random
    r1=(random.randint(1,6))
    print("it's player1 chance")
    n=input("  ")
    print("player1 score",r1)
    print("player2 roll the dice")
    n=input("   ")
    import random
    r2=random.randint(1,6)
    print("player2 score",r2)
    print("")
    if r1>r2:
        print("THE WINNER IS:",p1)
    if r2>r1:
        print("THE WINNER IS:",p2)
    if r1==r2:
        print("MATCH DRAWS")
else:
    print("INCORRECT CODE")print("---------------******ROLL THE DIE*****-------------".center(50))
print("")
p1=input("name of player1  :")
print("")
p2=input("name of player2  :")
print("")
print("@@@@@@@@@@@@let's begin the game@@@@@@@@@@@@@@".center(24))
print("")
n=input("write CODE to start the game:")
print("")
if n=="don is here":    
    print("you are right") 
    import random
    r1=(random.randint(1,6))
    print("it's player1 chance")
    n=input("  ")
    print("player1 score",r1)
    print("player2 roll the dice")
    n=input("   ")
    import random
    r2=random.randint(1,6)
    print("player2 score",r2)
    print("")
    if r1>r2:
        print("THE WINNER IS:",p1)
    if r2>r1:
        print("THE WINNER IS:",p2)
    if r1==r2:
        print("MATCH DRAWS")
else:
    print("INCORRECT CODE")
 
 
