# 需求：
# 1. 小明 体重 75.0 公斤
# 2. 小明每次 跑步 会减肥 0.5 公斤
# 3. 小明每次 吃东西 体重增加 1 公斤
# 类的设计
"""
类名：人类（Person）
属性：名字（name）/体重（weight）
方法：跑步（run）/eat（吃东西）
"""


class Person(object):
    """人类"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        """打印对象输出的内容"""
        return f'我的体重变成了{self.weight}'

    def run(self):
        """跑步"""
        print('我跑步了')
        self.weight -= .5

    def eat(self):
        """吃东西"""
        print('可是我又吃了东西')
        self.weight += 1


# 初始化对象
xm = Person('小明', 75)
# 调用函数
xm.run()
print(xm)
xm.eat()
print(xm)
