# print(10%3)

# number = int(input("enter a number: "))
# if number%2 == 0:
#     print("even number")
# else:
#     print("odd number")



#Rollercoaster ticket checker plus photo asker
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n "))
age = int(input("What is your age?\n "))
bill = 0
if height >= 120:
    if age>18:
        bill = 80
        #print("Cost of ride =80rs\n")
    elif age==18:
        bill = 70
        #print("Cost of ride =70rs\n")
    elif 15<age<18:
        bill = 50
        #print("Cost of ride =50rs\n")
    elif age<12:
        bill = 40
        #print("Cost of ride =40rs\n")

    if age>=45 and age<=55:
        bill = 0

    photo = input("do you want to take photo or not(yes/no): ")
    if photo == "yes":
        bill += 15
        print(f"cost of rollercoaster and photo= {bill}")
    else:
        print(f"cost of rollercoaster and without_photo= {bill}")
    
else:
    print("cannot ride")


#python pizza delivery program
# print("Welcome to the pizza program!")
# size = input("what size customer wants(s/m/l): ")
# if size == "s" :
#     bill = 15
#     pepperoni =input("Add pepperoni for small pizza (Y or N): ")
#     if pepperoni == "y":
#         bill += 2
#     cheese =input("Add extra cheese for any size pizza (Y or N): ")
#     if cheese == "y":
#         bill += 1
#     print(f"Total cost of your pizza = {bill}$")
# if size == "m" :
#     bill = 20
#     pepperoni =input("Add pepperoni for medium or large pizza (Y or N): ")
#     if pepperoni == "y":
#         bill += 3
#     cheese =input("Add extra cheese for any size pizza (Y or N): ")
#     if cheese == "y":
#         bill += 1
#     print(f"Total cost of your pizza = {bill}$")
# if size == "l" :
#     bill = 25
#     pepperoni =input("Add pepperoni for medium or large pizza (Y or N): ")
#     if pepperoni == "y":
#         bill += 3
#     cheese =input("Add extra cheese for any size pizza (Y or N): ")
#     if cheese == "y":
#         bill += 1
#     print(f"Total cost of your pizza = {bill}$")

