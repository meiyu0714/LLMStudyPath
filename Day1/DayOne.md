**KeyWords**: LLM, LangChain, Chain

**LangChain** is a framework designed for developing applications powered by large language models (LLMs). It provides tools to easily integrate and manage LLMs for various tasks, making it accessible for developers to create powerful language-based applications.  [LangChain Doc](https://python.langchain.com/v0.1/docs/get_started/introduction)

eg. LangChain make swap databases or LLM models(openai, claude, Llama, etc) quick and easy. And LangChain has many useful function like using the pdf file into the application. 

**Chain**: In LangChain, a "chain" refers to a sequence of modular components or steps that work together to process input data, interact with a large language model (LLM), and produce a desired output. Chains can be simple or complex, depending on the application requirements. Chain is the foundation piece to make resuable text generation pipeline. To create a chain, you need a prompt template and a language model. 

```python
poem_prompt = PromptTemplate(
    input_variables=["subject"],
    template="Write a very short poem about {subject}"
)
poem_chain = LLMChain(
    llm=llm,
    prompt=poem_prompt
)
 
result = poem_chain({ "subject": "snow" })
 
print(result)
```

The command line result would be sth. like the following(result will be a map)

```bash
{
    "subject" : "snow"
    "text": "Snow is magical"
}
```

**Openai API Usage Notice**: 使用前往里冲5刀。openai api免费$5额度只在注册openai account前三个月可使用。

### Setup

##### Python

You must have the 3.11 version of Python installed: https://www.python.org/downloads/   This is very important, as only a few versions of Python support LangChain and OpenAI.

##### Pipfile

\1. If you have not already done so, create a **pycode** directory somewhere on your development machine.
\2. In your terminal run `pip install pipenv` or depending on your environment, `pip3 install pipenv`

\3. Create a file in your pycode project directory called **Pipfile**

\4. Copy paste the following code into that new Pipfile (or drag and drop the file that is attached to this lecture into your **pycode** project directory):

```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi" 

[packages]
langchain = "==0.0.352"
openai = "==0.27.8"
python-dotenv = "==1.0.0" 

[dev-packages] 

[requires]
python_version = "3.11"
```

\5. Inside your **pycode** project directory, run the following command to install your dependencies from the Pipfile:

```bash
pipenv install
```

\6. Run the following command to create and enter a new environment:

```bash
pipenv shell
```

After doing this your terminal will now be running commands in this new environment managed by Pipenv.

Once inside this shell, you can run Python commands just as shown in the lecture videos.

eg:

```bash
python main.py
```

\7. If you make any changes to your environment variables or keys, you may find that you need to exit the shell and re-enter using the `pipenv shell` command.