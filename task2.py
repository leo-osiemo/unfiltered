# from task1 import classroom

# def add_sugar(func):
#     def wrapper():
#         print("You have added sugar")
#         func()
#     return(wrapper)

# @add_sugar
# def get_coffee():
#     print("Here is your coffee")

# print(__name__)

# get_coffee()


import os
print(os.path.join(os.path.abspath(os.path.dirname(__file__)), "hello"))