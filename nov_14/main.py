from module import Student, Teacher

s1=Student("Laiba Kiyani", 23,1003)
t1=Teacher("Fawad", 25,"Advanced Python")
print(s1.name, s1.age)
print(s1.name, s1.age, s1.student_id)
print(t1.name, t1.age, t1.subject)

import myMath
result = myMath.add(5, 3)
print(result)
result1 = myMath.subtract(10, 4)
print(result1)
result2 = myMath.multiply(6, 7)
print(result2)
