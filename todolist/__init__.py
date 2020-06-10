import sqlite3


def status_num2string(num):
    if num == 1:
        s = '进行中'
    elif num == 2:
        s = '已完成'
    return s


class ToDoList():
    '''
    主类
    '''
    todo = dict()

    def __init__(self):
        '''
        类创建函数
        '''
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        # print("链接数据库成功")

    def list_task(self):
        cursor = self.c.execute("SELECT ID, title, status from task")
        for row in cursor:
            print('%d, %s, %s' % (row[0], row[1], status_num2string(row[2])))

    def done_task_by_id(self, id):
        self.c.execute("UPDATE task set status = 2 where ID = %d" % id)
        self.conn.commit()
