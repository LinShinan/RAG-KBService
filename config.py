#md5工具配置
md5_path = "./config_data/md5.text"

# 向量库配置
embedding_name="text-embedding-v4"
collection_name="knowledge_base"
persist_directory="./chroma_db"

#分割器配置
separator=["\n\n","\n",".","!","?",",","。","！","？","，"," ",""]
chunk_size=500
chunk_overlap=20
max_split_char_number = 1000

# 模型配置
chat_model_name="qwen3-max"


# 历史记录配置
history_store_path="./chat_history"
