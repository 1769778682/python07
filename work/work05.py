# 定义一个水果类, 创建苹果对象, 橘子对象, 西瓜对象并分别添加属性: 颜色和价格


class Fruit(object):

    def __init__(self, color, price):
        self.color = color
        self.price = price

    def __str__(self):
        return f'颜色是{self.color}，价格是{self.price}'


apple = Fruit('红色', 7)
orange = Fruit('橙色', 5)
watermelon = Fruit('外绿内红', 4.5)
print(apple)
print(orange)
print(watermelon)
