def coint_degit_occurences(number):
    number_str=str(number)
    my_dict={}
    
    for char in number_str:
        if char  != '.':
            digit=int(char)
            if digit in my_dict:
                my_dict[digit]+=1
            else:
                my_dict[digit] = 1
    return my_dict
                
float_numbers = 1.332
counts=coint_degit_occurences(float_numbers)
print(counts)



    