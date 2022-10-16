# coding=utf-8
import os

# 子类集合
sonclass_set = set()
# 类集合
class_set = set()
# 调用其他模块次数
fanin_list = []
# 被调用次数
fanout_list = []
# 类名集合
classname_list = []
# 定义代码所在的目录
base_path = "D:\Study\大学\作业平台\B211107_薛景\B211107_学生材料\第03小组_健康饮食推荐系统\健康饮食推荐系统"


# 在指定目录下统计所有的py文件，以列表形式返回
def collect_files(dir):
    filelist = []
    pyfile_num = 0  # .py文件数
    picfile_num = 0  # 图片文件数 .png .bmp .jpg .jepg .gif
    audiofile_num = 0  # 音频文件数 .mp3 .wav
    videofile_num = 0  # 视频文件数 .flv .avi .mov .mp4 .wmv
    docfile_num = 0  # 文档数
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.bmp') or filename.endswith('.jpg') or filename.endswith(
                    '.gif'):
                picfile_num += 1
            if filename.endswith('.mp3') or filename.endswith('.Mp3') or filename.endswith('.wav'):
                audiofile_num += 1
            if filename.endswith('.flv') or filename.endswith('.avi') or filename.endswith('.mov') or filename.endswith(
                    '.mp4') or filename.endswith('.wmv'):
                videofile_num += 1
            if filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.txt'):
                docfile_num += 1
            if filename.endswith('.py'):
                pyfile_num += 1
                # 将文件名和目录名拼成绝对路径，添加到列表里
                filelist.append(os.path.join(parent, filename))
    print('模块总数：   %s' % pyfile_num)
    print('图片文件数：   %s' % picfile_num)
    print('音频文件数：   %s' % audiofile_num)
    print('视频文件数：   %s' % videofile_num)
    print('文档数：   %s' % docfile_num)
    return filelist


# 计算单个文件内的代码行数
def calc_lines(file):
    with open(file, encoding='utf-8') as fp:
        content_list = fp.readlines()
        code_num = 0  # 当前文件代码行数计数变量
        blank_num = 0  # 当前文件空行数计数变量
        annotate_num = 0  # 当前文件注释行数计数变量
        class_num = 0  # 当前文件class数
        sonclass_num = 0  # 当前文件子类数
        # sonclass_set = set() #当前文件子类集合
        classmethod_num = 0  # 当前文件静态方法数
        for content in content_list:
            content = content.strip()
            # 统计空行
            if content == '':
                blank_num += 1
            # 统计注释行
            elif content.startswith('#'):
                annotate_num += 1
            # 统计类数
            elif content.startswith("class"):
                # class_num += 1
                code_num += 1
                # print("...")
                # print("%s" % content)
                # print(content[6:len(content)-2])
                if content[len(content) - 2] != ')':
                    class_set.add(content[6:len(content) - 1])
                    class_num += 1
                    # print(content[6:len(content)-1])
                    continue
                s = content[6:len(content) - 2]
                if (s not in class_set):
                    class_set.add(s)
                    class_num += 1
                    # print(s)
                if s[len(s) - 1] != "(" and s[len(s) - 6:len(s)] != "Object" and s[len(s) - 6:len(s)] != "object":
                    # print(s[len(s)-6:len(s)-1])
                    # sonclass_num += 1
                    if (s not in sonclass_set):
                        sonclass_set.add(s)
                        # print(s)
                        sonclass_num += 1
            elif content.__contains__("@classmethod"):
                classmethod_num += 1
                code_num += 1
            # 统计代码行
            else:
                code_num += 1
    # 返回代码行数，空行数，注释行数
    return code_num, blank_num, annotate_num, class_num, sonclass_num, classmethod_num


def calc_static_property(file):
    with open(file, encoding="utf-8") as fp:
        content_list = fp.readlines()
        def_num = 0  # 当前文件方法数
        property_num = 0  # 当前文件静态属性数
        pro_num = 0  # 一个类中静态属性数
        flag = 0  # 是否在类中

        for content in content_list:
            content = content.strip()
            if content.__contains__("class"):
                pro_num = 0
                flag = 1
                # print("...")
            if content.__contains__("=") and flag == 1:
                pro_num += 1
            elif content.__contains__("def"):
                property_num += pro_num
                pro_num = 0
                flag = 0

        # for content in content_list:
        #  content = content.strip()
        # if content.__contains__()

        for content in content_list:
            content = content.strip()
            if content.__contains__("def"):
                def_num += 1
    return def_num, property_num


def calc_invoke(file):
    with open(file, encoding="utf-8") as fp:
        content_list = fp.readlines()
        flag = -1  # 标记当前类
        invoke = set()  # 一个类对另一个类的调用只记录一次

        class_list = list(class_set)
        length = len(class_set)
        fanin_list = [0] * length
        fanout_list = [0] * length
        instability = [0] * length

        classname_set = set()
        for i in class_list:
            i = i.split("(")
            classname_set.add(i[0])

        classname_list = list(classname_set)
        print(classname_list)

        for content in content_list:
            content = content.strip()
            if content.startswith("class"):
                flag = class_list.index(content[6:len(content) - 2])
            index = list_contain(content, classname_list)
            if index != -1:
                s = str(flag) + "->" + str(index)
                if s not in invoke:
                    invoke.add(s)
                    fanin_list[flag] += 1
                    fanout_list[index] += 1

        print(invoke)
        print(fanin_list)
        print(fanout_list)

        # bug1
        # i = 0
        # for num in instability:
        #    instability[i] = fanout_list[i] / (fanin_list[i] + fanout_list[i])
        #    i += 1
        # print(instability)

    # 遍历文件
    # 对同一个类：计算每个方法的self+不含()的变量list
    # 得到一个关系set 所有不在set中的方法对为结果


def calc_method_pair(file):
    with open(file, encoding="utf-8") as fp:
        content_list = fp.readlines()
        method_num = -1  # 当前类中方法数
        classes_num = -1
        class_method = []  # 记录每个类的方法数
        total_list = []  # 当前类中所有方法实例变量数

        # bug2
        # for content in content_list:
        #    if content.startswith("class"):
        #        print(content)
        #        classes_num += 1
        #        method_num = 0
        #        class_method.append(0)
        #    if content.__contains__("def"):
        #        method_num += 1
        #        class_method[classes_num] = method_num
        # print(class_method)

        flag = 0  # 标记循环次数
        classes_num = -1
        class_list = []  # 存储当前类中，每个方法包含的实例变量
        methodpair_num = 0  # 所有方法对数
        share_methodpair_num = 0  # 有共享变量的方法对数
        for content in content_list:
            if content.startswith("class"):
                #  bug3
                print(content)
                # print(total_list)
                # 判断两个集合是否有交集
                if classes_num > -1:
                    for i in class_list:
                        flag += 1
                        for j in class_list[flag:]:
                            set_1 = set(i)
                            set_2 = set(j)
                            res = set_1 & set_2
                            if res != set():
                                share_methodpair_num += 1
                    print("有共同实例变量的方法对：  %s" % share_methodpair_num)
                    print(class_list)
                flag = 0
                share_methodpair_num = 0
                method_num = -1
                classes_num += 1
                class_list = []  # 当前类中，方法属性集合
            if content.__contains__("def"):
                # print(content)
                method_num += 1
                vars_set = set()
                class_list.append(vars_set)
            if content.__contains__("self.") and "(" not in content and "#" not in content:
                content = content.strip()
                temp = content.split(" ")
                # print(temp)
                # 截取self.后的元素
                for i in temp:
                    i = i.split("[")
                    for j in i:
                        if j.__contains__("self"):
                            j = j.split(".")
                            vars_set.add(j[1])
                            class_list[method_num] = vars_set
                    # if i.__contains__("self"):
                    #    vars_set.add(i)
                    #    class_list[method_num] = vars_set
        for i in class_list:
            flag += 1
            for j in class_list[flag:]:
                set_1 = set(i)
                set_2 = set(j)
                res = set_1 & set_2
                if res != set():
                    share_methodpair_num += 1
        print("有共同实例变量的方法对：  %s" % share_methodpair_num)
        print(class_list)


def list_contain(str, classname_list):
    flag = -1
    for classname in classname_list:
        if classname in str:
            flag = classname_list.index(classname)
            # print(classname)
            # print(flag)
    return flag


if __name__ == '__main__':
    files = collect_files(base_path)
    total_code_num = 0  # 统计文件代码行数计数变量
    total_blank_num = 0  # 统计文件空行数计数变量
    total_annotate_num = 0  # 统计文件注释行数计数变量
    total_class_num = 0  # 统计总类数
    total_sonclass_num = 0  # 子类数
    total_classmethod_num = 0  # 统计总静态方法数
    total_def_num = 0  # 统计总方法数
    total_property_num = 0  # 统计总静态属性数
    for f in files:
        code_num, blank_num, annotate_num, class_num, sonclass_num, classmethod_num = calc_lines(f)
        total_code_num += code_num
        total_blank_num += blank_num
        total_annotate_num += annotate_num
        total_class_num += class_num
        total_sonclass_num += sonclass_num
        total_classmethod_num += classmethod_num

    for f in files:
        def_num, property_num = calc_static_property(f)
        total_def_num += def_num
        total_property_num += property_num

    for f in files:
        calc_invoke(f)

    print('代码总行数为：  %s' % total_code_num)
    print('空行总行数为：  %s' % total_blank_num)
    print('注释行总行数为： %s' % total_annotate_num)
    print('总类数：  %s' % len(class_set))
    print('子类数：   %s' % len(sonclass_set))
    print('静态方法数：   %s' % total_classmethod_num)
    print('方法数：   %s' % total_def_num)
    print('静态属性数：   %s' % total_property_num)
    # print(sonclass_set)

    for f in files:
        calc_method_pair(f)
