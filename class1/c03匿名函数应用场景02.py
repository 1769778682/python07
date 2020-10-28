# 作为内置函数的参数
# 定义列表数据
user_info = [{'name': '刘备', 'age': 45},
             {'name': '关羽', 'age': 44},
             {'name': '张飞', 'age': 43}]
# 注意：key参数要求传入的值应该是能够返回
user_info.sort(key=lambda x: x['age'])
print(user_info)
# 说明：函数参数要求传入的值必须符合能够返回结果的情况下，也可以使用匿名函数