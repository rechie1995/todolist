import os as _os
import sys as _sys


__version__ = '0.0.1'
__all__ = [
    'Myargparser',
]


class Myargparser(object):

    def __init__(self,
                 prog=None,
                 usage=None,
                 description=None):

        # default setting for prog
        if prog is None:
            prog = _os.path.basename(_sys.argv[0])

        self.prog = prog
        self.usage = usage
        self.description = description
        self.args = self._get_args()
        self.options = []

        self._add_help()

    # 获取命令行输入
    def _get_args(self):
        return _sys.argv[1:]

    # 添加help
    def _add_help(self):
        func = self.print_help
        self.options.append(['-h', '--help', func])

    # 添加命令
    def add_command(self, *args, **kwargs):
        pass

    # 添加参数
    def add_option(self, *args, **kwargs):
        pass

    # 解析命令行输入
    def parse_args(self):
        for arg in self.args:
            for opt in self.options:
                if arg in opt:
                    # print(opt)
                    opt[2]()

    # #####
    # help 输出格式
    # #####
    def help_format(self):
        pass

    # #####
    # print相关函数
    # #####

    def _print_message(self, message):
        if message:
            _sys.stdout.write(message)

    def print_help(self):
        self._print_message(self.usage % {'prog': self.prog})
        self._print_message(self.description)
