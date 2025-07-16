import nltk
from nltk.chat.util import Chat, reflections

# ---- Define chatbot rules (patterns & responses) ----
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot created by CodTech intern!"]
    ],
    [
        r"how are you?",
        ["I'm doing great! How can I assist you today?"]
    ],
    [
        r"(.*) your name?",
        ["I am a chatbot built using NLTK."]
    ],
    [
        r"what is python?",
        ["Python is a programming language. It is used for web development, data analysis, AI, and more."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Thanks for chatting. Bye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

# ---- Initialize chatbot ----
chatbot = Chat(pairs, reflections)

# ---- Start conversation ----
print("Welcome to the CodTech Chatbot! (type 'bye' to exit)")
chatbot.converse()
