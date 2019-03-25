#!/usr/bin/python

import math
'''
1) Understand the problem
    - compare two dictionaries (recipes, ingredients)
    - write a function that will return the number of batches that can be made
    - Will the dictionaries always have the same keys and indexes?
    - if one ingredient is less that the recipe needs returns 0
2) Devise a plan
    - iterate through recipe dict and compare it to ingredient dict
3) Carry out plan
4) Looking back
'''
def recipe_batches(recipe, ingredients):
    for key, value in  recipe.items():
        print(key, value)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))