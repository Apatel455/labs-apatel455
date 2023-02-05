# Analysis and Reflection for Lab 1

## function 1:

Examine the ensuing function in relation to number.

Python defines function 1 as value, number.

If (number == 0): 1 operation returns 1; otherwise, 
if (number == 1): 1 operation returns value.

function1 * return value (value, number-1)

```

Time Complexity
Time Complexity T(n) = 1 + 1 + Function1(value, number - 1) = 2 + (2 + function1(value, number - 2)) = 2 + 2 + (2 + function1(value, number - 3))
before the function (value, 0)
As a result, this process will continue until the number reaches 0 = 2 + 2 + 2 + n times = 2n 
=> When the number is large, 2n is regarded as a n. Consequently, this function's time complexity is O. (n). The n stacks will be produced by this function. Therefore, it varies depending on the numbers.

## function 2:

Examine function 2 in relation to the mystring's length. For operator counting, we must build up two mathematical functions. both for recursive function2 and function2 respectively.

```python

def recursive function2(mystring,a,b): if(a >= b): / 1 operation return If the condition (mystring[a]!= mystring[b]) is true, then one operation should be returned. Return recursive function2(mystring,a+1,b-1) if false else.

return recursive function2(mystring, 0,len(mystring)-1) if function2(mystring) is defined.

```
=> The function executes whenever there are two operations. As a result, this function is called n/ 2 times. because a and b are shifting within one position every time. A and B will therefore relocate to the middle. Here, number denotes the string's length. In the worst scenario, n / 2 times of 2 operations are carried out. Thus, O is the temporal complexity (n). Here, the number also affects how intricate the space is. because n/2 will be created by this function.

T(n) = 2 * n / 2 = n is Time Complexity                     

### function 3 (optional challenge):

Examine the ensuing function in relation to number.

```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?
    => Recursive functions can be useful on occasion, in my opinion. First, I take note of the function and examine its behaviours. Recursive is simple to employ if the function is repetitious. Function will repeatedly call them, as in the factorial function. Recursiveness is the ideal option for us when we have a pattern, such as when we have the base condition and we are continuously decreasing the value.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 
    => Recursive functions require a base condition, which must exist. Because the end of the recursive function is the base condition Therefore, the same number of operations are performed in the recursive function with each function call. As a result, the argument always affects how complicated time and space are, and this is true for all functions. The operations that are multiplied during each function call and the number of function calls are what cause the time complexity.
    T(n) = number of operations * number of time function
            performed by one            calls
            function call
    On the other hand, in a non-recursive function, it depends on a variety of variables, including loops and the number of parameters. The degree of space complexity differs greatly amongst us. Because they use the stack for memory allocation, recursive functions consume more space than non-recursive functions. As a result, it will make copies of the same variables for the various functions. Recursion is thus only advantageous in the function with smaller arguments.
