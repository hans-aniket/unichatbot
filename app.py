import streamlit as st
import json
import random
import pickle

st.title("IIITD Chatbot")

try:
    with open('intents.json') as file:
        data = json.load(file)

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

def chatbot_response(user_input):
    input_vec = vectorizer.transform([user_input.lower()])
    probabilities = model.predict_proba(input_vec)[0]
    max_prob = max(probabilities)

    if max_prob < 0.25:
        return "I'm not sure. I can answer questions about IIITD's location, fees, placements, facilities, courses, timings, labs, and attendance."

    tag = model.classes_[probabilities.argmax()]

    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I am not sure how to respond to that."

# Initialize chat history using dictionaries
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input using the native chat input element
if prompt := st.chat_input("Ask me something about IIITD..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get chatbot response
    response = chatbot_response(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})