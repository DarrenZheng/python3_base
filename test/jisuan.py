
tianshu = int(input("请输入天数："))
huilv = float(input("请输入汇率:"))

if tianshu < 25:
    print("会得到人民币:", 35 * tianshu * huilv)
else:
    print("会得到人民币:", (35 * 25 + (tianshu - 25)* 45) * huilv )
