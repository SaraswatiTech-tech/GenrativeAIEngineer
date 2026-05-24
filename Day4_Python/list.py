# welcome to list in python
from click import clear


My_Skill = ["Python", "java", "Javascript"]
print(My_Skill) 

# creating a list (we should create a list in square brackets)
Subjects= ["Maths", "physics", "chemistry"]
print(Subjects)

# accessing the elements of the list by using index number and always remember that the index number starts with 0

print(My_Skill[0])
print(My_Skill[1])
print(Subjects[-1])
# in list we have some common methods like append, insert, remove, pop, clear, sort, reverse etc

# if u want add a element in the list then we can use append() method
My_Skill.append("SQL")
print(My_Skill)

# if u want to add a elements in the list at a specific index then we can use insert() method

My_Skill.insert(2, "C++")
print(My_Skill)

# if u want remove a elements from the list then we can use remove() method
My_Skill.remove("C++")
print(My_Skill)

# if u want to remove a element from the list by using index number then we can use pop() method
My_Skill.pop(3)
print(My_Skill)

# if u want to write elements in the list in ascending order then we can use sort() method
Numbers = [5, 2, 6, 1, 4]
Numbers.sort()
print(Numbers)

# if u want to write elements in the list  in descending order then we can use sort() method with reverse parameter
Numbers.sort(reverse=True)
print(Numbers)
# looping through the list
for i in My_Skill:
    print(i)
     
    # if u want to check the length of the list then we can use len() method
    print(len(My_Skill))
   
   # if u want to clear the list then we can user clear() 
Age= [20, 30]
Age.clear()
print(Age)

#nested list means inside the list we have another list 
Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Matrix[1])
print(Matrix[1][2])
