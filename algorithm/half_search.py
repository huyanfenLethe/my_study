#二分查找
def half(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list1 = [2, 4, 7, 8]
print(half(list1, 4))
list2 = [2, 4, 7]
print(half(list2, 4))
list3 = []
print(half(list3, 4))
