import sys

# 常量----------------------------------
VERSION = "0.0.0"

# 全局变量------------------------------
code = ""  # 代码
RAM = [0, ]  # 内存
codePoint = 0  # 当前代码的地址
RAMPoint = 0  # 当前内存的地址


# 函数--------------------------------
def run():
    while codePoint <= len(code):
        c = code[codePoint]
        if c == "+":
            while len(RAM) >= RAMPoint:
                RAM.append(0)
            RAM[RAMPoint] += 1
            RAM[RAMPoint] %= 255
        if c == "-":
            while len(RAM) >= RAMPoint:
                RAM.append(0)
            RAM[RAMPoint] -= 1
            RAM[RAMPoint] %= 255
        if c == ".":
            print(chr(RAM[RAMPoint]))
        if c == ",":
            RAM[RAMPoint] = ord(input())
        if c == "<":
            if RAMPoint == 0:
                print("BF Error '{}' index:{} :illegal operation")
                return
        if c == ">":
            RAMPoint += 1
            if RAM < RAMPoint:RAM.append(0)


if __name__ == '__main__':
    total = len(sys.argv)
    if total == 1:
        print("BF log: {}".format(VERSION))
    if total == 2:
        ss = sys.argv[1]
        if ss[0] != "-" and ss[-3:-1] == ".bf":  # file
            try:
                file = open(ss, "r")
                code = file.read()
            except:
                print("BF Error: no file named {}".format(ss))
            else:
                run()
        if ss == "-v":
            print(VERSION)
