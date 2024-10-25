def addition(num):
    if num<=1:
        return num
    else:
        return num +addition(num-1)

num=int(input("enter the number:"))
res=addition(num)
print(res)
