# import random
# print(random.randint(1,10))
# import Day_4_module
# print(Day_4_module.my_favorite_number)
# print(random.random()*10)
# print(random.uniform(1,5))


#question:Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.
# import random
# number = random.randint(0,1)
# if number==0:
#     print("heads")
# else:
#     print("tails")



# Figure out how to pick a random name from the list of friends.[friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]]
# type1
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))
# type2
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0,4)
print(friends[random_index])

