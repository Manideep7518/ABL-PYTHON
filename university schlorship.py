aggregate = float(input("Enter aggregate percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))
subject_marks = float(input("Enter minimum subject mark: "))

if aggregate >= 80 and attendance >= 75 and income <= 200000 and subject_marks >= 70:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")