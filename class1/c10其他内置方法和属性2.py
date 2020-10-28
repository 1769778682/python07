class Cat(object):
    """猫类"""

    def __init__(self, name):
        self.name = name
        print('%s被创建' % self.name)

    # # 在对象被内存销毁前自动调用
    # def __del__(self):
    #     print('%s被销毁' % self.name)
    def __str__(self):
        # 语法:return 要输出的内容.不包括print（）函数
        return '我是小猫: %s' % self.name


# 调用
tom = Cat('汤姆')
# 默认情况下，使用print（）函数输出对象
# 输出的内容如下：<__main__.Cat object at 0x00000204E6B48160>
print(tom)

# del tom
lz_c = Cat('懒猫')
print(lz_c)