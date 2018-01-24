#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from colorama import Fore, Back, Style, init

DELIMITER = ' '
sentense = u"..나는 오늘 3000원짜리 밥을 먹었어. 그리고, 오늘은 집에가서 20만원 정도 게임을 살 거야! 내 전화번호는 010-5000-2000야. 전화해?"
labels = []
chars = []
segments = sentense.split(DELIMITER)
for segment in segments:
    s_len = len(segment)
    if s_len == 0:
        continue
    elif s_len == 1:
        labels.append('S')
    else:
        labels.append('B')
        for j in range(s_len -2):
            labels.append('M')
        labels.append('E')
    for char in segment:
        chars.append(char)
assert len(chars) == len(labels)
for i in range(len(labels)):
    if chars[i].isdigit():
        labels[i] = 'N'


print sentense
for label in labels:
    if label == 'N':
        sys.stdout.write(Fore.RED + label + Fore.RESET)
    else:
        sys.stdout.write(label)
    if label == 'E' or label == 'S':
        sys.stdout.write(' ')

