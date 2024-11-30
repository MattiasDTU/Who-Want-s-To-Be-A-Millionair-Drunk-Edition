WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GRAY_COLOR = (128, 128, 128)
GOLD_COLOR = (255, 215, 0)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)

import random



import random

def TAKE_SHOT(original_list, important_value):
    """
    Generates a new list with one random value removed from the original list,
    while ensuring the important value is always included.

    :param original_list: List of elements.
    :param important_value: The value that must always be included in the new list.
    :return: A new list with one less value and the important value included.
    """
    if important_value not in original_list:
        raise ValueError("The important value is not in the original list.")
    
    # Ensure there are other values to remove
    if len(original_list) == 1 and original_list[0] == important_value:
        return original_list  # Nothing to remove

    # Get a list of candidates for removal, excluding the important value
    removable_candidates = [value for value in original_list if value != important_value]
    
    # Randomly select a value to remove
    value_to_remove = random.choice(removable_candidates)
    
    # Create a new list excluding the randomly selected value
    new_list = original_list[:]
    new_list.remove(value_to_remove)

    return new_list


import random

def FITTYFITTY(original_list, important_value):
    """
    Generates a new list with two random values removed from the original list,
    while ensuring the important value is always included.

    :param original_list: List of elements.
    :param important_value: The value that must always be included in the new list.
    :return: A new list with two less values and the important value included.
    """
    if important_value not in original_list:
        raise ValueError("The important value is not in the original list.")
    
    # Ensure there are enough values to remove
    if len(original_list) <= 2 and important_value in original_list:
        raise ValueError("Not enough values to remove two while keeping the important value.")
    
    # Get a list of candidates for removal, excluding the important value
    removable_candidates = [value for value in original_list if value != important_value]
    
    # Randomly select two values to remove
    values_to_remove = random.sample(removable_candidates, 2)
    
    # Create a new list excluding the selected values
    new_list = original_list[:]
    for value in values_to_remove:
        new_list.remove(value)

    return new_list


new_list = [5,2,3,4,1]

newlist = []
new_list.remove(5)
print(new_list)