from functools import reduce

numbers = [10, 20, 22, 25, 29, 35]
summed_up = reduce(lambda x, y: x + y, numbers)
print(summed_up)

print(max(numbers))  #to get the maximun number
print(min(numbers))  #minimum  number

#using lambdas

maximum_value = reduce(lambda x, y: max(x, y), numbers)
minimum_value = reduce(lambda x, y: min(x, y), numbers)

print(maximum_value)
print(minimum_value)