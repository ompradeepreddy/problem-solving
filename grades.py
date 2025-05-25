t = int(input("Enter number of test cases: "))
for _ in range(t):
    marks = int(input("Enter marks: "))
    if marks >= 90:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    elif marks >= 35:
        print("Grade D")
    else:
        print("Fail")
