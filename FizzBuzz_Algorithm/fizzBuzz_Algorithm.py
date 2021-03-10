#Project 2 - FizzBuzz Algorithm

#insert a number for the max of range
maxNumber = int(input('Insert a number for the max range: '))

#Add one blank line between the input and output
print()

#function range -> [x,y[
rangeInt = range(1,maxNumber + 1)

#for every number in the range
for number in rangeInt:

    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
