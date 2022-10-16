from information import Book
from information import User
import re#正则表达式

class Instance():
    def __init__(self, book_list: list, usr_list: list):
        self.book_list = book_list
        self.usr_list = usr_list
        self.log_usr = None
        

def read_instance(book_file_path, usr_file_path) :
    #读取书籍清单
    book_list = []
    with open(book_file_path, 'r',encoding='utf-8') as book_file:
        for line in book_file.readlines():
            line = line.strip('\n')#移除line头尾的换行符
            book_info=line.split('\t')
            book_list.append(Book(book_info[0], book_info[1], book_info[2], book_info[3],
                                    book_info[4], int(book_info[5]), int(book_info[6])))
    #读取用户清单
    user_list = []
    with open(usr_file_path, 'r',encoding='utf-8') as user_file:
        t = user_file.readlines()#读取文件中每行信息
        idx = 0
        while idx < len(t):
            line = t[idx]
            user_info=re.split('\s+', line)
            #在正则表达式中，\s可匹配空白字符
            #“+”重复修饰符，表示它前面与它紧邻的表达式格式相匹配的字符串至少出现一个
            usr = User(user_info[0], user_info[1], int(user_info[2]))#读取用户名，密码，是否为管理员

            idx += 1
            line = t[idx]
            split = re.split('\s+', line)
            for book in split:
                if len(book) > 0:
                    usr.books.append(book)#读取所借书籍索书号
                        
            idx += 1
            line = t[idx]
            split = re.split('\s+', line)
            for give_back in split:
                if len(give_back) > 0:
                    usr.give_back.append(give_back)#读取所借书籍是否归还信息
                        
            idx += 1
            line = t[idx]
            split = re.split('\s+', line)
            for give_back_date in split:
                if len(give_back_date) > 0:
                    usr.give_back_date.append(give_back_date)#读取所借书籍归还时间，未归还为“-1”

            user_list.append(usr)#将这一次循环中的usr记录到user_list中
            idx += 1

                
    inst = Instance(book_list, user_list)#调用Instance记录这两组列表数据
    return inst #返回Instance类下的信息
