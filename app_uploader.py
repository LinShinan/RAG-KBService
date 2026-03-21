"""
知识库更新服务
"""
import streamlit as st

st.title("知识库更新服务")

file = st.file_uploader(
    label="上传txt文件",
    type=['txt'],
    accept_multiple_files=False
)

if file is not None:
    st.subheader(f"文件名：{file.name}")
    st.write(f"类型：{file.type}，大小：{file.size/1024:.2f} KB")
    text = file.getvalue().decode("utf-8")
    st.write(text)