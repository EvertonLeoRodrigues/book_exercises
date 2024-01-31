
quantityOfNumbers = 0
sumOfIntegerNumbers = 0

while True:
    interegerNumber = int(input("Digit an integer number: digit \"0\" for exit "))
    sumOfIntegerNumbers+=interegerNumber
    if(interegerNumber == 0 ):
        print(quantityOfNumbers)
        print(f"The sum of the entered integers is {sumOfIntegerNumbers}")
        break
    quantityOfNumbers+=1