names = ['tom','jack'];
for item in names:
  print(item)
  print(item + ' is my good friend')

traffic = ['bicycle','underground','bus','car'];

for item in traffic:
  print('I would like take ' + item + ' to school')


customer = ['tom','sam','jack'];
customer[1] = 'jackson'
customer.append('lily')
customer.insert(1,'bob')
customer.insert(2,'wang')
customer.pop()
customer.pop()
customer.pop()
customer.pop()
for item in customer:
  print(item + ' will come to my home')

del customer[1]
del customer[0]


print('customer', customer)
print('customerNum', len(customer))
# # 为什么第二次循环都是打印列表的最后一个
# for changed in customer:
#   print(item + ' will come to my home')
