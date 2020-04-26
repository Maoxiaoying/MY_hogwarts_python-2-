"""
作业1：定义5个类
my:
类5：特种兵（刺激战场）
属性：枪，子弹，倍镜
方法：打人
在自身能力的基础上，如果没枪或者没有子弹，则打人成功概率为自身能力
在有枪且有子弹的情况下，若是散弹枪，则概率加5；若是步枪，则概率加10；若是狙击枪，则看有没有倍镜（无倍镜+5,2倍镜加10,4倍镜加15，八倍镜加20）
"""

class TeZhongBing:#定义一个特种兵类：具有属性：枪、子弹、倍镜  具有方法：打人
    def __init__(self,gun,bullet,magnification):
        self.gun=gun
        self.bullet=bullet
        self.magnification=magnification

    def fight(self,selfcapability):
        if(self.gun=="" or self.bullet==0):
            return selfcapability
        if(self.gun=="散弹枪"):
            return selfcapability+5
        if(self.gun=="步枪"):
            return selfcapability+10
        if(self.gun=="狙击枪"):
            if(self.magnification==0):
                return selfcapability+10
            if(self.magnification==2):
                return selfcapability+15
            if(self.magnification==4):
                return selfcapability+20
            if(self.magnification==8):
                return selfcapability+25
#枪的选择：步枪，散弹，狙击枪
#子弹的选择：1为有子弹，0为没有子弹
#倍镜的选择：0,2,4,8分别为无倍镜，2倍镜，4倍镜，8倍镜
tzb=TeZhongBing("狙击枪",1,2)    #实例化一位特种兵
print(f"该特种兵能打到人的概率为：{tzb.fight(50)}")  #打印该特种兵能打到人的概率