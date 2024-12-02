import streamlit as st
import google.generativeai as genai

# Configure the page
st.set_page_config(page_title="بصير - مساعد المكفوفين", page_icon="👁️")
st.title("بصير - مساعد المكفوفين")

# Configure API
genai.configure(api_key="AIzaSyBKcY3eOLnn_07Uc-hhiwwwzzfCI8yls4s")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are بصير (Baseer), an Arabic-speaking AI assistant specifically designed to help blind people."},
        {"role": "assistant", "content": "مرحباً! أنا بصير، مساعدك الشخصي. كيف يمكنني مساعدتك اليوم؟"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Text chat input
if prompt := st.chat_input("كيف يمكنني مساعدتك؟"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        system_prompt = """You are بصير (Baseer), an Arabic-speaking AI assistant specifically designed to help blind people. 
        Your responses should be in Arabic and focused on providing helpful, clear, and detailed assistance for visually impaired individuals. 
        Be extra descriptive when explaining visual concepts and always prioritize accessibility in your suggestions."""
        
        full_prompt = f"{system_prompt}\n\nUser: {prompt}"
        response = model.generate_content(full_prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})