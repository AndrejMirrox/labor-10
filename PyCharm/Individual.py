#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "e", "g", "h", "k", "s"}
    b = {"c", "g", "p", "q"}
    c = {"f", "g", "s", "x", "y", "z"}
    d = {"a", "c", "d", "g", "u", "v", "z"}

    x = c.intersection(a.union(b))
    print(f"x = {x}")

    an = u.difference(a)
    print(f"notA = {an}")

    y = ((an.intersection(b)).union(c.difference(b)))
    print(f"y = {y}")
