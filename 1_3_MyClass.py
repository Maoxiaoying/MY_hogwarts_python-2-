"""
作业1：定义5个类
my:
类3：陈情男孩
属性：名，字，门派，武器
方法：台词
"""

class ChenQingBoy:
    def __init__(self,name,zi,menpai,wuqi):
        self.name=name
        self.zi=zi
        self.menpai=menpai
        self.wuqi=wuqi

    def speak(self):
        if(self.name=="魏婴"):
            print("愿我魏无羡能够一生锄强扶弱，无愧于心")
        if(self.name=="蓝湛"):
            print("我想带一人回云深不知处，带回去，藏起来")
        if(self.name=="江厌离"):
            print("阿羡，你之前怎么跑的都那么快……我都没来得及看你一眼")
        if(self.name=="江澄"):
            print("你说过，将来我做家主，你做我的下属，一辈子扶持我，永远不会背叛云梦江氏……这是你自己说的")
xz=ChenQingBoy("魏婴","无羡","云梦","随便")
xz.speak()
wyb=ChenQingBoy("蓝湛","忘机","姑苏","避尘")