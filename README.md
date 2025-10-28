# Text Summarizer 

A simple Streamlit app that generates concise summaries of any text using Google’s Gemini model.  
Just paste your text, hit **Summarize**, and watch the AI do the trimming.

---

## Features
- Generates short, meaningful summaries in seconds  
- Understands both formal and casual text tones  
- Built with **Python** and **Streamlit**  
- Uses Google’s **Gemini 1.5 Flash** model for fast responses  

---

## Setup & Usage

### 1. Clone this repo
```bash
git clone https://github.com/yourusername/Text-Summarizer.git
cd Text-Summarizer
```

### 2. Install dependencies
```bash
pip install streamlit google-generativeai
```

### 3. Add your Gemini API key  
Open the code file and replace this line:
```python
GOOGLE_API_KEY = ""
```
with your own key:
```python
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
```

*(You can get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey))*

### 4. Run the app
```bash
streamlit run app.py
```

---

## Example Use
Paste any paragraph, article, or essay —  
and the app will return a crisp 3–5 sentence summary focused on the main ideas.

---

## Tech Stack
- **Python**  
- **Streamlit**  
- **Google Gemini API**

---

## License
This project is open-source. You can use or modify it for learning and non-commercial projects.
