#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = tuple(map(int, input().split()))

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        sys.exit(1)

    s = sum([x for x in A if 2 < x < 20 and x % 8 == 0])
    l = len([x for x in A if 2 < x < 20 and x % 8 == 0])

    print(f"Сумма: {s}, количество: {l}")
