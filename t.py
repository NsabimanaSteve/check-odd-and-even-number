#Approximation of solution-cube root
cube=27
epsilon=0.01
guess=0.0
increment=0.0001
num_guesses=0
while abs(guess**3-cube)>=epsilon:
    guess+=increment
    num_guesses+=1
print('num_guess=',num_guesses)
if abs(guess**3-cube)>=epsilon:
    print('Failed on cube root of',num)
else:
    print(guess,'is close to the cube of',cube)