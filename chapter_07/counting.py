current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 使用continue让程序忽略余下的代码
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# 只要cat在pets中就进入循环，可以把'cat' in pets 看作整体，返回结果true 或者 false
while 'cat' in pets:
    pets.remove('cat')

print(pets)