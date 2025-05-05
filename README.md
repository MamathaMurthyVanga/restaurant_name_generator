# 🍽️ Restaurant Name & Menu Generator

This is a fun and creative web app that generates a fancy restaurant name and suggests menu items based on the selected cuisine. The app uses **LLaMA 3 (via Groq API)** and **LangChain** for AI-powered content generation, and **Streamlit** for the web interface.



## Features

- Choose from popular cuisines (e.g., Indian, Italian, Mexican, etc.)
- Get a fancy AI-generated restaurant name
- See a list of menu items tailored to the cuisine
- Fast, responsive, and runs entirely in your browser (via Streamlit)



## Tech Stack

- [LangChain](https://www.langchain.com/)
- [Groq](https://console.groq.com/) (LLaMA 3 model)
- [Streamlit](https://streamlit.io/)
- Python 3.9+





##  Setup Instructions

 1. Clone the Repo

```bash
git clone https://github.com/your-username/restaurant-name-generator.git
cd restaurant-name-generator
```

2. Install Requirements
```bash
pip install -r requirements.txt 
```



3. Add Your Groq API Key
Create a file called secret_key.py:
```bash
groq_api_key = "gsk_your_actual_groq_key_here"
```
Do not share or upload this file publicly.


4. Run the App
```bash
streamlit run main.py
```




