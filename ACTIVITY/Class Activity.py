import random

def simulate_diceroll():
    "1,2,3,4,5,6"    
    first, second=random.randrange(1,7),random.randrange(1,7)
    return first + second

def display_table(sample_dictionary):
    print("Total\tFrequency\tStimulated %\tExpected %")
    for key, value in sample_dictionary.items():
        frequency = value
        percentage = (value / 1000) * 100
        expected_percentage = (1/36) * 100  # 1/36 is the probability of getting each total
        print(f"{key}\t{frequency}\t\t{percentage:.2f}%\t\t{expected_percentage:.2f}%")

def main():
    my_dict = {}
    for i in range(1000):
        total = simulate_diceroll()
        if total not in my_dict:
            my_dict[total] = 1
        else:
            my_dict[total] += 1
    display_table(my_dict)

main()
