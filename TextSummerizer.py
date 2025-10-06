import streamlit as st
import requests

# --- App Title ---
st.title("Text Summarizer")
st.markdown("Enter your text below and get a clean, structured summary powered by AI.")

# --- Input Section ---
text = st.text_area("Enter your text here:", height=250)

# --- API Config ---
GROK_API_KEY = st.secrets.get("GROK_API_KEY")
GROK_API_URL = "https://api.x.ai/v1/chat/completions"

if not GROK_API_KEY:
    st.error("Grok API key is missing!")
    st.stop()

# --- Button ---
if st.button("Summarize"):
    if not text.strip():
        st.error("Please enter some text first.")
        st.stop()

    # --- Create summarization prompt ---
    prompt = f"""
You are an expert text summarizer with deep understanding of context, logic, and clarity.
Your job is to read the given text carefully and generate a summary that captures its key points
in a professional, human-like tone.

Follow these strict rules:

1. Main Objective: Capture the core ideas, reasoning, and insights — not every line.
2. Clarity: Rewrite sentences for coherence, remove redundancy and filler words.
3. Tone:
If the input text is academic, summarize in a formal tone.
If it’s casual or conversational, keep it natural and easy to read.
4. Length:
For short inputs (<100 words), write a 1–2 sentence summary.
For medium inputs (100–300 words), write 3–5 sentences.
For long texts, aim for 1 concise paragraph (max 120 words).
5. Objectivity: Do not add new information or personal opinions — only summarize what’s present.
6. If the text seems vague, mention that politely in your summary.

Here is the text to summarize:
{text}
"""

    try:
        # --- Prepare API request ---
        headers = {
            "Authorization": f"Bearer {GROK_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "grok-3", 
            "messages": [
                {"role": "system", "content": "You are a helpful AI text summarizer."},
                {"role": "user", "content": prompt}
            ]
        }

        # --- Send request to Grok API ---
        response = requests.post(GROK_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        # --- Parse API response ---
        result = response.json()
        summary_text = result["choices"][0]["message"]["content"]

        # --- Display summary ---
        st.markdown("### Summary Result")
        st.write(summary_text)

    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
