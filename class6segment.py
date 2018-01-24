#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from colorama import Fore, Back, Style, init

DELIMITER = ' '
sentense = u"..나는 오늘 3000원짜리 밥을 먹었어. 그리고, 오늘은 집에가서 20만원 정도 게임을 살 거야!!!! 내 전화번호는 010-5000-0200야. 전화해? 이거슨 클라스 추가하는 각인가요?? 응?"
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
    if chars[i] == '.' or chars[i] == ',' or chars[i] == '!' or chars[i] == '?':
        labels[i] = 'G'
        if labels[i-1] == 'M':
            labels[i-1] = 'E'
        elif labels[i-1] == 'G':
            None
        elif labels[i-1] == 'B':
            labels[i-1] = 'S'
        elif labels[i+1] == 'M':
            labels[i+1] = 'B'

# PARSER
print sentense

k = 0
i = 0
for label in labels :
    if label == 'N':
        sys.stdout.write(Fore.RED + chars[i] + Fore.RESET)
    elif label =='G':
        sys.stdout.write(Fore.BLUE + chars[i] + Fore.RESET)
    else:
        sys.stdout.write(chars[i])
    if label == 'E' or label == 'S' or label == 'G':
        if labels[k+1] == 'G' and label =='E':
            None
        elif labels[k+1] == 'S' and label == 'G':
            sys.stdout.write(' ')
        elif labels[k-1] == 'G' and label == 'G':
            None
        elif labels[k+1] == 'G' and label == 'G':
            None
        elif labels[k+1] == 'G' and label == 'S':
            None
        else:
            sys.stdout.write(' ')
    k += 1
    i += 1
    if k == len(labels)-1:
        k -= 1


print ''

k = 0
for label in labels:
    if label == 'N':
        sys.stdout.write(Fore.RED + label + Fore.RESET)
    elif label =='G':
        sys.stdout.write(Fore.BLUE + label + Fore.RESET)
    else:
        sys.stdout.write(label)
    if label == 'E' or label == 'S' or label == 'G':
        if labels[k+1] == 'G' and label =='E':
            None
        elif labels[k+1] == 'S' and label == 'G':
            sys.stdout.write(' ')
        elif labels[k-1] == 'G' and label == 'G':
            None
        elif labels[k+1] == 'G' and label == 'G':
            None
        elif labels[k+1] == 'G' and label == 'S':
            None
        else:
            sys.stdout.write(' ')
    k += 1
    if k == len(labels)-1:
        k -= 1
