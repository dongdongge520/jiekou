import os

def data_dir(data=None,fileName=None):
    '''查找文件路径'''
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),data,fileName)

print(data_dir('data','data.xlsx'))