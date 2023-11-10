input_string=input('Enter a string: ')
input_string = input_string.lower()

my_dict= {}

for char in input_string:
    if char.isalpha(): #isalpha:used to check if a character is a letter 
        if char in my_dict:
            my_dict[char]+=1
        else:
            my_dict[char] = 1


 
for key,value in sorted(my_dict.items()):
    print(key,value)

    
    
    