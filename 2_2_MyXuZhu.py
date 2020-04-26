"""
定义一个XuZhu类，继承于童姥。
虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
from ModuleTongLao.MyTongLao import TongLao  #导入自定义模块MyTongLao(自定义模块需要放进package中，导入时会自动调用)

class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")

xuzhu=XuZhu(2000,100)
xuzhu.read()