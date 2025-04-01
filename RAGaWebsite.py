from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = OllamaLLM(model="exaone3.5:latest")


loader = WebBaseLoader('원하는 URL')
docs = loader.load()

template = ChatPromptTemplate.from_template("""
    질문에 대해서 context 부분을 읽고 답변을 한국어로 작성해줘.
    context : {context}
    질문 : {query}
    답변 : 
""")

chain = template | model | StrOutputParser()
result = chain.invoke({'context' : docs, 'query' : "요약해줘."})
print(result)
