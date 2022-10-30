import os
import zipfile


def unzip_file(zip_src, dst_dir):
    """
    解压zip文件
    :param zip_src: zip文件的全路径
    :param dst_dir: 要解压到的目的文件夹
    :return:
    """
    if zipfile.is_zipfile(zip_src):
        zip_file_contents = zipfile.ZipFile(zip_src, 'r')
        for file in zip_file_contents.namelist():
            zip_file_contents.extract(file, dst_dir)  # 解压缩ZIP文件
        for root, dirs, file_list in os.walk(dst_dir):
            for dir in dirs:
                real_name = dir.encode('cp437').decode('gbk')  # 先使用cp437编码，然后再使用gbk解码
                if real_name != dir:
                    os.rename(os.path.join(root, dir), os.path.join(root, real_name))  # 重命名文件
            for file in file_list:
                real_name = file.encode('cp437').decode('gbk')  # 先使用cp437编码，然后再使用gbk解码
                if real_name != file:
                    os.rename(os.path.join(root, file), os.path.join(root, real_name))  # 重命名文件
