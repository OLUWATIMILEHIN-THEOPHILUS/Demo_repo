                            # FizzBuzz Coding Interview

# This is the question I found online: The FizzBuzz problem is a classic test given in coding interviews. The task is simple: Print integers 1 to N, but
# print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer
# is divisible by both 3 and 5.

# But then, I decided to get more handy and came up with this;

N = int(input('Hi, please input an integer: '))

if N % 3 == 0 and N % 5 == 0:
    print('FizzBuzz')
elif N % 3 == 0:
    print('Fizz')
elif N % 5 == 0:
    print('Buzz')
else:
    print('N is neither divisible by 3 nor 5')


  
# Swapping two variables in python
#     (Note that method 1 & 2 only work for numbers likewise consume more/extra bit, unlike method 3
# which works for both numbers and strings and consumes less bit)
#         (Note; you can also do this by setting a third variable)
a = 14
b = 43

# Method 1
# a = a + b
# b = a - b
# a = a - b

# Method 2 (using XOR)
# a = a ^ b
# b = a ^ b
# a = a ^ b

# Method 3
# a,b = b,a

#setting a third variable

swap = a
a = b 
b = swap

print(a)
print(b)
