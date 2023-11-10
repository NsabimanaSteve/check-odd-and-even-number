def low_upper_count(string):

   counter = {"lower" : 0, "upper" : 0}
   
   for i in string:
       if i.islower():
           counter["lower"]+=1
           
           
       if i.isupper():
           counter["upper"] +=1
   return counter


user = input("Enter the string: ")

print(low_upper_count(user))