<<<<<<< HEAD
#question:   Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
def life_in_weeks(age):
    last_age = 90
    current_age = 90 - age
    x = current_age*52
    if age == 90:
        print("you are dead")
    else:
        print(f"You have {x} weeks left.")
=======
#question:   Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
def life_in_weeks(age):
    last_age = 90
    current_age = 90 - age
    x = current_age*52
    if age == 90:
        print("you are dead")
    else:
        print(f"You have {x} weeks left.")
>>>>>>> 15025402e06e9348e7caaa5e700f76d9cb0f72e8
life_in_weeks(12)