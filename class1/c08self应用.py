# 需求：小猫爱吃鱼，小猫要喝水
# 在方法内部输出每个猫的名字


class Cat(object):
    """猫类"""

    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food
    def eat(self):
        """吃鱼方法"""
        print(f'{self.name}爱吃{self.food},今年{self.age}岁了')

    def drink(self):
        """喝水方法"""
        print(f'{self.name}爱喝{self.food},今年{self.age}岁了')


# 创建猫对象
# 创建对象语法：类名()
Tom = Cat('汤姆', 3, "小鱼干")
m = Cat('咪咪', 2, '火腿肠')
# 给猫增加一个名字属性并赋值，对象.属性名 = 属性值
# Python中不推荐在类定义外部给对象添加属性
# Tom.name = '汤姆'
# 调用方法
Tom.eat()
# Tom.drink()
m.eat()

# 在创建一个猫对象
lazy_cat = Cat('懒猫', 8, '牛奶')  # 对象2
# lazy_cat.name = '懒猫'
# lazy_cat.eat()
lazy_cat.drink()

# 注意：
# 1.再类外部，通过 对象.属性名 或对象.方法名，访问对象的属性和方法
# 2. 在类定义内部, 通过 self.属性名 或 self.方法名 访问对象的属性和方法