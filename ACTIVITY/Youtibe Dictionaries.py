#Sorting a dictionary using Sorted() Method
t={'a':7,'r':2,'k':3}
k=sorted(t)
print(k)
K=sorted(t.items(),reverse=True)
print(t)
import operator
sorted(sorted(t),key=operator.itemgetter(0))
print(t)

sales={'India':100,'China':500,'USA':800,'Uk':900,'Japan':700}
#r=sorted(sales)
#print(r)
import operator
k=sorted(sorted(sales),key=operator.itemgetter(1))
print(k)


#check whether the key is part of the dictionary or noy
if 'China' in sales:
    print(sales['China'])
print('India' in sales)