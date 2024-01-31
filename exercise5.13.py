debt = float(input("Digit you debt: "))
monthlyInterestRate = int(input("Digit the monthly interest rate: "))
monthlyPaymentValue = float(input("Digit the value of monthly payment: "))

quantityOfMonths = 0
currentDebit = debt

while(currentDebit >= 0):
    currentDebit+=monthlyInterestRate
    if(currentDebit<monthlyPaymentValue):
        currentDebit-=currentDebit
        print(currentDebit)
        print(f"The current debt value is {currentDebit}, thanks for the payment!")
        break
    currentDebit-=monthlyPaymentValue
    print(f"The current debt value is {currentDebit}")
    quantityOfMonths+=1

print(f"The quantity of months to complete payment is {quantityOfMonths} months")
