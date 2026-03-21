"""
知识库
"""
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

import config
import os
import md5_util
from datetime import datetime

class KnowledgeBase:
    def __init__(self):
        #确保持久化目录存在
        os.makedirs(config.persist_directory,exist_ok=True)
        # 创建向量库对象
        self.chroma=Chroma(
            collection_name=config.collection_name,
            embedding_function=DashScopeEmbeddings(model=config.embedding_name),
            persist_directory=config.persist_directory
        )

        # 文本分割器
        self.spliter =RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=config.separator
        )

    def upload_str(self,data,filename):
        """将字符串进行向量化，传入向量库"""

        # 转换成md5，避免重复保存
        md5_hex=md5_util.get_md5(data)

        if md5_util.check_md5(md5_hex):
            return "[skip]内容过去已经存在于知识库中"


        # 根据情况使用分割器
        if len(data) > config.max_split_char_number:
            texts = self.spliter.split_text(data)
        else:
            texts=[data]

        # 把数据保存到知识库中
        metadata ={
            "source":filename,
            "create_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator":"LinShinan"
        }
        self.chroma.add_texts(
            texts=texts,
            metadatas= [metadata for _ in texts] #每份text都对应同样的metadata[metadata,metadata...]
        )

        md5_util.save_md5(md5_hex)
        return "[success]已保存到知识库中"


if __name__ == '__main__':
    kb=KnowledgeBase()
    show = kb.upload_str("Hello, it's me.","test")
    print(show)
