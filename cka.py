cube=27
epsilon=0.01
num_guesses=0
low=0
high=cube
guess=(high+low)/2
while abs(guess**3-cube)>=epsilon:
    if guess**3< cube:
        low=guess
    else:
        high=guess
    guess=(high+low)/2
    num_guesses+=1
print('num_guess=',num_guesses)
print(num_guesses,'is closer to the cube root of',cube)
