# coding: utf8


#冒泡排序
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n-i):
            if array[j-1] < array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

#选择排序:  与冒泡排序的区别，冒泡通过一次交换两个顺序不合法元素的位置，从而将当前最大元素放到合适的位置；
#           而选择排序每遍历一次，都记住当前最小（大）元素的位置，最后仅需要一次交换操作即可将其放到合适的位置
def select_sort(array):
    n = len(array)
    for i in range(0,n):
        min = i  # 最小元素下标
        for j in range(i+1, n):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]
    return array

# 插入排序：在已经排好的序列中，从后往前扫描、比较，找到相应的位置并插入
def insert_sort(array):
    n = len(array)
    for i in range(1,n):
        if array[i] > array[i-1]:
            temp = array[i]
            index = i   #带插入的下标
            for j in range(i-1, -1, -1): #从i-1 循环到0，包括0
                if array[j] < temp:
                    array[j+1] = array[j]
                    index = j  #记录待插下标
                else:
                    break
            array[index] = temp
    return array

#希尔排序：也称递增量排序，实质是分组插入排序（非稳定）；
#           基本思想：1)将一个列表分成 x 组，每组 Y 个元素，将每组的 x[i] 位置的元素进行排序，此时步长为Y，并按大小重新分组,然后合成列表
#                      2)重复步骤1）， 但步长要比 Y 小   步长的选择直接决定了希尔排序的复杂度。
def shell_sort(array):
    n = len(array)
    step = round(n/2)    #初始步长 , 用round四舍五入取整
    while step > 0:
        for i in range(step, n):
            j = i
            temp = array[i]
            # while (array[i-step] > array[i]):
            #     array[i-step], array[i] = array[i], array[i-step]
            while (j >= step and array[j-step]>temp):   #插入排序
                array[j] = array[j-step]
                j = j-step
                array[j] = temp
        step = round(step/2)
    return array

# 归并排序：归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
#           先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
#          然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
def merge_sort(array):
    n = len(array)
    if n <= 1: return array
    num = int(n/2)
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left, right)  #合并数组
def merge(left, right):
    # 合并操作，将两个有序数组left[]和right[]  合并成一个大的有序数组
    l, r = 0, 0    #left 和right 数组的下标指针
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result += left[l:]
    result += right[r:]
    return result

#快速排序：
'''
快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，
而且快排采用了分治法的思想，所以在很多笔试面试中能经常看到快排的影子。可见掌握快排的重要性。
步骤：
从数列中挑出一个元素作为基准数。
分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
再对左右区间递归执行第二步，直至各区间只有一个数。
'''
def quick_sort(array):
    n = len(array)
    return qsort(array, 0, len(array)-1)
def qsort(array, left, right):
# 快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right: return array
    key = array[left]  # 取最左边的为基准数
    lp = left
    rp = right    #右指针
    while lp < rp:
        while array[rp] >= key and lp<rp:
            rp -= 1
        while array[lp] <= key and lp<rp:
            lp += 1
        array[lp], array[rp] = array[rp], array[lp]
    array[left], array[lp] = array[lp], array[left]
    qsort(array, left, lp-1)
    qsort(array, rp+1, right)
    return array

# 堆排序
'''
堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。
二叉堆具有以下性质：
父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。
'''
def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary
#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

if __name__ == '__main__':
    array = [1, 5, 6, 4, 22, 88, 7, 98, 2, 45, 52, 36, 66, 1, 2]
    # ret = bubble_sort(array)
    # ret = select_sort(array)
    # ret = insert_sort(array)
    # ret = shell_sort(array)
    # ret = merge_sort(array)
    # ret = quick_sort(array)
    ret = heap_sort(array)
    print(ret)