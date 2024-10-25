import array as arr 
num=arr.array('i', [10,200,130,40,50]) 
print("The array is:",num)  
maxVal = num[0] 
for i in range(1, 5): 
    if num[i] > maxVal: 
        maxVal = num[i]  
print ("Largest element in the given array is:",maxVal)
