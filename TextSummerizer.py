import streamlit as st
from xai_sdk import Client
from xai_sdk.chat import system, user

# --- App Title ---
st.title("Text Summarizer")
st.markdown("Enter your text below and get a clean, structured summary powered by AI.")

# --- Input Section ---
text = st.text_area("Enter your text here:", height=250)

# --- API Key from Streamlit secrets ---
try:
    GROK_API_KEY = st.secrets["GROK_API_KEY"]
except KeyError:
    st.error("Grok API key is missing!")
    st.stop()

client = Client(api_key=GROK_API_KEY)

# --- Button ---
summarize = st.button("Summarize")

# --- Action ---
if summarize:
    try:
        if not text.strip():
            st.error("Please enter some text first.")
            st.stop()

        prompt = f"""
You are an expert text summarizer with deep understanding of context, logic, and clarity.
Your job is to read the given text carefully and generate a summary that captures its key points 
in a professional, human-like tone.

Follow these strict rules:

1. Capture core ideas, reasoning, and insights — not every line.
2. Rewrite sentences for coherence, remove redundancy and filler words.
3. Tone:
   - Academic text → formal tone.
   - Casual text → natural tone.
4. Length:
   - Short inputs (<100 words) → 1–2 sentences.
   - Medium (100–300 words) → 3–5 sentences.
   - Long text → 1 concise paragraph (max 120 words).
5. Objectivity: Only summarize what’s present, no added info.
6. If unclear, mention politely.
7. Clear, readable formatting; avoid bullets unless original has lists.

Text to summarize:

{text}

Produce the summary below:
"""

        # --- Grok generate using chat ---
        response = client.chat(messages=[{"role": "user", "content": prompt}])

        # Extract summary text
        summary_text = response["content"] if "content" in response else "No summary returned."

        st.markdown("### Summary Result")
        st.markdown(summary_text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
