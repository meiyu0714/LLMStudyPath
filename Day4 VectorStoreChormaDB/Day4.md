ChromaDB

install chromaDB

```python
pip install chromaDB
```

 

```python
db = Chroma.from_documents(
    # three different documents
    docs, #past list of docs 
    embedding=embeddings, # make them into embeddings. This is actually calculate embeddings. 
    persist_directory='emb' 
) # duplicate of the embeddings. because each time we run the program, we do the dbagain. 
```

LangChain RetrivalQA: Building a Retrieval Chain.

Langchain embedded chained thing for you to find the closest answer. 

![image-20240604205705342](C:\Users\zzhez\Desktop\image-20240604205705342.png)

A piece of glue code that Langchain had to make the whole project work. 

chain_type = "stuff". Take some context from the vector store and "stuff" into the prompt.

Three other Chain types: 

#### Section 6

![image-20240604210614408](C:\Users\zzhez\AppData\Roaming\Typora\typora-user-images\image-20240604210614408.png)

