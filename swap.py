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
