""""
作业0：冒泡排序每一行加注释说明
my:分别在主函数中，子函数中，类中进行冒泡排序
"""

#主函数中进行冒泡排序
list1=[1,3,2,7,-2,9,10]   #定义一个列表并赋值
print(f"原列表：{list1}") #打印原列表
for i in range(len(list1)):  #外循环：每一次外循环都可以把最大的(上一轮最大值不算)调整到最后一位
    for j in range(len(list1) - i - 1): #内循环：两两比较，每一次比较[总长度-i-1]次
        if (list1[j] > list1[j + 1]):  #如果前一位大于后一位，则交换位置
            list1[j], list1[j + 1] = list1[j + 1], list1[j]  #交换
print(f"主函数排序后列表：{list1}") # 打印排序后的列表

#函数法进行冒泡排序
def bubble_sort(list1):  #定义冒泡排序函数(内部实现同上)
    for i in range(len(list1)):
        for j in range(len(list1) - i - 1):
            if (list1[j] > list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

bubble_sort(list1)  #调用冒泡排序函数进行排序
print(f"函数法排序后列表：{list1}") # 打印排序后的列表

#类中进行冒泡排序
class BubbleSort:  #定义一个BubbleSort类
    def __init__(self,list1):   #初始化对象，在实例化对象时自动调用
        self.list1=list1        #给对象的属性进行赋值

    def list_sort(self):       #定义BubbleSort中的类方法：冒泡排序（具体排序算法同上）
        for i in range(len(self.list1)):
            for j in range(len(self.list1) - i - 1):
                if (self.list1[j] > self.list1[j + 1]):
                    self.list1[j], self.list1[j + 1] = self.list1[j + 1], self.list1[j]

l=BubbleSort(list1)     #实例化一个对象，并进行初始化为list1
l.list_sort()
print(f"在类中进行排序后的列表：{list1}") # 打印排序后的列表