#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    my_tuple = tuple(map(float, input("Введите элементы списка: ").split()))

    if len(my_tuple) == 0:
        print("Список пуст", file=sys.stderr)
        sys.exit(1)

    a = float(input("Введите нижнюю границу диапазона: "))
    b = float(input("Введите верхнюю границу диапазона: "))
    s = sum(1 for x in my_tuple if a <= x <= b)
    print(f"В заданном диапазоне находится {s} элементов.")

    max_index = my_tuple.index(max(my_tuple))
    s_after_max = sum(my_tuple[max_index + 1:])
    print(f"Сумма элементов списка, расположенных после максимального: {s_after_max}")