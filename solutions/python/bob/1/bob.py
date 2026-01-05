def response(hey_bob):
    if hey_bob.isupper():
        if hey_bob.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"      
    if hey_bob.strip().endswith('?'):
        return "Sure."
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    return "Whatever."
