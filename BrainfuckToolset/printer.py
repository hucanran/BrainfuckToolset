# 用于特殊输出

def errorPrint(text):
    print('\033[31m', end = "")
    print(text, end = "")
    print('\033[0m')

def logPrint(text):
    print('\033[33m', end = "")
    print(text, end = "")
    print('\033[0m')
