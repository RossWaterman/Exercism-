def is_valid(isbn):
    isbn_formatted = [] #empty list to recreate isbn without dashes
    isbn_formula = 0 #defining a variable for the final value after the numbers are inputted to the formula
    d_numbers = list(range(1,11)) #list from 1 -> 10 to loop over.
    for i in isbn: 
        if i.isnumeric():
            isbn_formatted.append(int(i)) # adds the numbers to isbn_formatted
        if  i.lower() == 'x' and isbn.endswith(('X', 'x')):
            isbn_formatted.append(10) #adds x as 10 only if it's at the end of the isbn
        if i.lower().isalpha() and i.lower() != 'x': #for any other letter, return false
            return False
    if len(isbn_formatted) != 10: #if the number inputted is not the correct size, return false
        return False
    for d in d_numbers:
        isbn_formula += (isbn_formatted[d-1] * d_numbers[-d]) #adding values to isbn_formula. The first term indexes the isbn_formatted to start from the first digit and the negative index on d_numbers will start it from the last value (10), replicating the formula given.
    return isbn_formula % 11 == 0 #if mod 11 of the final value = 0 then ISBN valid.
    
    
