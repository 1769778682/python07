# 创建一个儿童类, 定义一个吃东西的方法, 喝饮料的方法, 运动的方法, 创建儿童对象并调用对象的方法


class Children(object):
    """儿童类"""

    # def __init__(self, name,):
    #     self.name = name

    def eat(self):
        print('吃蛋糕')

    def drink(self):
        print('总是喝可乐')

    def action(self):
        print('经常运动')


# 初始化对象
xh = Children()
xq = Children()
xg = Children()
# 调用函数
xh.eat()
xq.drink()
xg.action()