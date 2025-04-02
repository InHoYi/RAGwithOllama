from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.document_loaders import TextLoader
from datetime import datetime


model = OllamaLLM(model="exaone3.5:latest")

def loadDocument(dir):
    loader = TextLoader(dir, encoding='UTF-8')
    documents = loader.load()
    return documents

document = loadDocument(f'article/article{datetime.today().strftime("%Y%m%d")}.txt')

template = ChatPromptTemplate.from_template("""
    질문에 대해서 context 부분을 읽고 query에 대한 답변을 한국어로 작성해줘.
    context : {context}
    질문 : {query}
    답변 : 
""")

chain = template | model | StrOutputParser()
result = chain.invoke({'context' : document, 'query' : "주요 뉴스를 요약해줘."})
print(result)