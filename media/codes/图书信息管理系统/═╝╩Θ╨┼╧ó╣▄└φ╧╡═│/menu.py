from loader import Instance#引入Instance,传递数据
from information import Book#引入Book类
from information import User#引入User类
import tkinter as tk#GUI制作
import sys#运行环境模块，用于退出程序
import datetime#引入时间模块，用于记录还书时间


class Menu():
    
    def __init__(self, inst: Instance):#初始方法
        self.inst = inst#“inst”的属性
             
    def denglu(self):
        #登录界面及其相应功能
        denglujiemian=tk.Tk()
        denglujiemian.title('登录界面')
        denglujiemian.geometry("300x200")
        denglujiemian.config(bg='LightSkyBlue') 
        labyh=tk.Label(denglujiemian,text='请输入用户名')
        labyh.pack()
        labyh.config(bg='LightSkyBlue') 
        entryyh=tk.Entry(denglujiemian)
        entryyh.pack()
        entryyh.config(bg='SkyBlue')
        labmm=tk.Label(denglujiemian,text='请输入密码')
        labmm.pack()
        labmm.config(bg='LightSkyBlue')
        entrymm=tk.Entry(denglujiemian)
        entrymm.pack()
        entrymm.config(bg='SkyBlue')
        dltext=''#定义字符串变量，用于显示登录状态
        labdl=tk.Label(denglujiemian,text=dltext)
        labdl.pack()
        labdl.config(bg='LightSkyBlue')
        def dljianyan():
            usr_name=str(entryyh.get())
            pwd=str(entrymm.get())
            #登录检验
            success = False#两个用来判别的值
            is_exist = False
            for user in self.inst.usr_list:#循环遍历usr_list的用户信息
                if user.uid == usr_name:#找到有相应用户名的用户
                    is_exist = True#记录该用户存在
                    if user.pwd == pwd:#检验对应密码是否正确
                        labdl['text']='登录成功'
                        success = True#记录此次登录成功
                        self.inst.log_usr = user
                        #记录此次登录的用户
                        break
            if not is_exist:#输入用户不存在条件的情况
                labdl['text']='无此账号'
            else:
                if not success:
                    labdl['text']='登录失败'
            #身份判定
            if self.inst.log_usr is not None:#有用户成功登录的情况下
                if self.inst.log_usr.is_manager:
                #is_manager为布尔值（user.txt文件中显示为1或0）,该条即在True/1的情况下运行
                    self.edit_manage()#调用管理员界面的方法
                else:
                    self.usr_function()#同理
        #确认按钮，调用“登录检验的方法”
        btnqueren=tk.Button(denglujiemian,text='确认',command=dljianyan)
        btnqueren.pack()
        btnqueren.config(bg='SkyBlue')
        denglujiemian.mainloop()

    #管理员注册
    def glzhuce(self):
        glzhuce=tk.Tk()
        glzhuce.title('管理员注册')
        glzhuce.geometry("300x200")
        glzhuce.config(bg='LightSkyBlue')
        labyh=tk.Label(glzhuce,text='请输入注册管理员名称')
        labyh.pack()
        labyh.config(bg='LightSkyBlue')
        entryyh=tk.Entry(glzhuce)
        entryyh.pack()
        entryyh.config(bg='SkyBlue')
        labmm=tk.Label(glzhuce,text='请输入密码')
        labmm.pack()
        labmm.config(bg='LightSkyBlue')
        entrymm=tk.Entry(glzhuce)
        entrymm.pack()
        entrymm.config(bg='SkyBlue')
        dltext=''
        labdl=tk.Label(glzhuce,text=dltext)
        labdl.pack()
        labdl.config(bg='LightSkyBlue')
        #管理员注册检验
        def zhucejianyan():
            usr_name=str(entryyh.get())
            pwd=str(entrymm.get())
            is_exist = False
            #检查是否重名
            for user in self.inst.usr_list:
                if user.uid == usr_name:
                    is_exist = True
                    labdl['text']='请重新取名'
                    break
            if is_exist==False:
                #注册成功，管理员信息以User类追加在usr_list中
                self.inst.usr_list.append(User(usr_name, pwd, int(1)))
                #弹窗提示
                top1=tk.Tk()
                top1.title('管理员注册成功！')
                top1.config(bg='LightSkyBlue')
                lab1=tk.Label(top1,text='管理员注册成功！')
                lab1.pack()
                lab1.config(bg='LightSkyBlue')
                btn1=tk.Button(top1,text='确认',command=top1.destroy)
                btn1.pack()
                btn1.config(bg='SkyBlue')
                top1.mainloop()
        btnqueren=tk.Button(glzhuce,text='确认',command=zhucejianyan)
        btnqueren.pack()
        btnqueren.config(bg='SkyBlue')
        btnexit=tk.Button(glzhuce,text='退出',command=glzhuce.destroy)
        btnexit.pack()
        btnexit.config(bg='SkyBlue')
        glzhuce.mainloop()

    #普通用户注册，与上方“管理员注册”模块异曲同工
    def yhzhuce(self):
        yhzhuce=tk.Tk()
        yhzhuce.title('普通用户注册')
        yhzhuce.geometry("300x200")
        yhzhuce.config(bg='LightSkyBlue')
        labyh=tk.Label(yhzhuce,text='请输入注册普通用户名称')
        labyh.pack()
        labyh.config(bg='LightSkyBlue')
        entryyh=tk.Entry(yhzhuce)
        entryyh.pack()
        entryyh.config(bg='SkyBlue')
        labmm=tk.Label(yhzhuce,text='请输入密码')
        labmm.pack()
        labmm.config(bg='LightSkyBlue')
        entrymm=tk.Entry(yhzhuce)
        entrymm.pack()
        entrymm.config(bg='SkyBlue')
        dltext=''
        labdl=tk.Label(yhzhuce,text=dltext)
        labdl.pack()
        labdl.config(bg='LightSkyBlue')
        def zhucejianyan():
            usr_name=str(entryyh.get())
            pwd=str(entrymm.get())
            def chongfu():
                for user in self.inst.usr_list:
                    if user.uid == usr_name:
                        return True
                        break
            if chongfu():
                    labdl['text']='请重新取名'
            else:
                self.inst.usr_list.append(User(usr_name, pwd, int(0)))
                top1=tk.Tk()
                top1.title('普通用户注册成功！')
                top1.config(bg='LightSkyBlue')
                lab1=tk.Label(top1,text='普通用户注册成功！')
                lab1.pack()
                lab1.config(bg='LightSkyBlue')
                btn1=tk.Button(top1,text='确认',command=top1.destroy)
                btn1.pack()
                btn1.config(bg='SkyBlue')
                top1.mainloop()
        btnqueren=tk.Button(yhzhuce,text='确认',command=zhucejianyan)
        btnqueren.config(bg='SkyBlue')
        btnqueren.pack()
        btnexit=tk.Button(yhzhuce,text='退出',command=yhzhuce.destroy)
        btnexit.config(bg='SkyBlue')
        btnexit.pack()
        yhzhuce.mainloop()
            
    def register_manage(self):
        #登陆与注册界面
            top=tk.Tk()
            top.title('图书信息管理系统 by 李庭悠，刘翔，姚镔哲')
            top.geometry('300x200')
            top.config(bg='LightSkyBlue') 
            labO=tk.Label(top,text='欢迎来到图书管理系统\nby 李庭悠，刘翔，姚镔哲')
            labO.grid(row=0,column=4)
            labO.config(bg='LightSkyBlue')
            btn1=tk.Button(top,text='用户登录',command=self.denglu)
            btn1.grid(row=0,column=0,rowspan=1,columnspan=2)
            btn1.config(bg='SkyBlue')
            btn2=tk.Button(top,text='管理员注册',command=self.glzhuce)
            btn2.grid(row=1,column=0,rowspan=1,columnspan=2)
            btn2.config(bg='SkyBlue')
            btn3=tk.Button(top,text='普通用户注册',command=self.yhzhuce)
            btn3.grid(row=2,column=0,rowspan=1,columnspan=2)
            btn3.config(bg='SkyBlue')
            def comexit():
                #记录此轮信息并退出
                with open('file/book.txt', 'w',encoding='utf-8') as book_file:
                    #实质是将本轮运行结束时记录在inst.book_list的内容记录在book.txt中
                    for idx in range(len(self.inst.book_list)):#用idx定位book_list中的元素（在此是书籍信息）
                        book = self.inst.book_list[idx]#取book_list中对应下标的元素（书籍信息）
                        book_file.write(str(book))#将上一行取得的书籍信息写入book.txt中，实现记录
                        if idx != len(self.inst.book_list) - 1:#换行以便记录下一次循环中的信息（如有的话）
                            book_file.write('\n')
                with open('file/user.txt', 'w',encoding='utf-8') as user_file:
                    #实质是将本轮运行结束时记录在inst.user_list的内容记录在user.txt中
                    for idx in range(len(self.inst.usr_list)):#用idx定位usr_list中的元素（在此是用户信息）
                        user = self.inst.usr_list[idx]#取usr_list中对应下标的元素（用户信息）
                        user_file.write(str(user))#将上一行取得的用户信息以字符串形式写入user.txt中（事实上调用了__str__方法），实现记录
                        user_file.write('\n')#换行，进行同一用户下一块信息的记录
                        for books in user.books:
                            user_file.write(books)#记录改用户所借书目的索引号
                            user_file.write('\t')#“\t”为制表符，可将对其上下数据的各列
                        user_file.write('\n')
                        for give_back in user.give_back:
                            user_file.write(give_back)#写入对应用户的对应书籍的是否归还情况，usr.txt中以True或False表示
                            user_file.write('\t')
                        user_file.write('\n')
                        for give_back_date in user.give_back_date:
                            user_file.write(give_back_date)#写入对应用户的归还时间，如无归还则为“-1”
                            user_file.write('\t')
                        if idx != len(self.inst.usr_list) - 1:#判断是否为最后一组用户数据，如不是则换行以记录下一组
                            user_file.write('\n')
                    top.destroy()#退出窗口
                    sys.exit(0)#处理环境运行模块中的退出，结束程序运行
            btn4=tk.Button(top,text='退出系统',command=comexit)
            btn4.grid(row=3,column=0)
            btn4.config(bg='SkyBlue')
            top.mainloop()

    def input_book(self):
        #录入新书
            inputm=tk.Tk()
            inputm.title('添加图书信息')
            inputm.geometry('500x500')
            inputm.config(bg='LightSkyBlue')
            lab0=tk.Label(inputm,text='请输入书籍详细信息')
            lab0.pack()
            lab0.config(bg='LightSkyBlue')
            lab1=tk.Label(inputm,text='请输入索书号')
            lab1.pack()
            lab1.config(bg='LightSkyBlue')
            entry1=tk.Entry(inputm)
            entry1.pack()
            entry1.config(bg='SkyBlue')
            lab2=tk.Label(inputm,text='请输入书名')
            lab2.pack()
            lab2.config(bg='LightSkyBlue')
            entry2=tk.Entry(inputm)
            entry2.pack()
            entry2.config(bg='SkyBlue')
            lab3=tk.Label(inputm,text='请输入作者')
            lab3.pack()
            lab3.config(bg='LightSkyBlue')
            entry3=tk.Entry(inputm)
            entry3.pack()
            entry3.config(bg='SkyBlue')
            lab4=tk.Label(inputm,text='请输入出版社')
            lab4.pack()
            lab4.config(bg='LightSkyBlue')
            entry4=tk.Entry(inputm)
            entry4.pack()
            entry4.config(bg='SkyBlue')
            lab5=tk.Label(inputm,text='请输入图书类别')
            lab5.pack()
            lab5.config(bg='LightSkyBlue')
            entry5=tk.Entry(inputm)
            entry5.pack()
            entry5.config(bg='SkyBlue')
            lab6=tk.Label(inputm,text='请输入收藏总量')
            lab6.pack()
            lab6.config(bg='LightSkyBlue')
            entry6=tk.Entry(inputm)
            entry6.pack()
            entry6.config(bg='SkyBlue')
            lab7=tk.Label(inputm,text='请输入可借本数')
            lab7.pack()
            lab7.config(bg='LightSkyBlue')
            entry7=tk.Entry(inputm)
            entry7.pack()
            entry7.config(bg='SkyBlue')
            lrtext=''
            lab8=tk.Label(inputm,text=lrtext)
            lab8.pack()
            lab8.config(bg='LightSkyBlue')
            def luru():
                #据对应的输入框内容记录书籍信息
                bid=entry1.get()
                name=entry2.get()
                author=entry3.get()
                press=entry4.get()
                btype=entry5.get()
                amount=entry6.get()
                available=entry7.get()
                #将信息以Book类的形式追加到book_list中
                self.inst.book_list.append(Book(bid, name, author, press, btype, amount, available))
                lab8['text']='录入成功！'
            btn0=tk.Button(inputm,text='确认',command=luru)
            btn0.pack()
            btn0.config(bg='SkyBlue')
            btn1=tk.Button(inputm,text='退出',command=inputm.destroy)
            btn1.pack()
            btn1.config(bg='SkyBlue')
            inputm.mainloop()
            
    def modify_book(self):
        #修改书籍信息
            topmd=tk.Tk()
            topmd.title('修改图书信息')
            topmd.geometry('500x500')
            topmd.config(bg='LightSkyBlue')
            lab0=tk.Label(topmd,text='请输入要修改的书籍的索书号')
            lab0.pack()
            lab0.config(bg='LightSkyBlue')
            entry0=tk.Entry(topmd)
            entry0.pack()
            entry0.config(bg='SkyBlue')
            lab1=tk.Label(topmd,text='请输入修改后的索书号')
            lab1.pack()
            lab1.config(bg='LightSkyBlue')
            entry1=tk.Entry(topmd)
            entry1.pack()
            entry1.config(bg='SkyBlue')
            lab2=tk.Label(topmd,text='请输入要修改后的书名')
            lab2.pack()
            lab2.config(bg='LightSkyBlue')
            entry2=tk.Entry(topmd)
            entry2.pack()
            entry2.config(bg='SkyBlue')
            lab3=tk.Label(topmd,text='请输入要修改后的作者')
            lab3.pack()
            lab3.config(bg='LightSkyBlue')
            entry3=tk.Entry(topmd)
            entry3.pack()
            entry3.config(bg='SkyBlue')
            lab4=tk.Label(topmd,text='请输入要修改后的出版社')
            lab4.pack()
            lab4.config(bg='LightSkyBlue')
            entry4=tk.Entry(topmd)
            entry4.pack()
            entry4.config(bg='SkyBlue')
            lab5=tk.Label(topmd,text='请输入要修改后的图书类别')
            lab5.pack()
            lab5.config(bg='LightSkyBlue')
            entry5=tk.Entry(topmd)
            entry5.pack()
            entry5.config(bg='SkyBlue')
            lab6=tk.Label(topmd,text='请输入要修改后的收藏总量')
            lab6.pack()
            lab6.config(bg='LightSkyBlue')
            entry6=tk.Entry(topmd)
            entry6.pack()
            entry6.config(bg='SkyBlue')
            lab7=tk.Label(topmd,text='请输入要修改后的可借本书')
            lab7.pack()
            lab7.config(bg='LightSkyBlue')
            entry7=tk.Entry(topmd)
            entry7.pack()
            entry7.config(bg='SkyBlue')
            #与录入书籍方法中内容类似
            def queren():
                bid = entry0.get()
                is_exist = False#判定要修改的书是否存在
                for book in self.inst.book_list:
                    if book.bid == bid:
                        is_exist = True
                        book.bid = entry1.get()
                        book.name = entry2.get()
                        book.author = entry3.get()
                        book.press = entry4.get()
                        book.btype = entry5.get()
                        book.amount = entry6.get()
                        book.available = entry7.get()
                        top0=tk.Tk()
                        top0.config(bg='LightSkyBlue')
                        lab=tk.Label(top0,text='修改成功')
                        lab.pack()
                        lab.config(bg='LightSkyBlue')
                        btn=tk.Button(top0,text='好的',command=top0.destroy)
                        btn.pack()
                        btn.config(bg='SkyBlue')
                        top0.mainloop()
                if not is_exist:
                    top0=tk.Tk()
                    top0.config(bg='LightSkyBlue')
                    lab=tk.Label(top0,text='未找到相关书籍，请检查索书号')
                    lab.pack()
                    lab.config(bg='LightSkyBlue')
                    btn=tk.Button(top0,text='好的',command=top0.destroy)
                    btn.pack()
                    btn.config(bg='SkyBlue')
                    top0.mainloop()
            btn=tk.Button(topmd,text='确认修改',command=queren)
            btn.pack()
            btn.config(bg='SkyBlue')
            topmd.mainloop()
        
    def delete_book(self):
        #删除书
            topde=tk.Tk()
            topde.title('删除书籍信息')
            topde.geometry('500x500')
            topde.config(bg='LightSkyBlue')
            lab1=tk.Label(topde,text='请输入要删除的书籍的索书号')
            lab1.pack()
            lab1.config(bg='LightSkyBlue')
            entry1=tk.Entry(topde)
            entry1.pack()
            entry1.config(bg='SkyBlue')
            def queren():
                bid = entry1.get()
                is_exist = False#判断要删除的书是否存在
                for book in self.inst.book_list:#遍历book_list
                    if bid == book.bid:#找到对应的书籍
                        is_exist = True
                        self.inst.book_list.remove(book)
                        top0=tk.Tk()
                        top0.config(bg='LightSkyBlue')
                        lab=tk.Label(top0,text='索书号 ' + bid + ' 的书籍已删除')
                        lab.pack()
                        lab.config(bg='LightSkyBlue')
                        btn=tk.Button(top0,text='好的',command=top0.destroy)
                        btn.pack()
                        btn.config(bg='SkyBlue')
                        top0.mainloop()
                if not is_exist:
                    top0=tk.Tk()
                    top0.config(bg='LightSkyBlue')
                    lab=tk.Label(top0,text='未找到相关书籍，请检查索书号')
                    lab.pack()
                    lab.config(bg='LightSkyBlue')
                    btn=tk.Button(top0,text='好的',command=top0.destroy)
                    btn.pack()
                    btn.config(bg='SkyBlue')
                    top0.mainloop()
            btn1=tk.Button(topde,text='确认修改',command=queren)
            btn1.pack()
            btn1.config(bg='SkyBlue')
            topde.mainloop()
            
    #显示清单内所有书
    def show_book(self):
        show=tk.Tk()
        show.title('藏书一览')
        show.geometry('600x600')
        show.config(bg='LightSkyBlue')
        book_file=open('file/book.txt', 'r',encoding='utf-8')
        showtext=book_file.read()#read方法读取文件内容
        labshow=tk.Label(show,text=showtext)#book.txt中内容显示在对应Label上
        labshow.pack()
        labshow.config(bg='LightSkyBlue')
        book_file.close()
        show.mainloop()
        
    def edit_manage(self):
        #管理员模块
            topm=tk.Tk()
            topm.title('管理员界面')
            topm.geometry('300x200')
            topm.config(bg='LightSkyBlue')
            labm=tk.Label(topm,text='尊敬的管理员，请选择您所需的功能')
            labm.grid(row=0,column=2,rowspan=1,columnspan=2)
            labm.config(bg='LightSkyBlue')
            tj=tk.Button(topm,text='添加图书信息',command=self.input_book)
            tj.grid(row=1,column=0)
            tj.config(bg='SkyBlue')
            xg=tk.Button(topm,text='修改图书信息',command=self.modify_book)
            xg.grid(row=2,column=0)
            xg.config(bg='SkyBlue')
            sc=tk.Button(topm,text='删除图书信息',command=self.delete_book)
            sc.grid(row=3,column=0)
            sc.config(bg='SkyBlue')
            yilan=tk.Button(topm,text='藏书信息一览',command=self.show_book)
            yilan.grid(row=4,column=0)
            yilan.config(bg='SkyBlue')
            tc=tk.Button(topm,text='退出管理者界面',command=topm.destroy)
            tc.grid(row=5,column=0)
            tc.config(bg='SkyBlue')
            topm.mainloop()
            
#以下是普通用户功能
            
    def check_usr(self):
        #查询用户信息
        topck=tk.Tk()
        topck.title('查询用户信息')
        topck.config(bg='LightSkyBlue')
        topck.geometry('500x500')
        btn0=tk.Button(topck,text='退出',command=topck.destroy)
        btn0.pack()
        btn0.config(bg='SkyBlue')
        lab0=tk.Label(topck,text='借阅信息：')
        lab0.pack()
        lab0.config(bg='LightSkyBlue')
        cxtext="索书号" + "\t" + "是否归还" + "\t" + "归还日期"+'\n'
        lab1=tk.Label(topck,text=cxtext)
        lab1.pack()
        lab1.config(bg='LightSkyBlue')
        for idx in range(len(self.inst.log_usr.books)):
            lab1['text']=lab1['text']+(self.inst.log_usr.books[idx] + '\t' + self.inst.log_usr.give_back[idx] + '\t'+self.inst.log_usr.give_back_date[idx]+'\n')
        topck.mainloop()

    def search_book(self):
        #查找图书信息
        topcz=tk.Tk()
        topcz.title('查找图书信息')
        topcz.geometry('700x400')
        topcz.config(bg='LightSkyBlue')
        lab0=tk.Label(topcz,text='按条件查找')
        lab0.grid(row=0,column=0)
        lab0.config(bg='LightSkyBlue')
        labc=tk.Label(topcz,text='请输入查找信息')
        labc.grid(row=1,column=1)
        labc.config(bg='LightSkyBlue')
        entryc=tk.Entry(topcz)
        entryc.grid(row=2,column=1)
        entryc.config(bg='SkyBlue')
        labs=tk.Label(topcz,text='')
        labs.grid(row=3,column=1)
        labs.config(bg='LightSkyBlue')
        #通过索书号查询
        def bidsc():
            var=entryc.get()#读取输入框信息
            labs['text']=''#清空上一次的显示
            d=False
            for book in self.inst.book_list:#遍历book_list
                if book.bid == var:#找到对应的书籍
                    labs['text']=labs['text']+'\n'+str(book)
                    #在Label上显示所有满足条件的书籍的信息
                    d=True
            if not d:
                labs['text']='无符合条件的书籍'
        btn1=tk.Button(topcz,text='按索书号查询',command=bidsc)
        btn1.grid(row=1,column=0)
        btn1.config(bg='SkyBlue')
        #通过书名查询
        def nasc():
            var=entryc.get()
            var=str(var)
            labs['text']=''
            d=False
            for book in self.inst.book_list:
                if book.name == var:
                    labs['text']=labs['text']+'\n'+str(book)
                    d=True
            if not d:
                labs['text']='无符合条件的书籍'
        btn2=tk.Button(topcz,text='按书名查询',command=nasc)
        btn2.grid(row=2,column=0)
        btn2.config(bg='SkyBlue')
        #通过作者名查询
        def ausc():
            var=entryc.get()
            var=str(var)
            labs['text']=''
            d=False
            for book in self.inst.book_list:
                if book.author == var:
                    labs['text']=labs['text']+'\n'+str(book)
                    d=True
            if not d:
                labs['text']='无符合条件的书籍'
        btn3=tk.Button(topcz,text='按索作者查询',command=ausc)
        btn3.grid(row=3,column=0)
        btn3.config(bg='SkyBlue')
        #通过出版社查询
        def prsc():
            var=entryc.get()
            var=str(var)
            labs['text']=''
            d=False
            for book in self.inst.book_list:
                if book.press == var:
                    labs['text']=labs['text']+'\n'+str(book)
                    d=True
            if not d:
                labs['text']='无符合条件的书籍'
        btn4=tk.Button(topcz,text='按出版社查询',command=prsc)
        btn4.grid(row=4,column=0)
        btn4.config(bg='SkyBlue')
        def typesc():
            var=entryc.get()
            labs['text']=''
            d=False
            for book in self.inst.book_list:
                if book.btype == var:
                    labs['text']=labs['text']+'\n'+str(book)
                    d=True
            if not d:
                labs['text']='无符合条件的书籍'
        btn5=tk.Button(topcz,text='按书籍类型查询',command=typesc)
        btn5.grid(row=5,column=0)
        btn5.config(bg='SkyBlue')
        btn6=tk.Button(topcz,text='退出',command=topcz.destroy)
        btn6.grid(row=6,column=0)
        btn6.config(bg='SkyBlue')
        topcz.mainloop()
        
    def lend_book(self):
        #借阅书籍
        topld=tk.Tk()
        topld.title('借阅书籍')
        topld.geometry('400x200')
        topld.config(bg='LightSkyBlue')
        lab0=tk.Label(topld,text='请输入要借阅的书籍的索书号')
        lab0.pack()
        lab0.config(bg='LightSkyBlue')
        entry0=tk.Entry(topld)
        entry0.pack()
        entry0.config(bg='SkyBlue')
        lab1=tk.Label(topld)
        lab1.pack()
        lab1.config(bg='LightSkyBlue')
        def queren():
            bid=entry0.get()
            is_exist = False
            for book in self.inst.book_list:#在所有书籍中遍历
                if bid == book.bid:#找到对应书籍
                    is_exist = True
                    if int(book.available)==0:
                        lab1['text']='此书暂无库存'
                    else:
                        lab1['text']='你已借阅'+str(book.name)
                        book.available -= 1#可借数减一
                        self.inst.log_usr.books.append(book.bid)
                        self.inst.log_usr.give_back.append('未还')#未还信息
                        self.inst.log_usr.give_back_date.append('/')#未归还默认记录为/
            if not is_exist:
                lab1['text']='无书籍信息'
        btn0=tk.Button(topld,text='确认',command=queren)
        btn0.pack()
        btn0.config(bg='SkyBlue')
        btn1=tk.Button(topld,text='退出',command=topld.destroy)
        btn1.pack()
        btn1.config(bg='SkyBlue')
        topld.mainloop()
        
    def back_book(self):
        #归还书籍
        topgb=tk.Tk()
        topgb.title('归还书籍')
        topgb.geometry('400x200')
        topgb.config(bg='LightSkyBlue')
        lab0=tk.Label(topgb,text='请输入要归还的书籍的索书号')
        lab0.pack()
        lab0.config(bg='LightSkyBlue')
        entry0=tk.Entry(topgb)
        entry0.pack()
        entry0.config(bg='SkyBlue')
        lab1=tk.Label(topgb)
        lab1.pack()
        lab1.config(bg='LightSkyBlue')
        def queren():
            bid=entry0.get()
            is_exist = False
            sucess=False
            for bookbid in self.inst.log_usr.books:#在该用户已借阅的书籍中遍历
                if bid == bookbid:#找到已借的对应书籍
                    is_exist = True
                    for book in self.inst.book_list:
                    #将对应的已借书籍与book_list中的书籍匹配，以修改书籍信息、
                    #即，实现用户记录的索书号，输入的索书号，系统信息内索书号三者统一
                        if bid == book.bid:
                            sucess=True
                            lab1['text']='你已归还'+str(book.name)
                            book.available += 1
                            #找到用户所借书籍的索书号形成的列表中要处理的书籍对应的下标
                            num=int(self.inst.log_usr.books.index(bookbid))
                            self.inst.log_usr.give_back[num]='已还'#记录为已还
                            now=datetime.datetime.now().strftime('%Y-%m-%d')
                            print(str(now))
                            self.inst.log_usr.give_back_date[num]=str(now)#记录归还时间
                    if not sucess:
                            lab1['text']='已借书籍不能与信息库中书籍匹配，建议联系管理员'
            if not is_exist:
                lab1['text']='你未借阅此书'
        btn0=tk.Button(topgb,text='确认',command=queren)
        btn0.pack()
        btn0.config(bg='SkyBlue')
        btn1=tk.Button(topgb,text='退出',command=topgb.destroy)
        btn1.pack()
        btn1.config(bg='SkyBlue')
        topgb.mainloop()
        
    def usr_function(self):
        #普通用户模块
            topu=tk.Tk()
            topu.title('用户界面')
            topu.geometry('300x200')
            topu.config(bg='LightSkyBlue')
            labu=tk.Label(topu,text='尊敬的用户，请选择您所需的功能')
            labu.grid(row=0,column=2,rowspan=1,columnspan=2)
            labu.config(bg='LightSkyBlue')
            cx=tk.Button(topu,text='查询个人信息',command=self.check_usr)
            cx.grid(row=1,column=0)
            cx.config(bg='SkyBlue')
            cz=tk.Button(topu,text='查找图书',command=self.search_book)
            cz.grid(row=2,column=0)
            cz.config(bg='SkyBlue')
            jy=tk.Button(topu,text='借阅图书',command=self.lend_book)
            jy.grid(row=3,column=0)
            jy.config(bg='SkyBlue')
            gh=tk.Button(topu,text='归还图书',command=self.back_book)
            gh.grid(row=4,column=0)
            gh.config(bg='SkyBlue')
            tc=tk.Button(topu,text='退出用户界面',command=topu.destroy)
            tc.grid(row=5,column=0)
            tc.config(bg='SkyBlue')
            topu.mainloop()

            
