from os import listdir
from os import path as op
import re


class JavaCodeAnalyzer:
    def __init__(self):
        self.filelist = []
        self.filepath = ""
        self.row_count = self.blank_count = self.note_count = self.code_count = 0
        self.keywords = {key: 0 for key in
                         ["abstract", "assert", "boolean", "break", "byte",
                          "case", "catch", "char", "class", "const",
                          "continue", "default", "do", "double", "else",
                          "enum", "extends", "final", "finally", "float",
                          "for", "goto", "if", "implements", "import",
                          "instanceof", "int", "interface", "long", "native",
                          "new", "package", "private", " protected", "public",
                          "return", "strictfp", "short", "static", "super",
                          "switch", "synchronized", "this", "throw", "throws",
                          "transient", "try", "void", "volatile", "while"]}

    def search(self, path):
        # 递归搜索.java格式文件
        files = listdir(path)
        for file in files:
            self.filepath = path + "\\" + file
            if op.isdir(self.filepath):
                self.search(self.filepath)
            else:
                if self.filepath.endswith('.java'):
                    self.filelist.append(self.filepath)

    def count(self):
        # 计算.java文件个数和总大小
        length = len(self.filelist)
        size = sum([op.getsize(file) for file in self.filelist])
        print("文件总数：", length)
        print("文件总大小：", size)

    def keyword_analyze(self, filepath):
        # 统计源文件的关键字出现次数
        with open(filepath, encoding='gb18030', errors='ignore') as file:
            lines = file.read().split('\n')  # 一次性读取一个文件,并用换行分割每一行
        for line in lines:
            noteline = re.match(r'^/(.*)|^\*(.*)|(.*)\*/$', line.strip(), flags=0)  # 匹配以/* 或者* 或者 //开头 或*/结尾的注释行
            if noteline is None:  # 匹配为代码行
                codeline = re.sub(r'//(.*)$|/\*(.*)|\"(.*)\"', '', line)  # 去除行后注释,字符串直接量的代码行
                filterline = re.sub('\W', ' ', codeline)  # 过滤行中'{ , } .+-='等字符
                for key in filterline.split(' '):
                    if key in self.keywords.keys():
                        self.keywords[key] += 1
            else:
                pass

    def code_analyze(self, filepath):
        # 统计源文件的代码行数,注释行数等
        with open(filepath, encoding='gb18030', errors='ignore') as file:
            lines = file.read().strip().split('\n')  # 一次性读取一个文件,并用换行分割每一行
            self.row_count += len(lines)
        for line in lines:
            if line == '':
                self.blank_count += 1
                continue
            noteline = re.match(r'^/(.*)|^\*(.*)|(.*)\*/$', line.strip(), flags=0)  # 匹配以/、/* 、*开头 或*/结尾的注释行
            if noteline is None:  # 匹配为代码行
                self.code_count += 1
            else:
                self.note_count += 1

    def display(self):
        # 输出分析结果
        print("源程序总行数:", self.row_count)
        print("代码行数:", self.code_count, ",占", round(self.code_count / self.row_count * 100, 2), "%")
        print("注释行数:", self.note_count, ",占", round(self.note_count / self.row_count * 100, 2), "%")
        print("空白行数:", self.blank_count, ",占", round(self.blank_count / self.row_count * 100, 2), "%")
        for i in range(5):
            sort = sorted(self.keywords.items(), key=lambda x: x[1], reverse=True)
            print("关键字  ", sort[i][0], ": ", sort[i][1], "次")


analyzer = JavaCodeAnalyzer()
analyzer.search("C:\\Users\\JY\\IdeaProjects\\javase\\Project1\\src")
analyzer.count()
count = 1
for path in analyzer.filelist:
    for key in analyzer.keywords:
        analyzer.keywords[key] = 0
    analyzer.row_count = analyzer.blank_count = analyzer.note_count = analyzer.code_count = 0
    analyzer.keyword_analyze(path)
    analyzer.code_analyze(path)
    print()
    print(count)
    print(path)
    analyzer.display()
    count += 1
