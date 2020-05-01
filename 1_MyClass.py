import random   #导入random库
"""
作业1：定义5个类
"""
# 类1：猪
# 属性：猪鼻子，猪耳朵，猪嘴巴，体重，颜色
# 方法：吃，睡，能不能宰了（体重超过200公斤并且颜色不是粉色就能宰了，否则不宰）
print("============================= class1 猪类=====================================================")
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


# 类2：葫芦兄弟
# 属性：排行，颜色
# 方法：超能力
print("============================= class2 葫芦娃类=====================================================")
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

# 类3：陈情男孩
# # 属性：名，字，门派，武器
# # 方法：台词
print("============================= class3 陈情男孩类=====================================================")
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

# 类4：学生
# 属性：姓名，学号，性别
# 方法：选课
print("============================= class4 学生类=====================================================")
class Student:#定义一个学生类：具有属性：姓名、学号、性别  具有方法：选课
    def __init__(self,name,id,gender):
        self.name=name
        self.id=id
        self.gender=gender

    def courseSelection(self,list1):
        rand=random.randint(0,len(list1)-1)   #定义一个随机数
        return list1[rand]            #随机选课

list1=["计算机网络","python","机器学习","测试"]  #课程表
student1=Student("赵明明","10001","男")    #实例化一位学生
print(f"{student1.name}选了{student1.courseSelection(list1)}课")  #打印学生姓名和选课

# 类5：特种兵（刺激战场）
# 属性：枪，子弹，倍镜
# 方法：打人
# 在自身能力的基础上，如果没枪或者没有子弹，则打人成功概率为自身能力
# 在有枪且有子弹的情况下，若是散弹枪，则概率加5；若是步枪，则概率加10；若是狙击枪，则看有没有倍镜（无倍镜+5,2倍镜加10,4倍镜加15，八倍镜加20）
print("============================= class5 特种兵类=====================================================")
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