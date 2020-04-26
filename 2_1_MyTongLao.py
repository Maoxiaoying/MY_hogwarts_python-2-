"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
①see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
②fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""

class TongLao:   #定义天山童姥类
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power

    def see_people(self,name):  #定义see_people方法，传入名字
        if(name=="WYZ"):
            print("师弟！！！！")
        if(name=="李秋水"):
            print("呸，贱人")
        if(name=="丁春秋"):
            print("叛徒！我杀了你")

    def fight_zms(self,enemy_hp,enemy_power): #定义fight_zms方法，传入敌人的hp，power
        self.power=self.power*10       #自己的武力值提升10倍
        self.hp=self.hp/2         #血量缩减2倍
        self.hp=self.hp-enemy_power   #自己的血量
        enemy_hp=enemy_hp-self.power   #敌人的血量
        if(self.hp>0 and enemy_hp>0):  #一回合之后若双方都没有死，则进行狠话pk
            if(self.hp>enemy_hp):       #比较一回合之后双方血量
                print("童姥：你还差得远呢~")
                print("敌人：再来！")
            elif(self.hp<enemy_hp):
                print("敌人：天山折梅手不过如此")
                print("童姥：好戏才刚开始~")
            else:
                print("旁白：继续打，不死不休")
        while(self.hp>0 and enemy_hp>0):     #不死不休（只要有一个人死了就退出循环）
            self.power = self.power * 10    #每打一次都用折梅手，也就是武力值*10，血量/2
            self.hp = self.hp / 2  # 血量缩减2倍
            self.hp = self.hp - enemy_power  # 自己的血量
            enemy_hp = enemy_hp - self.power  # 敌人的血量
        #有一方血量清零了
        if(self.hp<=0):
            print("童姥：我不甘心！")
        if(enemy_hp<=0):
            print("敌人：折梅手果然，名。。不。。")


tl=TongLao(1000,20)            #实例化童姥
tl.see_people("丁春秋")        #调用see_people函数
tl.fight_zms(500,20)          #调用fight_zms函数