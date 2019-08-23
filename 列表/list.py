bicycles = ['trek','cannondale','redline','specialized'];
print(bicycles)  # ['trek','cannondale','redline','specialized']
print(bicycles[1]) #cannondale
print(bicycles[1].title()) #Cannondale
#访问列表最后一个用-1
print(bicycles[-1])
# 访问列表的长度
print(bicycles.__len__())

message = 'My first bicycle was a' + bicycles[0].title() + '.'
print(message)

# 修改列表的值

motorcycles = ['honda','yamaha','suzeki'];
print('motorcycles', motorcycles)

# motorcycles = 1  # 直接修改motorcycles本身

# print('motorcycles', motorcycles)
motorcycles[0] = ['monkey']
print('motorcycles', motorcycles)

# 给末尾添加值

motorcycles.append('bicycle')

print(motorcycles)
# 给列表插入值,可以在列表的任何位置插入值，及时插入的位置超出列表的边界，元素会插入到列表的最末端，
motorcycles.insert(8,'tools')
print(motorcycles)

# 从列表中删除元素,删除元素本身，就访问不到了,用del

del motorcycles[-1];
print(motorcycles)

# 删除列表末尾的值，并返回，可在pop方法内放置索引，指定哪一个值

popped =  motorcycles.pop();
print('popped', popped)
print(motorcycles)

# # 无需索引，删除元素,返回值为None,(????)只能指定第一次出现的值只能删一次
motorcycles.remove(['monkey'])
print("motorcycles", motorcycles)

#对列表进行排序
# sort改变原列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 字母顺序排序
cars.sort()
# 字母顺序相反排序
cars.sort(reverse=True)
print(cars)

# sorted: 临时排序
sorted_cars = sorted(cars)
print(sorted_cars)
print(cars)

# 翻转列表
# reverse 永久
cars.reverse();
print('cars', cars)
# 获取列表的长度
print(len(cars))

# 索引错误
print(cars[9])
