import google.generativeai as genai 
import streamlit as st


genai.configure(api_key="AIzaSyA1qn_AR21xBfrzTxO-KrumfP0fL_uv1Vg")

st.title("Gemini-ChatBot")


def load_model():
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    print("model loaded...")
    return model

model = load_model()

if "chat_session" not in st.session_state:    
    st.session_state["chat_session"] = model.start_chat(history=[]) 

for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메시지를 입력하세요."):    
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(prompt)        
        st.markdown(response.text)