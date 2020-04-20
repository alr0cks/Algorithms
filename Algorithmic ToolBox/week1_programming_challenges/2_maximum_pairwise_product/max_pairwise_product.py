# python3

'''
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
'''
def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_product = 0
    index1 = -1
    for first in range(n):
    	if index1 == -1 or numbers[first] > numbers[index1]:
    		index1 = first
    #print(index1)
    index2 = -1
    for second in range(n):
    	if index2 == -1 or numbers[second] > numbers[index2] and index1 != second:
    		index2 = second
    #print(index2)


    max_product = max(max_product,
            numbers[index1] * numbers[index2])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
