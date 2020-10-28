# 需求：小猫爱吃鱼，小猫要喝水


class Cat(object):
    """猫类"""

    def eat(self):
        """吃鱼方法"""
        self.drink()
        print('小猫爱吃鱼', self.drink())

    def drink(self):
        """喝水方法"""
        print('小猫要喝水',)


# 创建猫对象
# 创建对象语法：类名()
Tom = Cat()
# 调用方法
Tom.eat()
Tom.drink()


# # 在创建一个猫对象
# lazy_cat = Cat()  # 对象2
# print(id(lazy_cat))
# lazy_cat.eat()
# lazy_cat.drink()
