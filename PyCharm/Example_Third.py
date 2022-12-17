#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    s_1 = set(input("Введите первую строку: "))
    s_2 = set(input("Введите вторую строку: "))

    punc_marks = set(".?,!:;`'\" ")

    o = s_1.intersection(s_2);
    o = o.difference(punc_marks)
    count = len(o)

    print(f"Общие символы: {o}")
    print(f"кол-во общих символов: {count}")