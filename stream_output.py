from openai import OpenAI
import streamlit as st
from get_voting_data import get_all_rounds_data
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_KEY = os.getenv("API_KEY")
st.title("DROX GPT")

client = OpenAI(api_key=OPENAI_KEY)

def fetch_context_data():
    # Simulate data retrieval, replace this with real data fetching code
    return get_all_rounds_data()

# "Fetch Data" button
if st.button("Fetch Data"):
    st.session_state.context = fetch_context_data()
    st.session_state.fetch_success = True  # Set success state
    st.success("Data fetched successfully!")


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
            {"role": "system", "content": f"Answer the following question using this data: {st.session_state.context}."},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})