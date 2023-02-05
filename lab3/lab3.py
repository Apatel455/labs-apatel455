#
# Author: Aastha Patel
# Student Number: 125019216
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#





# function 1

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


# print(factorial(5))

# function 2

def linear_search(list, key):
    return recursive_linear_search(list,key,0)

def recursive_linear_search(list,key,index):
    if list == None or len(list) == 0:
        return -1
    else:
        if list[0] == key:
            return index
        else:
            return recursive_linear_search(list[1:], key, index + 1)


# print(linear_search([1,2,3,4,5,6,7], 6))

# function 3 

def binary_search(list, key):
    return recursive_binary_search(list,key,0,len(list) - 1)

def recursive_binary_search(list,key,low,high):
    mid = (low + high) // 2

    if low > high:
        return -1
    else:
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            return recursive_binary_search(list,key,mid + 1, high)
        else:
            return recursive_binary_search(list,key,low,mid - 1)

# print(binary_search([1,2,3,4,5], 4))

