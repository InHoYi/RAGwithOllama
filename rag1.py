from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="exaone3.5:latest")

loader = WebBaseLoader('https://news.naver.com')
docs = loader.load()
text_data = [doc.page_content for doc in docs]


chain = load_summarize_chain(model, chain_type = "stuff") 
# stuff 옵션 -> 다 집어넣어주세요.
# map_reduce 옵션 -> 길이가 긴 경우
result = chain.invoke(text_data)
print(result)