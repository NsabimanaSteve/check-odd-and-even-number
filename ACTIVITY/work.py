def prime_num(num):
    list_a=[]
    for i in range(1, num):
        if num % i == 0:
            return False
        return True
           
    
    if num % 2 ==0:
        list_a=[]
    else:
        if num % num == 0 and num % 1 ==0:
                    list_a.append(num)
                    
    return list_a
                    
    
for i in range(3):
    user_input=int(input('Enter a nmuber:'))
    print(prime_num(user_input))