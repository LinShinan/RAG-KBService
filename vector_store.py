from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings

import config


class VectorStoreService:
    def __init__(self):
        self.chroma = Chroma(
            collection_name=config.collection_name,
            embedding_function=DashScopeEmbeddings(model=config.embedding_name),
            persist_directory=config.persist_directory
        )

    def get_retriever(self,k=2):
        return self.chroma.as_retriever(search_kwargs={"k":k}) # 默认参数为2


if __name__ == '__main__':
    retriever = VectorStoreService().get_retriever(1)
    res = retriever.invoke("我身高174，体重115斤，尺码推荐")
    print(type(res))
    for i in res:
        print(i.page_content)