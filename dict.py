# write a python program to create dictionary and perform add,update and delete items to dictionary
std={"reg":"111cs23039","name":"ram","college":"gptcpt"}
print("the given dictionary is:",std)
std["result"]="pass"
std["phone"]=9988776655
print("after added items:",std)
std["name"]="chandu"
print("after update items:",std)
std.pop("college")
print("after remove college key:",std)

