# 简单字典定义，key-value值，通过key来访问值
alien_1 = {}  # 空字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 修改字典值
alien_0['x_position'] = 100
print(alien_0)
# 删除键值对
del alien_0['x_position']
print(alien_0)

# 字典的遍历，user_0.items()返回一个键—值对列表，然后分别将键，值赋给key，value变量，该变量可任意命名
user_0 = {
    'username': 'efermi', 'first': 'enrico', 'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 遍历字典的key
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name in favorite_languages.keys():
    print(name.title())
# 遍历所有值
for language in favorite_languages.values():
    print(language.title())
# 调用set方法去重
for language in set(favorite_languages.values()):
    print(language.title())

# 嵌套
# 列表中存储字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'], }
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# 字典中存储字典
users = {'aeinstein': {
    'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
    'mcurie': {
        'first': 'marie', 'last': 'curie', 'location': 'paris', },
}
# username对应key，user_info对应字典类型的value值
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
