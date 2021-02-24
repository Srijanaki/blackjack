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


i=int(input("Mr B : Enter hit(1) or  stand(0)"))
if i==1:
    sumb=0
    while True:
         if sumb<21:
            x = random.choice(test_list)
            print("you got number",str(x)) 
            sumb=initb+x
            initb=sumb
            print("Score of Mr.B=" ,sumb)
         else:
            if sumb==21:
                print("you won")
                break
            else:
                print("Busted")
                break        
if i==0:
    suma=0
    sumb=initb
    while True:
         if suma<17:
             y = random.choice(test_list) 
             print("you got number ",str(y)) 
             suma=inita+y
             inita=suma
             print("Score of dealer=" ,suma)
         else :
            if suma > sumb and suma<21:
                print("Dealer won")
                break
            elif suma ==  sumb:
                print("Tie")
                break
            else:
                print("busted")