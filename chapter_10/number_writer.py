import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
# 以写入模式打开文件
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)


filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)
print(__name__)

