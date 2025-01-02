#for loop
#finding the maximum and minimum of the given list and also performing addition

#addition
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(sum(student_scores))
sum = 0
for score in student_scores:
    sum += score
print(sum)


#subtraction
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
sub = 0
for score in student_scores:
    sub -= score
print(sub)


#maximum
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_num = 0
for score in student_scores:
    if score > max_num:
        max_num = score
print(max_num)


#minimum
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
min_num = student_scores[0]
for score in student_scores:
    if min_num > score:
        min_num = score
print(min_num)


#multiplication
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
multi = 1
for score in student_scores:
    multi *= score
print(multi)


#division
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
div = 1
for score in student_sco-res:
    div /= score
print(div)







#add number from 1 to 100
sum_numb = 0
for number in range(1, 101):
    sum_numb += number
print(sum_numb)




