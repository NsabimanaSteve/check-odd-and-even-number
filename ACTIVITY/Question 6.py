def unique_charachaters(word):
    my_dict={}
    for char in word:
        
            if char in my_dict:
                my_dict[char] += 1
                
            else:
                my_dict[char] = 1
    return my_dict
user_input=input('Enter the word: ').lower()

count=unique_charachaters(user_input)
print(count)
count_len=len(count)
print(user_input,'has',count_len,'unique characters')


            
        