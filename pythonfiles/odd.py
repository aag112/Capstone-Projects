numbers = list(range(1,11))
print(numbers)
for num in numbers:
  if num % 2 != 0:
    print('{}'.format(num) + " is an odd number")
print("these are all the odd numbers in the list")