import random

def play():
    user = input("what is your choice? r for rock ")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return 'tie'
    if is_win(user,computer):
        return "you won"
    
    return "you lost"
    # r > s , s > p , p > r
    



def is_win(player,opponent):

    if (player == 'r' and opponent == 's') or (player == "s" and opponent == 'p') or (player =='p' and opponent == 'r'):
        return True


print(play())