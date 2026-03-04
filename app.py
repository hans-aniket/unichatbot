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
    tag = model.predict(input_vec)[0]

    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I am not sure how to respond to that."

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = chatbot_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

for sender, msg in st.session_state.messages:
    if sender == "You":
        st.write(f"**You:** {msg}")
    else:
        st.write(f"**Bot:** {msg}")