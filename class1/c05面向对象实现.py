# 面向对象实现


class Person(object):  # 定义类
    """人类"""

    def __init__(self, name):  # 添加属性
        self.name = name

    def eat(self):  # 定义方法
        print(f'{self.name}吃东西')

    def drink(self):  # 定义方法
        print(f'{self.name}喝饮料')


# 调用
xm = Person('小明')  # 初始化对象
xh = Person('小红')
xm.eat()  # 调用方法
xh.drink()

# 增加需求
# 1.换人：换成小李小王
xl = Person('小李')
xw = Person('小王')
xl.eat()
xw.drink()
# 2.互换方法
xm.drink()
xh.eat()
print(dir(xl))