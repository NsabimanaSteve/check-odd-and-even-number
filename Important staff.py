s='6.00 is 6.0001 and 60002'
new_string=''
new_string+=s[-1]
new_string+=s[0]
new_string+=s[4::30]
new_string+=s[13:10:-1]

print(new_string)
x="steve"
print(x[2::8])

print(x[::])
print(x[0:len(x):1])
print(x[:])
print(x[0:])
print(x[:len(x)])
print(x[:7])
print(x[0::1])
print(x[0:5:1])
print(x[::-1])
print(x[::-2])
print(x[-1:(-len(x)+1):-1])
