import streamlit as st
from transformers import pipeline
import random

chatbot = pipeline("text-generation", model="gpt2")

if "convo_list" not in st.session_state:
    st.session_state.convo_list = []

st.title("Assistant Teacher")

st.write("an app for students to ask their questions on school subjects")

# function that starts a new chat
# will change to pin previous conversations to sidebar
def new_chat():
    st.session_state.messages.clear()
    return

def start_convo():
    new_convo = Conversation(prompt)
    new_convo.add_message(prompt)
    st.session_state.convo_list.append(new_convo)
    return

def update_convo(new_convo):
    st.session_state.messages = new_convo
    return

def generate_response(prompt):
    response = chatbot(prompt, max_length=100)
    return response[0]['generated_text']

class Conversation:
    def __init__(self, label):
        self.label = prompt
        self.messages = []
        # will add a key to each conversation to find it in the sidebar
        self.key = random.randint(0, 1000000)
    
    def add_message(self, message):
        self.messages.append({"role": "user", "content": message})
        return

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
        if not st.session_state.messages: start_convo()

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.convo_list[-1].add_message(prompt)
    # will fix to find prompt given a key

# sidebar functionality
with st.sidebar:
     # button to start a new chat
    new_chat_button = st.button("New Chat", on_click=lambda:new_chat())

    st.title("Previous Conversations")
    # will have the sidebar display a title for old conversations
    # for now, it will just display the most recent message
    if not st.session_state.convo_list:
        st.write("*No Previous Conversations*")
    else:
        for convo in reversed(st.session_state.convo_list):
            print(st.session_state.messages)
            st.button(convo.label, on_click=lambda:update_convo(convo.messages))
    
