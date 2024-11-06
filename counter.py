from collections import Counter

a = "hello"

print(Counter(a))



d = dict()

for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)