cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
# 临时排序
print(sorted(cars))

print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)
# 永久排序
cars.sort(reverse=True)
print(cars)

# 反转打印
cars.reverse()
print(cars)
# 列表长度
print(len(cars))
