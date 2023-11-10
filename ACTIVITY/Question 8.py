def are_anagrams(ward1, ward2):
    if len(ward1) != len(ward2):
        return False
    
    my_dict1={}
    my_dict2={}

    for char in ward1:
        if char.isalpha(): #isalpha:used to check if a character is a letter

            if char in my_dict1:
                my_dict1[char]+=1
            else:
                my_dict1[char]=1
    
    for char in ward2:
        if char.isalpha(): #isalpha:used to check if a character is a letter

            if char in my_dict2:
                my_dict2[char]+=1
            else:
                my_dict2[char]=1
                
    return my_dict1 == my_dict2
                
#     for key,value in my_dict1.items():
#         if key in my_dict1 and value== my_dict2(key):
#             pass
#         else:
#             return False
        
user_input1=input('Enter the first string: ')
user_input2=input('Enter the second string: ')
user_input1=user_input1.replace(" ","").lower()
user_input2=user_input2.replace(" ","").lower()

if are_anagrams(user_input1, user_input2):
    print(user_input1,'and',user_input2, 'are anagrams')
else:
    print(user_input1,'and', user_input2, 'are not anagrams')

    



