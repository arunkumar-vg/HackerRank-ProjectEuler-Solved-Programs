#!/bin/python3

limit=int(input())
arr=[]
for i in range(0,limit):
    value=int(input())
    arr.append(value)
    n=arr[i]
    sos=0
    son=0
    res=0
    son=n*(n+1)//2
    sos=n*(n+1)*((2*n)+1)//6
    res=(son*son)-sos
    print(res)