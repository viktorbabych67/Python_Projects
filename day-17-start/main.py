class User1:
    pass


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user = User("123", "Viktor")
print(user.id)
user_2 = User("002", "Elon")

user.follow(user_2)

print(user.followers)
print(user.following)

print(user_2.followers)
print(user_2.following)


user_1 = User1()
user_1.id = "001"
user_1.username = "Viktor"


