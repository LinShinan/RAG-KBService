import json,os
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import BaseMessage, messages_from_dict, message_to_dict



class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path,self.session_id)
        os.makedirs(os.path.dirname(self.file_path),exist_ok = True)

    # 将历史融合->dict ->json->写入文件中
    def add_messages(self,messages:Sequence[BaseMessage]):
        all_messages = list(self.messages)
        all_messages.extend(messages) # 新有的list和已有的list融合
        new_messages=[message_to_dict(message) for message in all_messages]
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)

    """
        @property 是 Python 中的一个内置装饰器，它的作用是将一个方法转换为只读属性，
        从而让你可以像访问属性一样调用它（即不加括号），同时可以在方法内部执行一些逻辑（如计算、读取文件、验证等）。
    """
    # 读取文件信息json -> messages_data -> messages
    @property
    def messages(self):
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                message_data= json.load(f)
            return messages_from_dict(message_data)
        except FileNotFoundError:
            return []

    # 写入空列表
    def clear(self):
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)