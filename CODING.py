def pig_latin(word):

    first_vowel=""
    if word[0] not in 'aeiou' or word[0] not in 'AEIUO':
        
        for letter in word:
            if letter in 'aeiou':
                first_vowel  = letter
                break
            
        index_of_first_vowl= word.find(first_vowel)
        letter_before_first_vowel=word[: index_of_first_vowl]
            
        letter_after_first_vowel = word[index_of_first_vowl: ]
            
        new_word=letter_after_first_vowel + letter_before_first_vowel + 'ay' 
        return new_word
    else:
        other_word=  word+'way'
        return other_word
print(pig_latin('cry'))