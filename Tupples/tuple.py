#List and tuple

y=(1,2,3)
x=['c','b','aa']
print(zip(y,x))
for pair in zip(y,x):
    print(pair)
    
r=list(zip(x,y))
print(r)
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)

#dictionaries and tuples

d={'w':2,"k":4,"t":6}
r=d.items()
p=dict(r)
print(p)
print(r)
d={'w':2,"k":4,"t":6}
r=d.keys()
print(r)

d={'w':2,"k":4,"t":6}
r=d.values()
print(r)



#combination of zip and range to make a dictionary
o=dict(zip('abs',range(3)))
print(o)

    
    