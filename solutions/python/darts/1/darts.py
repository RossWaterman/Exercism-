def score(x,y):
    score = 0
    radius = ((x)**2 + (y)**2)**0.5 #use pythagoras to find the radius
    if radius > 10: #set the conditions for scoring
        return score
    if (10 >= radius > 5):
        return score + 1
    if 5 >= radius > 1:
        return score + 5
    else:
        return score + 10

