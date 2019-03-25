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
    - create a list of comparisons between dict values
    - get the floor of the difference between the dictionary values at each key
    - return the lowest value in batches list
        (represents max total batches across all ingredients)
3) Carry out plan
4) Looking back
    - i think this is O(n) time
    - if thats true then I think thats a good solution'''


def recipe_batches(recipe, ingredients):
    batches = []
    if recipe.keys() == ingredients.keys():
        for k in recipe:
            batches.append(ingredients[k] // recipe[k])
            return min(batches)
    else:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print('''{batches} batches can be made from the
    available ingredients:{ingredients}.'''.format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
