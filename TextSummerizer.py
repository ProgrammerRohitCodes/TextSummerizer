import streamlit as st
import requests
import json

# --- App Title ---
st.title("Text Summarizer (Gemini 2.5 Flash-Lite)")
st.markdown("Enter your text below and get a structured summary powered by Google Gemini.")

# --- Input Section ---
text = st.text_area("Enter your text here:", height=250)

# --- API Config ---
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"

if not GEMINI_API_KEY:
    st.error("Gemini API key is missing!")
    st.stop()

# --- Button ---
if st.button("Summarize"):
    if not text.strip():
        st.error("Please enter some text first.")
        st.stop()

    # --- Create summarization prompt ---
    summarization_prompt = f"""
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
For short inputs (<100 words), write 1–2 sentence summary.
For medium inputs (100–300 words), write 3–5 sentences.
For long texts, aim for 1 concise paragraph (max 120 words).
5. Objectivity: Do not add new information or personal opinions — only summarize what’s present.
6. If the text seems vague, mention that politely in your summary.

Here is the text to summarize:
{text}
"""

    try:
        # --- Prepare API request using correct Gemini v1beta structure ---
        payload = {
            "input": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": summarization_prompt}
                    ]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        # --- Send request to Gemini API ---
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            data=json.dumps(payload),
            timeout=60
        )
        response.raise_for_status()

        # --- Parse API response ---
        result = response.json()
        summary_text = result["candidates"][0]["content"][0]["text"]

        # --- Display summary ---
        st.markdown("### Summary Result")
        st.write(summary_text)

    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
