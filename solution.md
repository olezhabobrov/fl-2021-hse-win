# 1

1. `a ((a | b)* b)*`

Самые короткие слова: `a`, `ab`, `aab` --- очевидно

`abbab` очевидно принадлежит данному регулярному выражению, сначала идет `a`, затем `bba` кодируется с помощью `(a | b)*`, а в конце просто `b`

`bababa` не принадлежит, так как начинается не с `a`

# 2

1. Надо построить автомат, принимающий все последовательности кроме тех, у которых в конце 00.

Полученный автомат:

