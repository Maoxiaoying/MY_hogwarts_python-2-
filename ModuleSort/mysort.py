#函数法进行冒泡排序
def bubble_sort(list1):  #定义冒泡排序函数(内部实现同上)
    for i in range(len(list1)):
        for j in range(len(list1) - i - 1):
            if (list1[j] > list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
