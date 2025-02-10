import streamlit as st
from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

def generate_response(prompt):
    response = chatbot(prompt, max_length=100)
    return response[0]['generated_text']

st.title("Assistant Teacher")
st.write("an app for students to ask their questions on school subjects.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("how can I help you?"):
    # Display user message in chat message container
    response = generate_response(prompt)
    st.write(f"Assistant Teacher: {response}")
    
    # Display AI response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear input field
    st.chat_input("").clear()
    st.text("")  # Add a space to the input field for readability and user experience.
    
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    