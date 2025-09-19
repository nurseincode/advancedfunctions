# Higher-order functions
# Wrapper - Wraps a function for additional functionality

# numbers = [5, 7, 2, 3]

# # def squares(nums):
# # Builds a new list with the result of
# # calling cb on each item in the list
# # def with_list(nums, cb):
# #     result = []
# #     for n in nums:   # Apply the callback function to the current number (n)
# #         # result.append(n ** 2)
# #         result.append(cb(n)) # Add the result to the new list
# #     return result

# def square(n):
#     return n * n

# def cube(n):
#     return n ** 3

# # Main 
# -->> map () HOF

# # print(with_list(numbers, cube)) # One generic cb function 'with_list' reused with square, cube
# result = map(square, numbers) # map iterator takes function first, then an iterable
# print(result)
# # print(list(result)) 
# print(list(map(lambda x: x ** 2, numbers))) # square list with lambda


# numbers = [5, 7, 2, 3]
# without cb
# def with_list(nums):
#     result = []
#     for n in nums:
#         result.append(n ** 2)
#     return result

# def cube_list(nums):
#     result = []
#     for n in nums:
#         result.append(n ** 3)
#     return result

# my_square = with_list(numbers)
# print("Squared:", my_square)



#  -->> Filter HOF

numbers = [5, 7, 2, 3]

def square(n):
    return n * n

def cube(n):
    return n ** 3

# Main 

print(list(map(lambda x: x ** 2, numbers))) # 

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens)) # 2 is the only even, output: [2] because 2 != [2]