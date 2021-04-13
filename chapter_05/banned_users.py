banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

numbers = [1, 2, 3]
for number in numbers:
    if (1 in numbers) and number == 1:
        print("correct")
    elif 2 in numbers or number == 3:
        print("hello")
    else:
        print("wrong")


