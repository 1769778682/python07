list1 = [1, 2, 3, 4]
print(dir(list1))
"""
['__add__', '__class__', '__contains__', '__delattr__', 
 '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__gt__', 
 '__hash__', '__iadd__', '__imul__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__reversed__', '__rmul__', '__setattr__', 
 '__setitem__', '__sizeof__', '__str__', '__subclasshook__']
"""

# 说明：凡是__方法名__形式的方法都属于Python提供的内置方法或属性
# 在学习Python过程中如果善用dir函数，就可以省去记忆大量方法的必要了