#!/usr/bin/python3
"""
ToDoList

这个项目的目的是制作一个简单的代办清单程序，可以管理我的日常事物。
"""
import argparse
import sys
from todolist import ToDoList


def my_argparse():
    '''
    通过对argv列表的解析来进行命令行参数的解析
    '''
    if sys.argv[1] == 'list':
        ToDoList().show_task()
    else:
        print("arg 不存在")


def main():
    prog = 'todo'
    version = '0.0.1'
    parser = argparse.ArgumentParser(
        prog=prog,
        usage='%(prog)s <command> [options]')
    parser.add_argument(
        '-V', '--version',
        action='version',
        version='%(prog)s '+version,
        help='show version and exit')
    ToDoList().list_task()


if __name__ == "__main__":
    # ToDoList().done_task_by_id(1)
    # ToDoList().list_task()
    # my_argparse()
    main()
