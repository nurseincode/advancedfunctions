import time

def greet(name, cb):
    print(f'Hello, {name}!')
    # time.sleep(2) # Program pauses here
    cb() # Runs after the pause

def say_bye():
    print('Bye!')

def shout():
    print('GOODBYE!!')


# Main
greet('Faith', say_bye) # say_bye function passed as a variable, cb
greet('Tim', shout)
print('Continuing main ...')


