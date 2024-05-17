# додаткове завдання

def merge_k_lists(lists: list) -> list:

    if len(lists) == 0:
        return []
    elif len(lists) == 1:
        return lists[0]

    left_list = lists[0]

    for i in lists[1:]:
        res_list = []
        right_list = i

        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0] == right_list[0]:
                res_list.append(left_list.pop(0))
                res_list.append(right_list.pop(0))
            elif left_list[0] < right_list[0]:
                res_list.append(left_list.pop(0))
            else:
                res_list.append(right_list.pop(0))

        res_list.extend(left_list)
        res_list.extend(right_list)

        left_list = res_list

    return res_list


lists = [[1, 4, 5], [1, 3, 4], [2, 6], [1, 7, 9,]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
