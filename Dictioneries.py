d={'steb':2,3:'s'}

def reverse_lookup(dictonary, value_to_lookfor):
    for key in dictonary:
        if dictonary[key] == value_to_lookfor:
            return key
    return "key not found"

result=reverse_lookup(d,2)
print(result)