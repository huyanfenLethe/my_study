# 括号匹配
def is_balanced(s):
    sack = []
    rule = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in rule.keys():
            sack.append(char)
        if char in rule.values():
            #栈为空返回false
            if not sack:
                return False
            # 拿栈顶元素作为key查规则列表的值是否等于右括号，不等返回false，相等进行出栈
            if rule[sack[-1]] != char:
                return False
            else:
                # 栈顶元素出栈
                sack.pop()
    #栈为空返回true，否则返回false

# 测试用例
print(is_balanced("()"))  # True
print(is_balanced("()[]{}"))  # True
print(is_balanced("(]"))  # False
print(is_balanced("([)]"))  # False
print(is_balanced("{[]}"))  # True
