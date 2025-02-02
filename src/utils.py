import os
import sys
import hashlib

def get_size(path):
    """获取文件或目录的总大小（字节）"""
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
    return 0

def get_resource_path(relative_path):
    """获取资源文件的绝对路径，兼容开发环境和打包后的环境"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller打包后的路径
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def hash_filename(filename):
    """使用 MD5 对文件名进行哈希"""
    return hashlib.md5(filename.encode('utf-8')).hexdigest() 