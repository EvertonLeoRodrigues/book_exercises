initialDeposit = float(input("Digit your initial deposit: "))
interestRate = int(input("Digit the interest rate: "))

month = 0
finalBalance = initialDeposit
interestRateValue = initialDeposit*interestRate/100


while(month<=24):
    finalBalance+=(initialDeposit*interestRate/100)
    print(finalBalance)
    month+=1

print(finalBalance)

