import random

def coin(n):
    headcount=0
    tailcount=0
    for i in range(n):
        num=random.randint(1,2)
        print(check1(num))
        if check1(num)=='Heads':
            headcount+=1
        else:
            tailcount+=1
    print('Heads:',headcount)      
    print('Tails:',tailcount)

def check1(num):
    if num==1:
        return 'Heads'
    else:
        return 'Tails'

    
coin(100)
    
