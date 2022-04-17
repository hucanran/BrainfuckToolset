import sys

# 常量----------------------------------
VERSION = "1.0.1"

# 全局变量------------------------------
code = ""  # 代码
memory = [0, ]  # 内存
codePoint = 0  # 当前代码的地址
memoryPoint = 0  # 当前内存的地址
stackOfBrackets = []
runFlag = 1


# 函数--------------------------------
def run():
    global code, memory, codePoint, memoryPoint, stackOfBrackets
    while codePoint < len(code):
        c = code[codePoint]
        if c == "+":
            while len(memory) < memoryPoint + 1:
                memory.append(0)
            memory[memoryPoint] += 1
            memory[memoryPoint] %= 255
        if c == "-":
            while len(memory) < memoryPoint + 1:
                memory.append(0)
            memory[memoryPoint] -= 1
            memory[memoryPoint] %= 255
        if c == ".":
            print(chr(memory[memoryPoint]), end="")
        if c == ",":
            memory[memoryPoint] = ord(input())
        if c == "<":
            if memoryPoint == 0:
                print("BF Error '{}' index:{} :illegal operation")
                return
            else:
                memoryPoint -= 1
        if c == ">":
            memoryPoint += 1
            if len(memory) < memoryPoint + 1:
                memory.append(0)
        if c == "[":
            stackOfBrackets.append(codePoint)
            if memory[memoryPoint] == 0:
                while len(stackOfBrackets) != 0:
                    codePoint += 1
                    if code[codePoint] == "[":
                        stackOfBrackets.append(codePoint)
                    if code[codePoint] == "]":
                        if len(stackOfBrackets) > 0:
                            stackOfBrackets.pop()
                            codePoint += 1
                            continue
                        else:
                            print("BF Error: ']' index:{} :illegal operation".format(codePoint))
                            return
                continue
        if c == "]":
            if len(stackOfBrackets) > 0:
                codePoint = stackOfBrackets.pop() - 1
            else:
                print("BF Error: ']' index:{} :illegal operation".format(codePoint))
        codePoint += 1


if __name__ == '__main__':
    total = len(sys.argv)
    if total == 1:
        print("BF log: {}".format(VERSION))
    if total == 2:
        ss = sys.argv[1]
        if ss[0] != "-" and ss[-3:] == ".bf":  # file
            try:
                file = open(ss, "r")
            except FileNotFoundError:
                print("BF Error: no file named {}".format(ss))
            else:
                code = file.read()
                file.close()
                try:
                    run()
                except:
                    print("BF Error: Error")
        if ss == "-v":
            print(VERSION)