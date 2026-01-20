import string
def rotate(text, key):
    code = '' #empty string to put the new code in
    alphabet = list(string.ascii_lowercase) #creates list of lowercase alphabet
    upper_alphabet = list(string.ascii_uppercase) #creates list of uppercase alphabet
    for i in text: #loop to inspect each character in the string
        if i.isalpha() == False: #if not a letter, keep it the same and add to the code
            code += i
        else: 
            if i.islower() == True: #if lowercase
                new_index = alphabet.index(i) + key - 26 *(1 + (key // 26)) #find the index of a letter in the alphabet and add the rotation to it
                new_letter = alphabet[new_index] #Using the mod of the key // 26 to ensure the new index always stays within 0 and 25 (index of the alphabet)
                code += new_letter
            if i.isupper() == True: #if uppercase
                upper_index = upper_alphabet.index(i) + key - 26* (1 + (key // 26))
                new_letter = upper_alphabet[upper_index]
                code += new_letter
    return code
