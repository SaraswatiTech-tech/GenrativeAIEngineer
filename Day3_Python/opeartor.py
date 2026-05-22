
kannada = int(input("Enter the marks obtained in kannada:"))
English = int(input("Enter the marks obtained in English:"))
Maths = int(input("Enter the marks obtained in Maths:"))
Science = int(input("Enter the marks obtained in Science:"))
Hindi = int(input("Enter the marks obtained in Hindi:"))
total_Marks = kannada + English + Maths + Science + Hindi

print("Total marks obtained:", total_Marks)

percentage = (total_Marks / 500) * 100
print("Percentage obtained:", percentage)

if percentage >=90:
    print("Grade: A")
elif percentage >=80:
    print("Grade: B")
elif percentage >=35:
    print("Grade: C")
else:
    print("Failed")
    
if percentage >=85 and Science >=90:
    print("You are eligible for B.E in computer science engineering")
else:
    print("you are not eligible for B.E in computer science engineering")


