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

x=[1,2,3]
y=
copy_x=x[:]

print(x)