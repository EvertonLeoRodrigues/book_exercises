#Modify de program 6.11 to print the smallest value of the list.

l = [1,7,2,4]
greatest = l[0]
smallest = l[0]
for e in l:
    if e>greatest:
        greatest = e
    if e<smallest:
        smallest = e
print(greatest)
print(smallest)