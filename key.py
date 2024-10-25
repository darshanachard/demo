d={1:10,2:20,3:30,4:40,5:50,6:60}
print("the dictionary is:",d)
key=int(input("enter key to check:"))
if key in d:
    print("key is present in the dictionary")
else:
    print("key is not present in the dictionary")
