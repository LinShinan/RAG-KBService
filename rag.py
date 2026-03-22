from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from langchain_community.chat_models.tongyi import ChatTongyi
from vector_store import VectorStoreService
import config
from history_store import FileChatMessageHistory


def print_prompt(prompt):
    print("-"*40)
    print(prompt.to_string())
    print("-"*40)
    return prompt


def get_history(session_id):
    history = FileChatMessageHistory(session_id, config.history_store_path)
    return history

class RagService:

    def __init__(self):
        self.chat_model = ChatTongyi(model=config.chat_model_name)
        self.store_service = VectorStoreService()
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system","请参考我提供的资料:{reference},输出一个合适又简洁的回答。"),
                ("system","以下是用户历史记录:"),
                MessagesPlaceholder("history"),
                ("user","请回答用户的提问：{input}")
            ]
        )
        self.chain = self._get_chain()

    def _get_chain(self):
        retriever = self.store_service.get_retriever()
        def format_docs(docs):
            if not docs:
                return "无参考资料"
            format_str = ""
            for doc in docs:
                format_str += doc.page_content + "\n\n"
            return format_str

        def debug(input):
            print("-"*20)
            print(input)
            print("-"*20)
            return input

        def transform(value):
            new_value={}
            new_value["input"]=value["input"]["input"]
            new_value["history"]=value["input"]["history"]
            new_value["reference"]=value["reference"]
            return new_value

        chain = (
            {
                "input":RunnablePassthrough(),
                "reference": RunnableLambda(lambda x:x["input"])
                             | retriever | format_docs
            }
            | RunnableLambda(transform)
            | self.prompt_template
            | RunnableLambda(print_prompt)
            |self.chat_model
            | StrOutputParser()
        )

        chain_with_history = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history"
        )

        return chain_with_history



if __name__ == "__main__":
    session_config={
        "configurable":{
            "session_id":"user_007"
        }
    }
    res = RagService().chain.invoke({"input": "我身高180,推荐衣服尺寸"}, session_config)
    print(res)
