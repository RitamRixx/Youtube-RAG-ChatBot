# app.py — Streamlit chat interface

import streamlit as st
from src.rag_pipeline import process_video, build_rag_chain, ask_question

st.set_page_config(page_title="YouTube RAG Chatbot", layout="centered")
st.title("YouTube RAG Chatbot")
st.caption("Ask questions about any YouTube video using AI.")

# --- Session state init ---
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "video_processed" not in st.session_state:
    st.session_state.video_processed = False

# --- Video input section ---
with st.form("video_form"):
    url = st.text_input("Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
    submitted = st.form_submit_button("Process Video")

if submitted and url:
    with st.spinner("Fetching transcript and building index..."):
        try:
            vector_store = process_video(url)
            st.session_state.rag_chain = build_rag_chain(vector_store)
            st.session_state.chat_history = []
            st.session_state.video_processed = True
            st.success("Video processed! You can now ask questions.")
        except Exception as e:
            st.error(f"Error: {e}")

# --- Chat interface ---
if st.session_state.video_processed:
    st.divider()
    st.subheader("Chat with the Video")

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Ask a question about the video...")

    if user_input:
        # Show user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = ask_question(st.session_state.rag_chain, user_input)
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error: {e}")