# -*- coding: utf-8 -*-


from datetime import date

from cat import Cat

# jiji = Cat("ジジ", 13, "オス", "ニシンパイ", "黒", "白", "短毛種")
jiji = Cat("ジジ", date(2017, 5, 10), "オス", "", "ニシンパイ", "黒", "白", "短毛種")
print(jiji.name)
# print(jiji.sex)
print(jiji.birth_day)
print(jiji.age)
