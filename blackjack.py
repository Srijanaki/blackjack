#!/usr/bin/python3

import random
test_list = [1, 2,3,4,5,6,7,8,9,10]
a1 = random.choice(test_list)
a2 = random.choice(test_list) 
b1 = random.choice(test_list) 
b2 = random.choice(test_list)  
initb=b1+b2
inita=a1+a2
  
print("Numbers for A  : " +str(a1)+  "  " + str(a2)) 
print("Numbers for B  : " +str(b1)+ "  " + str(b2)) 
sumb=initb
suma=inita
while True:
    i=int(input("Enter hit(1) or  stand(0)"))
    if i ==1 and sumb<21:
        x = random.choice(test_list)
        print("you got number",str(x)) 
        sumb=initb+x
        initb=sumb
        print("Score of Mr.B=" ,sumb)
        if sumb >21:
            print("busted")
            break
        elif sumb==21:
            print("you won")
            break               
        
    if i==0 and suma<18:
        y = random.choice(test_list)
        print("you got number",str(y)) 
        suma=inita+y
        inita=suma
        print("Score of dealer=" ,sumb)
        if sumb >21:
            print(" dealer busted")
            break
        elif sumb==21:
            print("dealerwon")
            break 
        elif suma == sumb:
            print("Tie")
     