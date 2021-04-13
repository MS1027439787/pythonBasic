players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# 左闭右开
print(players[0:3])
# 不指定第一个索引，默认从第一个开始
print(players[:4])
# 到结尾元素
print(players[0:])
# -3代表距离末尾元素距离为3，左开右闭
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
