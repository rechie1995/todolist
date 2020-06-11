#!/usr/bin/python3
"""
ToDoList

这个项目的目的是制作一个简单的代办清单程序，可以管理我的日常事物。
"""
# import argparse
import sys
from todolist import ToDoList
import myargparse


def my_argparse():
    '''
    通过对argv列表的解析来进行命令行参数的解析
    '''
    if sys.argv[1] == 'list':
        ToDoList().show_task()
    else:
        print("arg 不存在")


def main():
    # prog = 'todo'
    # version = '0.0.1'
    # parser = argparse.ArgumentParser(
    #     prog=prog,
    #     usage='%(prog)s <command> [options]')
    # commands = parser.add_argument_group('commands')
    # commands.add_argument(
    #     '--list',
    #     help='list todo list',
    #     action=ToDoList().list_task()
    #     )
    # subparsers = parser.add_subparsers(help='sub-command help')
    # 添加子命令 list
    # parser_list = subparsers.add_parser('list', help='list help')
    # parser_list.set_defaults(func=ToDoList().list_task())
    # parser.add_argument(
    #     '-V', '--version',
    #     action='version',
    #     version='%(prog)s '+version,
    #     help='show version and exit')
    # parser.parse_args()
    # ToDoList().list_task()
    # print(args)
    parser = myargparse.Myargparser(usage='%(prog)s <command> [options]',
                                    description=__doc__)
    print(parser._get_args())
    parser.print_help()


if __name__ == "__main__":
    main()
