SENTIMENT ANALYSIS

🎯 Sentiment Pulse

**Sentiment Pulse** is a lightweight web app that analyzes customer reviews and detects sentiment as **Positive**, **Negative**, or **Neutral** — complete with mood-matching emojis and smooth UI animations.

Built using:
🐍 Python (Flask)
🧠 NLTK (Naive Bayes)
🎨 Tailwind CSS
⚡ JavaScript (frontend animation)

🚀 Features

📝 Input customer reviews directly
🤖 NLP-based sentiment classification
😄 Emoji + description feedback (Positive Vibes / Negative Experience / Neutral Mood)
💫 Bounce animation for result display
🔥 Responsive and minimalist UI


🛠️ How to Run Locally

1. Clone the repo
   bash
   git clone https://github.com/YOUR_USERNAME/sentiment-pulse.git
   cd sentiment-pulse

2. Install dependencies

bash
pip install flask nltk

3. Install dependencies

bash
pip install flask nltk
Download NLTK tokenizer
(automatically handled in code, but to be safe)

python
import nltk
nltk.download('punkt')
Start the Flask app

bash
python app.py
Visit in browser

cpp
http://127.0.0.1:5000

📁 Project Structure
sentiment-pulse/
├── app.py                  # Flask server
├── static/
│   └── app.js              # Frontend logic + animation
└── templates/
    └── index.html          # UI (Tailwind + HTML)

📦Example Input & Output
Input:
"I loved the fast delivery and great packaging!"

Output:

Emoji: 😄

Sentiment: POS

Description: Positive Vibes

✅ License
MIT © 2025 Harshitha

🌟 Contribute
Want to improve accuracy or add features like charts or multilingual support? Fork the repo and raise a PR!









