import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post('http://localhost:8000/essay/invoke',
                json={'input': {'topic': input_text}})
    
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response=requests.post('http://localhost:8000/poem/invoke',
                json={'input': {'topic': input_text}})
    
    return response.json()['output']

st.title('Langchain Demo WIth LLAMA3 API')

option = st.selectbox(
    "What do you want to do?",
    ("Essay", "Poem"))

input_text=st.text_input('Context')

if option == 'Essay':
    st.write(get_openai_response(input_text))
elif option == 'Poem':
    st.write(get_ollama_response(input_text))