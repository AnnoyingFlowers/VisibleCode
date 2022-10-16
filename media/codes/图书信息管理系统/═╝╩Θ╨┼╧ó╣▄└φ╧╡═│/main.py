from menu import Menu
from loader import read_instance


if __name__ == '__main__':#判断是否以主程序执行
    #调用loader中read_instance函数，提取图书清单和用户清单
    inst = read_instance('file/book.txt', 'file/user.txt')
    #调用menu中Menu，创建Menu类实例menu，将inst数据传入
    menu = Menu(inst)
    #调用初始界面方法，正式开始
    menu.register_manage()


