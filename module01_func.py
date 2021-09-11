# ____________________sorted_____________________

def my_sort(my_list):
    my_list = list(map(int, my_list.split()))
    my_list = list(set(my_list))
    for lowest_value_idx in range(len(my_list)):
        for j in range(lowest_value_idx + 1, len(my_list)):
            if my_list[lowest_value_idx] > my_list[j]:
                my_list[lowest_value_idx], my_list[j] = my_list[j], my_list[lowest_value_idx]
    return my_list


# ____________________unique_character_____________________

def unique_characteristics(information: list, characteristics: list):
    """
    Функция возвращает отсортированые по уникальности словари.

    Информация состоит из списка словарей характеристик людей.
    Характеристика - это то, на что мы проверяем уникальность списка людей.
    Если наша характеристика для всех одинакова, функция возвращает соответствующую строку.
    """
    import itertools
    key_l, trash, final_result = [], [], []
    temp = 0
    while temp <= len(characteristics) - 1:
        for idx, infos in enumerate(information, 1):
            for key, value in infos.items():
                if key in characteristics[temp]:
                    if value in key_l:
                        trash.append(infos)
                    key_l.append(value)
            if idx == len(information):
                if len(trash) != len(information) - 1:
                    info_temp = [i for i in information if i not in trash]
                    final_result.append(info_temp)
                trash.clear()
                temp += 1
        flattened_final_result = list(itertools.chain.from_iterable(final_result))
        to_return = [flattened_final_result[i] for i in range(len(flattened_final_result)) if
                     i != flattened_final_result.index(flattened_final_result[i])]
    if not to_return:
        if not flattened_final_result:
            return 'Все значения характеристики совпадают!'
        return flattened_final_result
    else:
        return to_return


# ____________________wall_____________________

def wall(n, h):
    import random

    def match_indexs(a, x):
        out = []
        if x in a:
            out.append(a.index(x))
            for i in range(a.count(x) - 1):
                out.append(a.index(x, out[-1] + 1))
        return out

    if h >= n // 4:
        print('Балансирую введеные значения, чтобы стеночка имела форму прямоугольника...')
        n = n * 5
        if h != 1:
            h = n // 5

    _variable = n * '-'
    format_variable = f'+{_variable}+'

    random_brick = []
    [random_brick.extend('|' + ' ' * random.randrange(1, n // 2)) for _ in range(h) for _ in
     range(len(format_variable))]

    random_brick_ = ''.join(random_brick)

    _try1, _try2 = 0, n
    l = []

    for idx, i in enumerate(random_brick_):
        if idx == h:
            break
        if random_brick_[_try1:_try2] == '':
            break
        l.append(random_brick_[_try1:_try2])
        _try1, _try2 = _try1 + n, _try2 + n

    _list = [match_indexs(i[:n - 2], '|') for i in l]

    flattened = [x for row in _list for x in row]

    line_idx = max(zip((flattened.count(item) for item in set(flattened)), set(flattened)))

    frequency, elem = line_idx
    l_list = [list(i) for i in l]
    for i in l_list:
        if i[elem] == ' ':
            i[elem] = 'x'
    format_variable = list(format_variable)
    format_variable[elem + 2] = 'x'
    format_variable = ''.join(format_variable)
    print(format_variable)
    for i in l_list:
        print('|', end=' ')
        print(''.join(i)[:n - 2], end='')
        print(' |')
    print(format_variable)