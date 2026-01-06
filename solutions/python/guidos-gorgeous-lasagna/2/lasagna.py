"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

PREPARATION_TIME = 2
EXPECTED_BAKE_TIME = 40



def bake_time_remaining(elapsed_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_time



# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    
    """Calculate the preparation time required.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).
    
    Returns preparation time by multiplying PREPARATION_TIME by number_of_layers.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(layers, elapsed_time):
        
    """Calculate the total elapsed time including preparation.
    
    :param layers: int - the number of layers in the lasagna.
    :param elapsed_time: int - time already spent baking (in minutes).
    :return: int - total elapsed time (preparation + baking).
    
    Combines preparation time (based on layers) with actual baking time elapsed.
    """
    return PREPARATION_TIME * layers  + elapsed_time



