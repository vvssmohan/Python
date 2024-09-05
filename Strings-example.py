# Vowel Counter
'''
s= input("Enter Name:")
s2=s.lower()
a=s2.count('a') 
e=s2.count('e') 
i=s2.count('i') 
o=s2.count('o') 
u=s2.count('u') 
print(f"Number of ovwels:{a+e+i+o+u}")

'''

#Grade Calculator

m=int(input("Marks in Maths: "))
s=int(input("Marks in Science: "))
e=int(input("Marks in English: "))

Total_marks =m+s+e
Average=Total_marks/3

percentage =(Total_marks/300)*100

if percentage > 90: 
    grade ="A"
elif percentage > 80 and percentage<=90:
    grade ="B"
elif percentage > 70 and percentage<=80:
    grade="c"
else:
    grade="P"
print(f"Total Mraks:{Total_marks} \nAverage Marks:{Average} \nGrade:{grade}")
