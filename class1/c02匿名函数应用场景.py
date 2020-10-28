def calc(x, y, opt):
    """计算函数"""
    print(x)
    print(y)
    result = opt(x, y)
    print(result)


# 调用函数
calc(10, 20, lambda a, y: a + y)