#!/bin/python3

list=["Apple", "Orange", "Banana", "Pomgrenate", "Grapes"]

print(list)

print(list[0])

print(list[1:3]) #returns the first index numbergiven right until the last index number, but not including the last number item

print(list[1:]) # return the first index number item until the last item

print(list[:2]) # return all items before the second index number

print(list[-1]) # returm the last item

print(list[-2]) # returm the second last item

print(len(list)) #return the length of the list 

print(len(list[-1])) # return the length of last item


list.append("Watermelon") # Append to the end of the list

list.insert(3,"Pineapple") #Inserts at index 3

list.pop() # removes the last item

list.pop(3) # removes the item at index 3

list2=["Tomato", "Potato"]

list3=list+list2;

print(list3)

# 2D Lists
twodList=[["Apple",100],["Orange",90],["Watermelon",110]]

print(twodList[0][1]) # prints 100
print(twodList[1][1]) # prints 90
print(twodList[2][1]) # prints 110

print(twodList[0][0]) # prints Apple
print(twodList[0][-2]) # prints Apple
print(twodList[0][-1]) # prints 100



