"""
------------------------------------------------------------------------
CP164 Assignment 02, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food_utilities import read_food, calories_by_origin

gulab_jamun = read_food('Gulab Jamun|2|True|300')

spanakopita = read_food('Spanakopita|5|True|260')

avg = calories_by_origin([gulab_jamun, spanakopita], 2)

print(f"Average Calories: {avg}")