from collections import Counter


def unique_value_1(default_list):
    res = []
    for i in set(default_list):
        if default_list.count(i) == 1:
            res.append(i)
    return res


def unique_value_2(default_list):
    res = []
    value_dict = {i: default_list.count(i) for i in set(default_list)}
    for key, value in value_dict.items():
        if value == 1:
            res.append(key)
    return res


def unique_value_counter(default_list):
    res = []
    for key, value in Counter(default_list).items():
        if value == 1:
            res.append(key)
    return res


default_list = [22, 23, 42, 22, 23]

print(unique_value_1(default_list))
print(unique_value_2(default_list))
print(unique_value_counter(default_list))
