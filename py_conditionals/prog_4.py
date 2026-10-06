pin = int(input("enter pin:"))
account_balance= 9999999999
if pin == 3344:
    amount = int(input("enter withdrawl amount:"))
    if amount <= account_balance:
        print("transaction successful")
        print("please collect your cash.")
        print("remaing balance:{account_balance-amount}")
    else:
        print("insufficent balance.")
else:
    print("invalide pin.enter corret pin.")        