score=int(input("请输入你的成绩:"))
grade=""
if score>80:
    grade="优秀"
elif score>60:
    grade="一般"
else:
    grade="及格"
print("分数{0},成绩{1}".format(score,grade))