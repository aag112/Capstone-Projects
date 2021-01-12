#Coding Puzzle #1

#Sum of integers

#Write a function which takes one parameter e.g. ‘num’ as input and returns the sum of the integers from zero to the input parameter.

#The function should return 0 if a non-integer is passed in with a message stating ‘wrong input...BYE!’

#Note.
#Write the final script in a ”.py” using VSCode and submit the file itself!!
def getSum(num = int(input("enter a number: "))):  
    if type(num) != int:
      print('0') 
    sum = 0
    for digit in str(num):   
      sum += int(digit)        
    return sum
    

print(getSum(num))


    