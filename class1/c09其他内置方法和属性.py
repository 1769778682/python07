class Cat(object):
    """猫类"""

    def __init__(self, name):
        self.name = name
        print('%s被创建' % self.name)

    # 在对象被内存销毁前自动调用
    def __del__(self):
        print('%s被销毁' % self.name)


# 调用
tom = Cat('汤姆')
print(tom.name)

# del tom
lz_c = Cat('懒猫')
print(lz_c.name)