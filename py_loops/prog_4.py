num = int(input("enter a number:"))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse = 10
    num =  num //10
if original ==  reverse:
    print("palindrome number")
else:
    print("not a palindrome number")        