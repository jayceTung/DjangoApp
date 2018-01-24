# -*- coding: utf-8 -*-

# @Author  : super
# @Time    : 2018/1/24
# @desc    :


if __name__ == '__main__':
    l = [i * 10 for i in range(10) if i - 1 > 1]
    r = [i - 1 for i in range(1, 11, -1) if i - 1 > 1]

    print(l)
    print(r)
