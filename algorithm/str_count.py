# 统计字符串中出现次数最多的字符
def str_count(s):
    if s == "":
        return "传入的字符串不能为空"
    chars = {}
    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    print("打印字符串统计的次数：", chars)
    max_key = ""
    max_value = 0
    for key, value in chars.items():
        if value > max_value:
            max_key, max_value = key, value

    return (max_key, max_value)

print("打印返回结果：", str_count("ieriwhe"))


#某个字符在字符串中出现的次数
def count_char(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count
print(count_char("hello", "l"))
#用公共方法
print("hello".count("h"))

# 字符串中是否有某个字符串
print("=============字符串中是否有某个字符串")
print("hh" in "hhello")
# 在一个主字符串中查找一个子字符串的第一次出现位置
print("hhello".find("hh"))
print("hhello".index("hh"))

# 某个字符串在字符串中出现的次数
print("=============某个字符串在字符串中出现的次数")
print("hellheo".count("he"))

# 判断字符串里是否有重复字符
print("=============判断字符串里是否有重复字符")
print(len(set("hello")) != len("hello"))
