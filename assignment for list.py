a=[1,2,3,4]
b=a[:]
print(b)
b[0]=5
print(b)


# Start with an empty list
myList = []

# Use append to add the first item (76)
myList.append(76)

# Use append to add the second item (92.3)
myList.append(92.3)

# Use append to add the third item ("hello")
myList.append("hello")

# Use concatenation to add the fourth item (True)
myList += [True]

# Use concatenation to add the fifth item (4)
myList += [4]

# Use concatenation to add the sixth item (76)
myList += [76]
print(myList)

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

def sum_of_square(xs):
    total = 0
    for num in xs:
        total =total + num**2
    return total
xs=[2,3,4]
result = sum_of_square(xs)
print(sum_of_square(xs))



def my_count(list, item):
    count = 0
    for element in list:
        if element == item:
            count += 1
    return count

# Custom implementation of in
def my_in(list, item):
    for element in list:
        if element == item:
            return True
    return False

# Custom implementation of reverse
def my_reverse(lst):
    return list[::-1]
def my_reverse(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list


#implementation of index
def my_index(list, item):
    for i, element in enumerate(lst):
        if element == item:
            return i
    raise ValueError(f"{item} is not in list")

#implementation of insert
def custom_insert(list, index, item):
    if index < 0:
        index = 0
    elif index > len(lst):
        index = len(lst)
    lst[index:index] = [item]

# Example usage:
my_list = [1, 2, 2, 3, 4, 5]
print(custom_count(my_list, 2))  # Should print 2
print(custom_in(my_list, 4))  # Should print True
print(custom_reverse(my_list))  # Should print [5, 4, 3, 2, 2, 1]
print(custom_index(my_list, 3))  # Should print 3
custom_insert(my_list, 2, 99)
print(my_list)  # Should print [1, 2, 99, 2, 3, 4, 5]




   