import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def runOllama(message):
    llm = ChatOllama(model="exaone3.5:latest")
    prompt = ChatPromptTemplate.from_template("{message}")
    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({"message": message})
    return answer

def main():
    st.set_page_config(page_title="🦜🔗뭐든지 질문하세요~~")
    st.title("🦜🔗뭐든지 질문하세요~~")

    if 'history' not in st.session_state:
        st.session_state.history = []

    user_message = st.text_input("메세지를 입력하세요.", key='user_input')

    if st.button("입력"):
        if user_message: 
            answer = runOllama(user_message)
            st.session_state.history.append(f"Me : {user_message}")
            st.session_state.history.append(f"Ollama : {answer}")
            st.text_area("대화 내역", '\n'.join(st.session_state.history), height=250)

if __name__ == "__main__":
    main()