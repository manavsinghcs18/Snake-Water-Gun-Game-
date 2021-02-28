import random
def game(player1 , player2):
    if(player1==player2):
        return None
    elif(player1=="s"):
        if(player2=="w"):
            return False
        elif(player2=="g"):
            return True
    elif(player1=="w"):
        if(player2=="g"):
            return False
        elif(player2=="s"):
            return True
    elif(player1=="g"):
        if(player2=="s"):
            return False
        elif(player2=="w"):
            return True
print("Player 1 is already Choosed between Snake(s),Water(w) and Gun(g) :")
random_number=random.randint(1,3)
if(random_number==1):
    player1="s"
elif(random_number==2):
    player1="w"
elif(random_number==3):
    player1="g"
player2=input("Player 2 :Choose between Snake(s),Water(w) and Gun(g) :")
a=game(player1,player2)
print("Player1 choose",str(player1))
print("Player2 choose",str(player2))
if(a==None):
    print("The game is tie!")
elif(a):
    print("You Win!")
else:
    print("You Lose!")
