Different Embedding Algorithms:

eg. OpenAI Embeddings(1536 dimensions) SentenceTransformer(768 dimensions)
OpenAI Embeddings only disadvantage: cost a little bit to run. 

```python
#langchain has all kinds of textloader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

... 要面试了写不完了kk
```

