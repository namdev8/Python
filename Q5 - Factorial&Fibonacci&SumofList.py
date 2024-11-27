n=int(input("Enter a number:"))
factorial=1
if n>=1:
    for i in range(1, n+1):
        factorial=factorial*i

print("Factorial of the given number is:", factorial)

n=int(input("Enter the number of the terms: "))
a,b=0,1
print("fibonacci series:")
for i in range(n):
    print(a)
    a,b=b,a+b

list_numbers=[6,7,8,9,2,4]
print("Elements in the list are: ",list_numbers)
total=sum(list_numbers)
print("The sum of all elements in the list is:",total)
