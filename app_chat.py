import streamlit as st
from rag import RagService
st.title("智能客服")


def stream(chain_invoke, res_list):
    for chunk in chain_invoke:
        res_list.append(chunk)
        yield chunk


if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

if "message" not in st.session_state:
    st.session_state["message"] = [{"role":"assistant","content":"您好，我是智能客服，有什么能够帮助您的。"}]

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

question = st.chat_input()

if question:
    st.chat_message("user").write(question)
    st.session_state["message"].append({"role":"user","content":question})
    with st.spinner("正在思考中..."):
       chain_invoke = st.session_state["rag"].chain.invoke({"input": question},
                                                         {"configurable": {"session_id": "user_006"}})
       res_list=[]


       st.chat_message("ai").write_stream(stream(chain_invoke,res_list))
       st.session_state["message"].append({"role":"ai","content":"".join(res_list)})

