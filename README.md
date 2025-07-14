
# 🤖 AI Chatbot with NLP

A simple rule-based and intent-classifying chatbot built using **Python**, **NLTK**, and **Scikit-learn** as part of **CodTech Internship Task-3**.

## 📌 Features
- Built using **Natural Language Processing (NLP)** techniques
- Uses **NLTK** for tokenization and text processing
- Uses **Scikit-learn** for intent classification
- Can understand greetings, questions about Python, goodbyes, and more
- Fully customizable with more intents and responses

## 📁 Files Included
- `chatbot.py` – Main Python script (smart chatbot)
- `README.md` – Project documentation

## 🛠️ Technologies Used
- Python 3.x
- NLTK (Natural Language Toolkit)
- Scikit-learn (for intent classification)

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install nltk scikit-learn
```

### 2. (One-time) Download NLTK data
```python
import nltk
nltk.download('punkt')
```

### 3. Run the chatbot
```bash
python chatbot.py
```

## 💬 Example Interaction
```
You: hi
Bot: Hello!

You: what is python
Bot: Python is a powerful programming language.

You: thanks
Bot: You're welcome!

You: bye
Bot: Goodbye!
```

## 📌 How It Works
- The user input is converted to numerical vectors using `CountVectorizer`
- The trained model (`MultinomialNB`) classifies the input into an intent
- A response is selected from predefined answers based on the predicted intent

## 🧠 Future Improvements
- Add more intents and responses
- Integrate `spaCy` for advanced NLP
- Build a GUI using Tkinter or a web app with Flask

## 📃 License
This project is for educational/demo purposes under the CodTech Internship.
