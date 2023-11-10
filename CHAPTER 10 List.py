"""List is the sequence of value. The value can be elements or sometime items
List are mutable.
When you use method, it return None since you have change the elements that is
in the list. It becomes void. While for string are Immutable. When you use method it returns value not None"""

x=[1,2,3]
y=[9,8]
x.append(y)
print(x)
x.extend(y)
print(x)

#possible way of making copy in the list
x=[1,2,3]
copy_x=x[:]
print(x)

x=[1,2,3]
y=[]
print(x+y)

x=[1,2,3]
z=x.copy()
print(z)


my_list=[1,2,3]
for index,element in enumerate(my_list):
    print(index,element)

#list concatination is the same as you use method Extend

a=[3,13]
b=[2,4]
z=a+b
print(z)


a=[3,13]
b=[2,4]
a.extend(b)
print(a)


