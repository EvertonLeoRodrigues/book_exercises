#The temperature list of Mons, in Belgium, has been stored in the list T = [-10, -8, 0, 1, 2, 5, -2, -4]
#Write a program that prints the smallest and largest temperature, as well as the avarege temperature.


l = [-10,-8,0,1,2,5,-2,-4]

smallest = l[0] 
largest = l[0]
sumTemperature = 0
for item in l:
    sumTemperature+=item
    if item<smallest:
        smallest = item
    if item>largest:
        largest = item
print(f"The largest temperature that has been stored is {largest} degrees!")
print(f"The smallest temperature that has been stored is {smallest} degrees!")
print(f"The avarege temperature is {(sumTemperature/len(l)):.0f} degrees!")