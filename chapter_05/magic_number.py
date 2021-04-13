answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
# 在if 语句中将列表名用在条件表达式中 时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False
numbers = []
if numbers:
    for number in numbers:
        print("not empty")
else:
    print("empty")
