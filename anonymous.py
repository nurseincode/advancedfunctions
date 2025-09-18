import time

def greet(name, cb):
    print(f'Hello, {name}!')
    cb() 

# def say_bye():
#     print('Bye!')

# Main
# greet('Faith', say_bye)
greet('Faith', lambda: print('Bye!')) 



