def fizbuz(checkNumber):
    if checkNumber % 3 == 0 and checkNumber % 5 == 0:
         print("FizzBUZZ" )
         print(checkNumber)
    elif checkNumber % 3 == 0:
        print("Fizz")
        print(checkNumber)
    elif checkNumber % 5 == 0:
        print ("Buzz")
        print(checkNumber)

numbers = [1,3,5,6,8,9,10,12,13,20,15,30,45,47,27,18]
for number in numbers:
    check = fizbuz(number)
