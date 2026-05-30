def calculate_marks(mark_list):
    total= sum(mark_list)
    average = total / len(mark_list)
    return total, average

student_name = input("Enter student Name:")
num_subjects = int(input("Enter number of subjects:"))
marks = []
for i in range(1, num_subjects + 1):
    mark = int(input(f"Enter marks for subject {i}:"))
    marks.append(mark)

total, average = calculate_marks(marks)

if average >= 35:
    result = "pass"
else:
    result = "fail"

print("\n----- Student Report -----")
print("Student Name:", student_name)
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)