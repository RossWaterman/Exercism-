def colors():
    return [
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white'
    ]

def value(color):
    color_list = colors()        # NOTE: call the function
    color_1 = color[0]
    color_2 = color[1]
    return int(str(color_list.index(color_1)) + str(color_list.index(color_2)))

