"""
作业3：
使用列表推导式写下面这个算法题
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
"""

#常规做法
#分析：平方后的数组呈先小后大趋势，定义一个i从头开始，一个j从尾开始，取较大值放进B中
from ModuleSort.mysort import bubble_sort    #导入sort模块
A=[-4,-1,0,3,10] #定义目标排序列表
B=[]             #定义暂存列表
i=0              #i从头开始
j=len(A)-1       #j从尾开始
while(i<=j):    #直到i,j交叉结束
    if(A[i]**2<A[j]**2): #谁大就把谁放进B，并且索引移动
        B.append(A[j]**2)
        j=j-1
    else:
        B.append(A[i]**2)
        i=i+1
B.reverse()
print(B)

#列表法
#先用for循环和append进行求解
# B=[]
# for x in A:
#     B.append(x**2)
# bubble_sort(B)
# print(B)

C=[x*x for x in A]    #将A中所有元素平方，得到一个平方列表
bubble_sort(C)      #对平方列表进行排序
print(C)   #打印排序后的平方列表




