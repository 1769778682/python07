# 需求：
# 1. 小明 体重 75.0 公斤
# 2. 小明每次 跑步 会减肥 0.5 公斤
# 3. 小明每次 吃东西 体重增加 1 公斤

# 类的设计
"""
类名：人类（Person）
属性：名字（name）/体重（weight）
方法：跑步（run）/吃东西（eat）
"""


class Person(object):
    """人类"""

    def __init__(self, name, weight):
        # 名字
        self.name = name
        # 体重
        self.weight = weight

    def __str__(self):
        """自定义打印对象输出的内容"""
        return f'我叫{self.name}，我的体重是{self.weight}'

    def run(self):
        """跑步方法"""
        print('跑步了')
        self.weight -= .5  # Python中，浮点数前面的0可以省略

    def eat(self):
        """吃定西方法"""
        print('吃东西了')
        self.weight += 1


# 调用
xm = Person('小明', 75)
xm.run()  # 跑步方法
print(xm)  # 我叫小明，我的体重是74.5
xm.eat()  # 吃东西方法
print(xm)  # 我叫小明，我的体重是75.5


xh = Person('小红', 45)
xh.run()
print(xh)
xh.eat()
print(xh)