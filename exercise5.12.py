#Altere o programa anterior (5.11) de forma a perguntar também o valor depositado 
#mensalmente. Esse valor será depositado no inicio de cada mês, e você deve considerá-lo
#para o cálculo de juros do mês seguinte.

initialDeposit = float(input("Digit your initial deposit: "))
monthlyDepositedAmount = float(input("Digit the monthly deposit amount: "))
interestRate = int(input("Digit the interest rate: "))

month = 0
finalBalance = initialDeposit
interestRateValue = initialDeposit*interestRate/100

print(monthlyDepositedAmount)
while(month<=24):
    finalBalance+=monthlyDepositedAmount
    finalBalance+=(initialDeposit*interestRate/100)
    
    print(f"{finalBalance:.2f}")
    month+=1
print(f"the final value is {finalBalance:.2f}")



