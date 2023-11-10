def nested_sum(lst):
    total=0
    for inner_sum in lst:
        total+=sum(inner_sum)
    return total
t=[[1,2],[3],[4,5,6]]
result=nested_sum(t)
print(result)

def cumsum(t):
    cumulative_sum=[]
    num=0
    for i in t:
        num=num+i
        cumulative_sum.append(num)
    return cumulative_sum
t=[1,2,3]
print(cumsum(t))

def middle(lst):
    return lst[1:3]
t=[1,2,3,4]
print(middle(t))

def chob(lst):
    t.pop(0)
    t.pop(len(t)-1)
    
t=[1,2,3,4]
print(chob(t))

def is_sorted(lst):
    return lst==sorted(lst)

print(is_sorted([1,2,3]))
print(is_sorted(['b','A']))    
    

def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# Example usage:
print(has_duplicates([1, 2, 3, 2, 4]))  # True
print(has_duplicates([1, 2, 3, 4, 5]))  # False



    
        