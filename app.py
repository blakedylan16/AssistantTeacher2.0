import streamlit as st

if "convo_list" not in st.session_state:
    st.session_state.convo_list = []

st.title("Assistant Teacher")

st.write("an app for students to ask their questions on school subjects.")

# function that starts a new chat
# will change to pin previous conversations to sidebar
def new_chat():
    st.session_state.messages.clear()
    return

# def new_chat():
#     # Append the prompt to the conversation list if it's not None
#     if 'prompt' in st.session_state and st.session_state.prompt:
#         st.session_state.convo_list.append(st.session_state.prompt)
#     # Clear messages for a new chat
#     st.session_state.messages = []

def start_convo():
    st.session_state.convo_list.append(prompt)
    return

class Conversation:
    def __init__(self, label):
        self.label = prompt
        self.messages = []
    
    def add_message(self, message):
        self.messages.append(message)

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
    with st.chat_message("user"):
        st.markdown(prompt)
        if not st.session_state.messages: start_convo()

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


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
            st.write(convo)
    
   
