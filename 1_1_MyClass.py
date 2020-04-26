"""
作业1：定义5个类
my:
类1：猪
属性：猪鼻子，猪耳朵，猪嘴巴，体重，颜色
方法：吃，睡，能不能宰了（体重超过200公斤并且颜色不是粉色就能宰了，否则不宰）
"""

class Pig:  #定义一个猪类：具有属性：猪鼻子，猪耳朵，猪嘴巴，体重，颜色；具有方法：吃，睡，能不能宰了
    nose=1   #一个猪鼻子
    ears=2   #一个猪耳朵
    mouth=1  #一个猪嘴巴
    def __init__(self,weight,color):   #属性初始化，在实例化对象时自动调用
        self.weight=weight          #给猪体重赋值
        self.color=color            #给猪的颜色赋值

    def eat(self):               #猪的方法：猪会吃
        print("吧唧~吧唧~")      #调用该方法时打印

    def sleep(self):     #猪的方法：猪会睡
        print("呼~呼~")  #调用该方法时打印

    def kill(self):   #猪的方法：能不能宰了
        if(self.weight>200 and self.color!="pink"):
            print("宰猪喽~")
        else:
            if(self.color=="pink"):
                print("人家那么可爱，你舍得吃我嘛~~")
            if(self.weight<=200):
                print("人家还是个孩纸呀~")


peiqi=Pig(100,"pink")     #实例化一只小猪(宠物猪佩奇)
peiqi.kill()              #判断吃不吃佩奇
bajie=Pig(300,"white")    #实例化一只小猪(猪八戒)
bajie.kill()              #判断吃不吃八戒
