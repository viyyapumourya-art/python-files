num = int(input("enter a number:"))
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*1 + digit
    num = num//10

print("reversed number:",reverse)