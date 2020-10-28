# 需求：
# 1. 房子(House) 有 户型、总面积 和 家具名称列表 新房子没有任何的家具
# 2. 家具(HouseItem) 有 名字 和 占地面积，
# 其中 席梦思(bed) 占地 4 平米 衣柜(chest) 占地 2 平米 餐桌(table) 占地 1.5 平米
# 3. 将以上三件 家具 添加 到 房子 中
# 4. 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
"""
1,开发家具类
2,开发房子类
3，将家具添加到房子中
"""
"""
家具类名：HouseItem
属性：名字（name）/ 占地面积（area）
"""


class HouseItem(object):
    """家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        # return f'{self.name}的占地面积是{self.area}平米'
        return '{}的占地面积是{}平米'.format(self.name, self.area)

'''
房子类名:房子（House）
属性:户型（house_type)/总面积（area）
方法:添加家具（add_item)
'''


class House(object):
    """房子类"""

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f'户型：{self.house_type} 总面积：{self.area} 平米 ' \
               f'剩余面积：{self.free_area}平米 家具列表：{self.item_list}'

    def add_items(self, item):
        print(f'添加{item.name}到房子里, 占地面积:{item.area}平米')
        if self.free_area < item.area:
            print(f'{item.name}面积太大，房子放不下了')
            return
        self.free_area -= item.area
        self.item_list.append(item.name)


if __name__ == '__main__':
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)
    print(bed)
    print(chest)
    print(table)
    house = House('小三居', 100)
    print(house)
    house.add_items(bed)
    print(house)
    house.add_items(chest)
    print(house)
    house.add_items(table)
    print(house)
