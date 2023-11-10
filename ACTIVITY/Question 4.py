pi= "3.1415926535897932384626433832795028841971693993751"
my_dict={}
for char in pi:
    if char != ".":
        digit=int(char)
        if digit in my_dict:
            my_dict[digit] += 1
        else:
            my_dict[digit] = 1
#print(my_dict)
    
for digit, count in my_dict.items():
    print('The digit',digit,'has count',count)
    


        

            
        