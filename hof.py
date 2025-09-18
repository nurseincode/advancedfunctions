# Higher-order functions
# Wrapper - Wraps a function for additional functionality

numbers = [5, 7, 2, 3]

# def squares(nums):
# Builds a new list with the result of
# calling cb on each item in the list
def with_list(nums, cb):
    result = []
    for n in nums:
        # result.append(n ** 2)
        result.append(cb(n))
    return result

def square(n):
    return n * n

def cube(n):
    return n ** 3

# Main 
print(with_list(numbers, square))