#Programa que lê cédulas
from decimal import Decimal
while(True):
    value =Decimal(input("Digit the value for payment: "))
    if(value==Decimal("0")):
        break
    else:
        ballots = 0
        current = Decimal("100.00")
        unpaid = value

        while True:
            
            if current <= unpaid:
                unpaid -= current
                ballots += 1
            else:
                if ballots>0:
                    print(f"{ballots} banknotes of ${current:.3f}!")
                    print(f"current value for payment is: {unpaid:.2f}!")
                if unpaid == Decimal("0"):
                    break
                elif current == Decimal("100"):
                    current = Decimal("50")
                elif current == Decimal("50"):
                    current = Decimal("20")
                elif current == Decimal("20"):
                    current = Decimal("10")
                elif current ==Decimal("10"):
                    current = Decimal("5")
                elif current == Decimal("5"):
                    current = Decimal("1")
                elif current == Decimal("1"):
                    current = Decimal("0.50")
                elif current == Decimal("0.50"):
                    current = Decimal("0.10")
                elif current == Decimal("0.10"):
                    current = Decimal("0.05")
                elif current == Decimal("0.05"):
                    current = Decimal("0.01")
                elif current == Decimal("0.01"):
                    current = Decimal("0.001")
                ballots = 0