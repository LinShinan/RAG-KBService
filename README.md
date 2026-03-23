# 知识库服务

## 使用前提

①python中安装需要的库：

例如：

```
pip install streamlit
```

```
pip install langchain langchain-community langchain-ollama dashscope chromadb
```

以上不完整，请根据个人所缺自行安装其他库

② 进入阿里云百炼平台，创建相应的API-KEY,并把API-KEY配置到用户环境变量中，分别放在OPENAI_API_KEY和DASHSCOPE_API_KEY

![](assets/2026-03-23-10-23-40-image.png)

## 知识库上传服务

### 使用说明：

进入RAG-KBService中，输入cmd，然后输入

```
python -m streamlit run app_uploader.py
```

### 效果演示：

![](assets/2026-03-23-09-49-51-image.png)

## 智能问答服务

### 使用说明：

进入RAG-KBService中，输入cmd，然后输入

```
python -m streamlit run app_chat.py
```

### 效果演示：

![](assets/2026-03-23-09-41-17-image.png)

![](assets/2026-03-23-09-41-54-image.png)
