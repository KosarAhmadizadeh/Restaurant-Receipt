#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fee(food):
    if food=='pizza':
        return(100.0)
    if food=='fish':
        return(150.0)
    if food=='salad':
        return(50.0)
    if food=='steak':
        return(200.0)
    if food=='soup':
        return(40.0)
    
def change(f):
    for i in range(len(f)):
        f[i] = f[i].split(" ")
    for i in range(0,len(f)):
        for j in range(0,len(f[i])-1):
            if f[i][j] == '':
                f[i].remove(f[i][j])
    for i in range(0,len(f)):    
        for j in range(i+1,len(f)):       
            if f[i][0] == f[j][0]:
                f[i][1]= str(int(f[i][1])+int(f[j][1]))
                f.remove(f[j])
                
                
def price_bill(service):
    sum=0
    for i in range(0,len(f)):
        sum += fee(f[i][0])*int(f[i][1])
    if service=="takeout":
        sum+=10.0
    if service=="table":
        sum+=sum*0.1
    return sum



m = 1
serve = []
all_bills = []
removed = []
income = 0
waiting = []
while(True):
    order = input()
    if order == 'take':
        bill_num = 100 + m
        all_bills.append(bill_num)
        waiting.append(bill_num)
        in_out = input()
        f = input().split(',')# f is foods
        change(f)
        print("\n")
        print("bill no.:",' '*(6-len(str(bill_num))),bill_num)
        for i in range(0,len(f)):
            print(f[i][0]," "*(6-len(f[i][0])),":",' '*(6-len(f[i][1])),f[i][1],' '*(6-len(f[i][1])),fee(f[i][0]),' '*(6-len(f[i][1])),fee(f[i][0])*int(f[i][1]))
        s=0
        for i in range(0,len(f)):
            s+=int(f[i][1])*fee(f[i][0])
        if in_out == "takeout":
            tax=10.0
        if in_out == "table":
            tax=s*0.1
        print("tax"," "*3,":"," "*2,tax)
        print("total"," "*1,":"," "*2,price_bill(in_out))
        income += price_bill(in_out)
        print("\n")
    elif order == "cancel":
        m-=1
        cancel = int(input())
        for i in range(0,len(serve)):
            if waiting[i] == cancel:
                waiting.remove(waiting[i])
                print("removed")
                bill_num-=1
                income -= price_bill(in_out)
            else:
                print("not found")
    elif order == "exit":
        break
    elif order == "income":
        m-=1
        print("income  :  ",income)
    elif order == "serve":
        m-=1
        served = int(input())
        for j in range(0,served):
            serve.append(waiting[j])
        for i in  range(0,served):  
            waiting.remove(waiting[i])
    else:
        m-=1
        print("invalid input")
    m+=1

    

