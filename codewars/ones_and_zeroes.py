'''
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
However, the arrays can have varying lengths, not just limited to 4.
'''

def binary_array_to_number(arr):
    return int(''.join(str(l) for l in arr), 2)

print(binary_array_to_number([0,0,1,1]))

'''
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)

def binary_array_to_number(arr):
    return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))

def binary_array_to_number(arr):
    append_bit = lambda n, b: n << 1 | b
    return reduce(append_bit, arr)
'''