"""
md5工具函数库
"""

from config import md5_path
import os
import hashlib

def check_md5(md5_str):
    """检查md5字符串是否被处理过"""
    if not os.path.exists(md5_path):
        dir_path=os.path.dirname(md5_path)
        if dir_path:
            os.makedirs(dir_path,exist_ok=True)
        open(md5_path, "w", encoding="utf-8").close()
        return False
    else:
       with open(md5_path,"r",encoding="utf-8") as f:
           for line in f:
               if line.strip() == md5_str:
                   return True
    return False

def save_md5(md5_str):
    "保存传入的字符串"
    with open(md5_path,"a",encoding="utf-8") as f:
        f.write(md5_str+"\n")

def get_md5(string,encoding="utf-8"):
    """将字符串转换成md5并返回"""
    str_bytes = string.encode(encoding=encoding)
    # print(type(str_bytes))
    md5 = hashlib.md5()
    md5.update(str_bytes)
    md5_hex = md5.hexdigest()
    return md5_hex


# if __name__ == "__main__":
#     md_ = get_md5("林俊杰")
#     print(md_)
#     save_md5(md_)
#     print(check_md5(md_))
