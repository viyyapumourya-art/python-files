marks = int(input("enter your marks:"))
if marks <0 or marks > 100:
    print("invalid marks.enter correct mark.")
elif marks >=90:
    print("grade a")
elif marks >=80:
    print("grade b")
elif marks >=70:
    print("grade c")
elif marks >=60:
    print("grade d")
else:
    print("failed")                    