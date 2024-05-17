import timeit
import random

s = """

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

test_list = [random.randint(1, max_number) for _ in range(list_len)]
    
"""

max_number = 1000
list_len = 10000
test_list = [random.randint(1, max_number) for _ in range(list_len)]


func_tuple = ("merge_sort", "insertion_sort", "sorted")

for func in func_tuple:
    res = round(
        (timeit.timeit(func + "(test_list)", setup=s, number=1, globals=globals())), 5
    )
    print(
        f"Час сортування списку з {list_len} елементів від 1 до {max_number} по методу '{func:15s}' склав {res} секунд."
    )
