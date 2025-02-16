#字符串字符去重复

s = "eurfgwhhh"
s2 = ""
for char in s:
    if char not in s2:
        s2 += char
print(s2)
