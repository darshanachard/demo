def factorial(num):
    fact=1
    while(num!=0):
        fact=fact*num
        num=num-1
        print("factioral is",fact)
        
num=int(input("enter the number to find factorial:"))
factorial(num)
