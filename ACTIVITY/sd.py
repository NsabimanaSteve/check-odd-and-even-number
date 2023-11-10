
t2={'t':2,'t1':3}
print(t2)
del t2['t']
t2.update({"t3":8})
#t2[3]='t2'
print(t2)
del t2['t1']
print(t2)
t2['b']=2
t2['a']=1
print(sorted(t2.items()))

t4={'o':34,'y':34}
d={**t2,**t4}
print(d)
t5={'ol':34,'yz':34}
s=d.copy()
s.update(t5)
print(s)
