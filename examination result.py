marks = [32, 38, 45, 50, 60]

for i in range(len(marks)):
    if marks[i] < 35 and 35 - marks[i] <= 5:
        marks[i] = 35

result = "PASS"

for mark in marks:
    if mark < 35:
        result = "FAIL"

print("Final Marks =", marks)
print("Result =", result)