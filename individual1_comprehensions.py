#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = tuple(map(int, input().split()))

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        sys.exit(1)

    my_list = [x for x in A if 2 < x < 20 and x % 8 == 0]
    s = sum(my_list)
    l = len(my_list)

    print(f"Сумма: {s}, количество: {l}")
