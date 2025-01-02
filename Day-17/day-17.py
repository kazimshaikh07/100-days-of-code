class FullName:
    # pass
    # id = "001"
    # user_name = "Mohammmed Kazim Shaikh"
    # gender = "male","female"
    """creating constructor in our class using init function"""
    def __init__(self, user_id, user_name, user_gender):
        self.id = user_id
        self.name = user_name
        self.gender = user_gender
        self.followers = 0
        self.following = 0


    """Adding methonds in our class"""
    def follower_check(self):
        FullName.followers += 1
        self.following += 1

"""creating object from that class"""
n1 = FullName("001","Mohammed Kazim Shaikh", "Male")
n2 = FullName("002", "Simin Shaikh", "female")
n1.follower_check(n2)
print(n1.followers)
print(n1.following)
print
"""creating attribute for that class"""
# n1.age = 21



"""printing the object that we created from the class"""
# print(n1.age)