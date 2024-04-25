from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

def re():
    st.title("Chat Bot..🤖")
    with st.sidebar:
        st.info("Startup chatbot")
    def rebot():

        

        llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.2)
            
        if "messages" not in st.session_state:
                        st.session_state.messages = [{'role':'assistant', 'content':'Hi! How  may I assist you today?'}]
        for message in st.session_state.messages:
                        with st. chat_message(message["role"]):
                            st. write (message["content"])


        template = """You are chat bot for startup guide give response in that manner

            {chat_history}
            Human: {human_input}
            Chatbot:
            """

        prompt = PromptTemplate(
            input_variables=["chat_history", "human_input"], template=template)
        memory = ConversationBufferMemory(memory_key="chat_history")
            
        conversation = LLMChain(memory=memory,
                prompt=prompt, llm=llm, verbose=True)
            
        qu=st.chat_input("Ask Your Question")
        if qu:
                st. session_state. messages.append({"role": "user","content": qu})
                with st.chat_message ("user"):
                    st.write(qu)
            
        if st.session_state.messages[-1]['role']!= 'assistant':
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking🤔..."):
                            response = conversation.run(qu)
                        st. write(response)
                        st. session_state.messages. append(
                                    {"role": "assistant",
                                    "content": response})
    rebot()