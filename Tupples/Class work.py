def calculate_average(some_list):
    some_of_numbers=sum(some_list)
    number_of_items=len(some_list)
    
    return some_of_numbers/number_of_items
example_list=[1,2,3,4,5]
result=calculate_average(example_list)
print(result)

