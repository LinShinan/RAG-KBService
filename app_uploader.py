"""
知识库更新服务
"""
import time

import streamlit as st
from knowledge_base import KnowledgeBase

st.title("知识库更新服务")

# 第一次运行时，创建知识库对象
if "base" not in st.session_state:
    st.session_state["base"] =KnowledgeBase()

file = st.file_uploader(
    label="上传txt文件",
    type=['txt'],
    accept_multiple_files=False
)

if file is not None:
    st.subheader(f"文件名：{file.name}")
    st.write(f"类型：{file.type}，大小：{file.size/1024:.2f} KB")
    text = file.getvalue().decode("utf-8")
    # st.write(text)
    info = st.session_state["base"].upload_str(text,file.name)
    with st.spinner(text="正在处理中..."):
        time.sleep(1)
        st.write(info)
