"""
作业1：定义5个类
my:
类2：葫芦兄弟
属性：排行，颜色
方法：超能力
"""

class GourdDoll:  #定义一个葫芦娃类：具有属性：排行，颜色；具有方法：超能力
    def __init__(self,index,color):   #属性初始化，在实例化对象时自动调用
        self.index=index          #给葫芦娃的排行赋值
        self.color=color[index]            #给葫芦娃的颜色赋值

    def super_power(self):               #葫芦娃的超能力
        powerset=["占个坑","力大无穷","眼观六路，耳听八方","刀枪不入","会喷火","会喷水","隐身术","..我有6个哥哥"]  #定义超能力集合                   #调用该方法时打印
        print(f"我是{self.color}娃，我{powerset[self.index]}")  #打印葫芦娃的超能力

colorset=["占个坑","红","橙","黄","绿","青","蓝","紫"]  #定义一个颜色集合，1~7个娃的颜色分别为红橙黄绿青蓝紫
dawa=GourdDoll(1,colorset)     #实例化大葫芦娃
dawa.super_power()              #大娃的超能力
qiwa=GourdDoll(7,colorset)     #实例化七娃
qiwa.super_power()              #七娃的超能力