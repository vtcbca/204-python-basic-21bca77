n=int(input("enter the number:"))
temp=n
rev=0
while(temp>0):
    reminder=temp%10
    rev=(rev*10)+reminder
    temp=temp//10
if(n==rev):
    print("number is palindromic")
else:
    print("number is not palindromic")
