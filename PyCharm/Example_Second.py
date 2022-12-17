#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # Все согласные
    a = set("bcdfghjlkmnpqrstvwxz")
    punc_marks = set(".?,!:;`'\" ")

    # Ввод строки
    s = set(input("Введите строку: ").lower())

    # Находим все гласные буквы в строке
    g = s.difference(a)
    g = g.difference(punc_marks)

    count = len(g)

    print(f"Все гласные буквы из введёной строки: {g}")
    print(f"Кол-во гласных букв: {count}")



