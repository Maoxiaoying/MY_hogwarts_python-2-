"""
作业1：定义5个类
my:
类4：学生
属性：姓名，学号，性别
方法：选课
"""
import random   #导入random库

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