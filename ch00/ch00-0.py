# 注释以#开头

# 输出函数
print('我是输出')

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号
if True:
    print('正确')

# 变量定义
str = '我是一个变量'
print(str)

# for循环
languages = ["C", "C++", "Perl", "Python"]
for k in languages:
    print(k)

# for 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
# 从 0 到 10 步长为 3
for i in range(0, 10, 3) :
    print(i)

# if esle 的写法
if 10 > 11:
    print(1)
elif 10 > 22:
    print(2)
else:
    print(3)

# 特殊写法

# 1.for else 一般用于for循环最后时候需要输出什么或者做什么操作
for i in [1,2,3,4]:
	print(i)
else:
	print(i, '我是else')

# 2. Python 函数允许同时全部或部分使用固定参数、默认参数、单值（一颗星）可变参数、键值对（两颗星）可变参数，使用时必须按照前述顺序书写。

def do_something(name, age, gender='男', *args, **kwds):
	print('姓名：%s，年龄：%d，性别：%s'%(name, age, gender))
	print(args)
	print(kwds)

do_something('xinxigongcheng', 20, '男', 175, 75, math=99, english=90)

# 此外，一颗星和两颗星还可用于列表、元组、字典的解包，看起来更像C语言

# 3. 三元表达式
y = 5
if y < 0:
	print('y是一个负数')
else:
	print('y是一个非负数')

# 等价于

y = 5
print('y是一个负数' if y < 0 else 'y是一个非负数')

# python 的三元表达式也可以用来赋值：
y = 5
x = -1 if y < 0 else 1
print(x)

# 4. 列表推导式
# 一般写法
a = [1, 2, 3, 4, 5]
result = []
for i in a:
	result.append(i*i)
print(result)
# 优雅写法
a = [1, 2, 3, 4, 5]
result = [i*i for i in a]
print(result)

# 5. 匿名函数lambda
result = (lambda x,y: x+y)(3,4)
print(result)

