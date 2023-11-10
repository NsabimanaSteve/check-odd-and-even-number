'''recurision is programming techniques where a function calls itselt
some imprtant of recuusion:
1. Recursion may be simpler, more intuitive
2. Recursion may be efficient from programmer POV
3. Recursion ,may not be efficienty from computer POV
'''


def recursion(a,b):
    result=0
    while b > 0:
        result +=a
        b-=1
    return result
res=recursion(3,3)
print(res)

'''a=a+a+a+a+.......+a
a=a*b-1
'''

def recursion(a,b):
    if b==1:
        return a
    else:
        return a+a*(b-1)
res=recursion(3,3)
print(res)

def fact(n):
    prod=1
    for i in range(1,1+n):
        prod*=i
    return prod
res=fact(4)
print(res)

#n!=n*(n-1)*(n-2)*....(n-n)
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(4))

def fab(n):
    if n ==0:
        return 0
    elif n==1 or n ==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(7))

#Palindrome
def ispalindrome(s):
    
    def tochars(s):
        s = s.lower()
        ans=''
        if c in 'abcdefghigklmnopqrstuvwxyz':
            ans=ans+c
        def ispal(s):
            if len(s) <= 1:
                return True
            else:
                return s[0] == s[-1] and ispal(s[1:1])
            return ispal(tochars(s))
print(ispalindrome(''))


'''effernce between list and dict
1. List is ordered sequence of elements while
    dictionaries  maches 'key' to values
2. Look up elements by an integer index while Dictionaries
look up one item by anather item
3. Indeces habe an order while no orger is guaranted
4. index inans integer while key can be any immutable type 


'''

def lyrics_to_freqeuncy(lyriscs):
    my_dict={}
    for word in lyrics:
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1
    return my_dict
result = lyrics={'ste','sdfd','dff','love'}
lyrics_to_freqeuncy(result)
print(result)           
                
            

    