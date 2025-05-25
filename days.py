day = int(input("Enter day number (1-7): "))

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= day <= 7:
    print(days_of_week[day - 1])
else:
    print("Invalid")
