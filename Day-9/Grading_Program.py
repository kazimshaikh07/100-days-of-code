print("welcome to grading program".upper())
"""student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
    #Get the value (student score) by using the key each time.
    score = student_scores[student]
 
    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'


print(f"{student_grades}\n")"""

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for value in student_scores:
    
    score = student_scores[value]
    
    if score >=91 and score <= 100:
        student_grades[value] = "outstanding"
    elif score >=81 and score <= 90:
        student_grades[value] = 'Exceeds Expectations'
    elif score >=71 and score <= 80:
        student_grades[value] = 'Acceptable'
    elif score <= 70:
        student_grades[value] = 'Fail'
    # else:
    #     print("invalid entry")
print(student_grades)








"""print("welcome to grading program".upper())
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for value in student_scores:
    if student_scores[value] >=91 and student_scores[value] <= 100:
        student_scores += value
        print("Outstanding")
    elif student_scores[value] >=81 and student_scores[value] <= 90:
        student_scores += value
        print("Exceeds Expectations")
    elif student_scores[value] >=71 and student_scores[value] <= 80:
        student_scores += value
        print("Acceptable")
    elif student_scores[value] <= 70:
        student_scores += value
        print("Fail")
    # else:
    #     print("invalid entry")
print(student_grades)"""