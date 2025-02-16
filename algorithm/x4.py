# 最长回文子串

# 找到所有字串
def substrings(s):
    n = len(s)
    lists = []
    max_len = 0
    max_substring = ""
    # 外层循环控制子串的起始位置
    for i in range(n):
        # 内层循环控制子串的结束位置
        for j in range(i, n):
            # 获取从索引 i 到索引 j 的子串
            substring = s[i:j + 1]
            lists.append(substring)
            if substring == substring[::-1]:
                if len(substring) > max_len:
                    max_len = len(substring)
                    max_substring = substring
    print("字符串极其长度分别为", max_substring, max_len)
    return lists

# 测试示例
print(substrings("helloll"))