class User :
    #initalizing attributes
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0 #initinal value it changes from object to object
        self.following = 0

    def follow(self,user):
        user.followers =+1
        user.following =+1


user_1 = User(10,"kazo")
print(user_1.id , user_1.username)
user_2 = User(11,"razo")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
        
