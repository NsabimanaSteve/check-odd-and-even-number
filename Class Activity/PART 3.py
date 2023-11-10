#Append “apple” and 76 to the list.
myList=[76,92.3,"hello",True,4,76]
other_list=["apple",76]
myList.append(other_list)
print(myList)

#Insert the value “cat” at position 3.
myList=[76,92.3,"hello",True,4,76]
myList[3]="cat" 
print(myList)

#Insert the value 99 at the start of the list.
myList=[76,92.3,"hello",True,4,76]
myList[0]= 99
print(myList)

#Find the index of “hello”.
myList=[76,92.3,"hello",True,4,76]
y="hello" 
index=myList.index(y)
print(index)

#Count the number of 76s in the list.
myList=[76,92.3,"hello",True,4,76]
element=76
count=myList.count(element)
print(count)

#Remove the first occurrence of 76 from the list.
myList=[76,92.3,"hello",True,4,76]
x=myList[0]
myList.remove(x)
print(myList)
#Remove True from the list using pop and index.
myList=[76,92.3,"hello",True,4,76]
myList.pop(3)
print(myList)