#字符串反转
s = "helllo"
print("反转后的字符串", s[::-1])


#判断是否为回文字符串
s2 = "ee"
print(s2 == s2[::-1])


#字符串间隔3反转
s ="geydweifebf"
new_s = ""
for i in range(0, len(s), 3):
    #获取子串
    sub_str = s[i::i+3]
    #反转一下
    re_sub_str = sub_str[::-1]
    #拼接新串
    new_s += re_sub_str
print(new_s)