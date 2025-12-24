#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = tuple(map(int, input().split()))

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        sys.exit(1)

    s = 0
    count = 0
    for item in A:
        if 2 < item < 20 and item % 8 == 0:
            s += item
            count += 1

    print(f"Сумма: {s}, количество: {count}")
