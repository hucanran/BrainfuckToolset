#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;

namespace PROGRAM_FILE_NAMESPACE
{
    string PROGARM_FILE_NAME;
    string str;
}

namespace PROGRAM
{
    std::vector<char> RAM(1024,0);
    size_t codePoint = 0;
    size_t RAM_point = 0;
}

void run(const string &code)
{
    PROGRAM::codePoint = 0;
    for (; PROGRAM::codePoint < code.size();
         PROGRAM::codePoint++)
    {
        char c = code[PROGRAM::codePoint];
        if ('>' == c)
        {
            if (PROGRAM::RAM.size() == PROGRAM::RAM_point)
            {
                PROGRAM::RAM_point++;
                PROGRAM::RAM.push_back(0);
            }
            else
            {
                PROGRAM::RAM_point++;
            }
        }
        if ('<'==c)
        {
            if (0 == PROGRAM::RAM_point)
            {
                cout << "第"
                     << PROGRAM::codePoint
                     << "号指令出错\n您无法访问负数地址"
                     << endl;
            }
            else
            {
                PROGRAM::RAM_point--;
            }
        }
        if ('+'==c)
        {
            PROGRAM::RAM[PROGRAM::RAM_point] = PROGRAM::RAM[PROGRAM::RAM_point] + 1;
        }
        if ('-'==c){
            PROGRAM::RAM[PROGRAM::RAM_point] = PROGRAM::RAM[PROGRAM::RAM_point] - 1;
        }
        if ('.'==c)
        {
            cout << (char)PROGRAM::RAM[PROGRAM::RAM_point];
        }
        if (','==c)
        {
            cin >> PROGRAM::RAM[PROGRAM::RAM_point];
        }
        if ('['==c)
        {
            if (0 == PROGRAM::RAM[PROGRAM::RAM_point])
            {
                int total = 1;
                while (0 != total)
                {
                    PROGRAM::codePoint++;
                    if ('[' == code[PROGRAM::codePoint])
                        total++;
                    if (']' == code[PROGRAM::codePoint])
                        total--;
                }
            }
        }
        if (']'==c)
        {
            if (0 != PROGRAM::RAM[PROGRAM::RAM_point])
            {
                int total = 1;
                while (0 != total)
                {
                    PROGRAM::codePoint--;
                    if (']' == code[PROGRAM::codePoint])
                        total++;
                    if ('[' == code[PROGRAM::codePoint])
                        total--;
                }
            }
        }
    }
}
int main(int argc, char *argv[])
{
    if (argc > 1)
    {
        PROGRAM_FILE_NAMESPACE::PROGARM_FILE_NAME = argv[1];
        std::ifstream PROGARM_FILE(PROGRAM_FILE_NAMESPACE::PROGARM_FILE_NAME);
        if (PROGARM_FILE.is_open() == false)
        {
            cout << "文件\""
                 << PROGRAM_FILE_NAMESPACE::PROGARM_FILE_NAME
                 << "\"不存在"
                 << endl;
            return 0;
        }
        std::ostringstream buf;
        buf << PROGARM_FILE.rdbuf();
        PROGARM_FILE.close();
        PROGRAM_FILE_NAMESPACE::str = string(buf.str());
        run(PROGRAM_FILE_NAMESPACE::str);
    }
    return 0;
}