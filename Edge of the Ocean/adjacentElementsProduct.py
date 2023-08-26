"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""
def solution(inputArray):
    largest_product = float('-inf')
    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if largest_product < product:
            largest_product = product
    return largest_product
