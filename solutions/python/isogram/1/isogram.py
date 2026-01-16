def is_isogram(string):
    formatted_string = ''.replace(' ', '')
    for n in string:
        if n.isalpha():
            formatted_string +=n.lower()
    words = string.split()
    checked_words = ''
    for i, char in enumerate(formatted_string):
        checked_words += char.lower()
        if formatted_string[i].lower() in formatted_string[i+1:].lower():
            break
    return formatted_string == checked_words
    



    


