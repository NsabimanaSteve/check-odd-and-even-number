def OddEvencount(numbers):
    dict={'odd':0,'even':0}
    for num in numbers:
        if num % 2 != 0:
            dict['odd'] += 1
        else:
            dict['even']+=1
    return dict
int_list=[0,2,3,4]
print(OddEvencount(int_list))