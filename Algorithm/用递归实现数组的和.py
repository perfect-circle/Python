list= [1,2,3,4]

def sum(list):
    if list== []:
        return 0
    return list[0] + sum(list[1:])

print("列表元素之和：")
print(sum(list))

def coumt(list):
    if list == []:
        return 0
    return 1 + coumt(list[1:])

print("列表个数: ")
print(coumt(list))

def max_num(list):
    if list == []:
        return 0
    max_num = list[0]
    if list[0] < list[1]:
        max_num = list[1]
        return max_num(list[1:])

print('列表最大数：')
print(max_num(list))
