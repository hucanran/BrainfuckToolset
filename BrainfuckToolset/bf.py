import sys

# 常量----------------------------------
VERSION = "1.1,0"

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
            i = input()
            if len(i) > 1:
                print('\033[1;31m')
                print("BF Error :illegal input")
                print('\033[0m')
            else:
                memory[memoryPoint] = ord(i)
        if c == "<":
            if memoryPoint == 0:
                print('\033[0m')
                print("BF Error '{}' index:{} :illegal operation")
                print('\033[0m')
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
                            print('\033[0m')
                            print("BF Error: ']' index:{} :illegal operation".format(codePoint))
                            print('\033[0m')
                            return
                continue
        if c == "]":
            if len(stackOfBrackets) > 0:
                codePoint = stackOfBrackets.pop() - 1
            else:
                print('\033[0m')
                print("BF Error: ']' index:{} :illegal operation".format(codePoint))
                print('\033[0m')
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
                print('\033[0m')
                print("BF Error: no file named {}".format(ss))
                print('\033[0m')
            else:
                code = file.read()
                file.close()
                try:
                    run()
                except:
                    print('\033[0m')
                    print("BF Error: Error")
                    print('\033[0m')
        if ss == "-v":
            print(VERSION)
