print("第一題：")
James = ["Lebron James", 23, 19, 22, 31, 18]
games = len(James)
max_score = max(James[1:])
i = James.index(max_score)
print(James[0],"在第%d場得最高分為%d" % (i, max_score))

print()
print("第二題：")
James =[["Lebron James", "SF(小前鋒)", "1984/12/30"], 23, 19, 22, 31, 18]
games = len(James)
max_score = max(James[1:])
i = James.index(max_score)
name, position, birthday = James[0][0], James[0][1], James[0][2]
connect = "-"
print("姓名-位置-生日：", connect.join(James[0]))
print("姓名：", name)
print("位置：", position)
print("生日：", birthday)
print("在第%d場得最高分為%d" % (i, max_score))
