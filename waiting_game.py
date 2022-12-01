#waiting game in python 
import random
import time 
def w_game():
    t=random.randint(2,4)
    input("-----Press Enter to begin-----")
    print("Your target time is %s seconds",t)
    start=time.time()
    input("-----Press Enter to again-----")
    end=time.time()
    d=end-start
    print(d)
    if int(d)>t:
        print("too slow")
    elif int(d)<t:
        print("too fast")
    elif int(d)==t:
        print("right timing")

w_game()
