# 1.定义一个电脑类, 电脑有品牌, 有价格, 能够播放音乐, 播放电影
# 2.分别创建 2 个对象"联想电脑"和"苹果电脑"
# 3.两台电脑分别调用放电影和播放音乐的方法, 联想电脑播放音乐"桥边姑娘", 苹果电脑播放电影"骇客帝国"


"""
类名：电脑类（Computer）
属性：品牌（brand）/价格（price）
方法：播放音乐（music）/ 播放电影（movie）
"""


class Computer(object):
    """电脑类"""

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def music(self):
        """播放音乐"""
        print(f'{self.brand}播放音乐“桥边姑娘”')

    def movie(self):
        """播放电影"""
        print(f'{self.brand}播放电影“骇客帝国”')


# 初始化对象
lx = Computer('联想电脑', 6888)
ap = Computer('苹果电脑', 8999)
# 调用函数
lx.music()
ap.movie()