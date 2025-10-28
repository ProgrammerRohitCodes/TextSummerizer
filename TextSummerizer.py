import google.generativeai as genai
import streamlit as st

st.title("Text Summarizer")
st.markdown("Enter your text below and get a clean, professional summary.")

text = st.text_area("Enter your text here:", height=250)

GOOGLE_API_KEY = "" 
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = "gemini-1.5-flash-latest"
gen_model = genai.GenerativeModel(MODEL_NAME)

summarize = st.button("Summarize")

if summarize:
    try:
        if not text.strip():
            st.error("Please enter some text first.")
            st.stop()

        prompt = f"""
You are a professional text summarizer. Your task is to read the given text carefully
and produce a clear, concise, and meaningful summary in 3–5 sentences.

Guidelines:
1. Focus only on the main ideas or arguments.
2. Skip unnecessary examples, adjectives, and repetition.
3. Keep the tone of the original text (formal/informal as it appears).
4. If the text is too short, provide a single-sentence summary.
5. If the text seems unclear or incomplete, mention that politely in the summary.

Text to summarize:
{text}

Now provide the final summary below:
"""

        response = gen_model.generate_content([prompt])
        st.markdown("### Summary Result")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
