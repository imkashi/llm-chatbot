import streamlit as st
import openai
import ollama

# Configure your OpenAI API key (store securely in .env or Streamlit secrets)
openai.api_key = "API_KEY"

st.set_page_config(page_title="LLM Chatbot", page_icon="🤖")
st.title("🤖 Chat with GPT")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=st.session_state.messages
    # )

    # reply = response['choices'][0]['message']['content']

    response = ollama.chat(model="mistral", messages=st.session_state.messages)
    reply = response['message']['content']

    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
