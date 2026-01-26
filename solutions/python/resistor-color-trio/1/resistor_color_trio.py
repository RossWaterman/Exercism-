def colors_list():
    return [
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white'
    ]

def label(colors):
    color_list = colors_list()        # NOTE: call the function
    color_1 = colors[0]
    color_2 = colors[1]
    color_3 = colors[2]
    value = int(str(color_list.index(color_1)) + str(color_list.index(color_2)) + ('0' * color_list.index(color_3)))
    if value < 10**3:
        return f'{value} ohms'
    if 10**3 <= value < 10**6:
        return f'{int(value/10**3)} kiloohms'
    if 10**6 <= value < 10**9:
        return f'{int(value/10**6)} megaohms'
    return f'{int(value/10**9)} gigaohms'
    
