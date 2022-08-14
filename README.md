# Brainfuck
一款Brainfuck的工具集(版本：v2.0)

## 快速入门

### 依赖

**ubtuntu**

```bash
$ sudo apt install git cmake g++
```

### 下载

```bash
$ git clone https://github.com/hucanran/BrainfuckToolset.git
$ cd BrainfuckToolset
```

### 使用下面任意一种方法编译

1、(推荐)

```bash
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
```

2、

```bash
$ cmake .
$ make
```

### 运行Hello world

```bash
$ ./bf ../example/HelloWorld.bf
```

## 什么是Brainfuck
> Brainfuck是一种极小化的计算机语言，它是由Urban Müller在1993年创建的。由于fuck在英语中是脏话，这种语言有时被称为brainf*ck或brainf**k，甚至被简称为BF。

——《百度百科》

## Brainfuck语法

| 字符 | 含义 |
| --- | --- |
| > | 指针加一 | 
| < | 指针减一 |
| + | 指针指向的字节加一 |
| - | 指针指向的字节减一 |
| . | 输出指针指向的字节的ASCII码 |
| , | 输入指针指向的字节的ASCII码 |
| [ | 循环开头 |
| ] | 循环结束 |


循环终止条件：

循环结尾时指针所在的字节为0则跳出循环

否则则跳转到循环头继续 
