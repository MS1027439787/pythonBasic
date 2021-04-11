#由一系列按特定顺序排列的元素组成。
#用方括号（[] ）来表示列表，并用逗号来分隔其中的元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

too_expensive = 'ducati'
#删除列表元素
motorcycles.remove(too_expensive)
print(motorcycles)

#添加元素
motorcycles1 = []
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)
#插入新元素
motorcycles1.insert(0, "masai")
print(motorcycles1)
#删除元素
del motorcycles1[0]
print(motorcycles1)
#pop()方法删除末尾元素
#不指定位置，默认删除末尾元素
popped_motorcycle1 = motorcycles1.pop()
print(motorcycles1)
popped_motorcycle2 = motorcycles1.pop(0)

print(motorcycles1)

#根据值删除元素，方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
motorcycles1.remove('yamaha')
print(motorcycles1)
print("\nA " + too_expensive.title() + " is too expensive for me.")



