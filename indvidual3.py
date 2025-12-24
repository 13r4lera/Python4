#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    my_tuple = tuple(map(float, input("Введите элементы: ").split()))

    if len(my_tuple) == 0:
        print("Пустой кортеж", file=sys.stderr)
        sys.exit(1)

    first = my_tuple[0]
    count = 0
    while count < len(my_tuple) and my_tuple[count] == first:
        count += 1

    print(f"В кортеже есть {count} одинаковых элементов в начале. Элементы после них: {my_tuple[count:]}")
