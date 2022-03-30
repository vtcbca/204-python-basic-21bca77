n=int(input("Enter any number:"))
sum=0
for i in range(1, n+1):
    print(i, end=' ')
for i in range(1,n):
    sum=sum+i
    i=i+1
print("Sum of 1 to {} number is: {}".format(n,sum))
