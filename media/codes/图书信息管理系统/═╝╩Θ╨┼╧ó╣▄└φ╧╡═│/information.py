class User():
    def __init__(self, uid:str, pwd:str, is_manager: int):
        #设定对应属性
        self.uid = uid#用户名
        self.pwd = pwd#密码
        self.books = []#所借书籍索书号
        self.give_back = []#所借书籍是否归还
        self.give_back_date = []#归还时间，未归还则为“/”
        self.is_manager = is_manager#是否为管理员，布尔值表示

    def __str__(self):
        #当调用User类的实例时，以如下形式输出字符串
        return self.uid + "\t" + self.pwd + "\t" + str(self.is_manager)
        #“\t”为制表符，相当于一个“tab”
    
class Book():

    def __init__(self, bid:int, name:str, author:str, press:str, btype:str, amount: int, available: int):
        self.bid = bid  # 索书号
        self.name = name  # 书名
        self.author = author  # 作者
        self.press = press  # 出版社
        self.btype = btype  # 图书类别
        self.amount = amount  # 库存总量
        self.available = available  # 可借本书

    def __str__(self):
        #当调用Book类的实例时，以如下形式输出字符串
        return self.bid + "\t" + self.name + "\t" + self.author + "\t" + self.press + "\t" + self.btype + "\t" \
               + str(self.amount) + "\t" + str(self.available)

    def __eq__(self, other):
        #对比方法，应用于判断类的对象及其属性是否相等（“==”）
        #不用此方法可能因为同一类下不同对象地址不同而无法输出正确的布尔值
        #（即使两实例的属性完全相同）
        return type(self) == type(other) and self.bid == other.bid
