# AIChat – Anime Voice Chatbot

AIChat is a Python project that converts your speech to text, sends it to OpenAI’s GPT model,  
and reads the AI response out loud. The chatbot speaks like an anime character  
(currently Kakashi from Naruto, because I’m a fan) for an interactive voice experience.

Please note that on **Windows and Linux**, some steps or requirements may differ,  
although the overall setup is similar. An **OpenAI account is required** to use this project.  
Search for “OpenAI API” on Google to create an account and obtain your API key.

⚠️ **Important:** Make sure **not to commit your `.env` file** so that your API key remains private.

---

# Anime GPT

![Anime GPT Thumbnail](![AnimeGPT](https://github.com/user-attachments/assets/7966dc0f-4472-41e7-9bb5-104204d7b5d6)
)

---

## Features

- Speech-to-text using `speech_recognition`
- AI responses powered by OpenAI (GPT-4o-mini)
- Text-to-speech using `pyttsx3`
- Anime-style character responses (Kakashi)
- macOS system voice support
- Environment variables for secure API key handling

---

## Requirements

- Python 3.10+
- macOS (recommended for best TTS voices)
- Microphone access enabled
- OpenAI API key

---

## Resources & References

- [pyttsx3 documentation](https://pypi.org/project/pyttsx3/)
- [How to Convert Speech to Text in Python – HackerNoon](https://hackernoon.com/how-to-convert-speech-to-text-in-python-q0263tzp)
- [Python: Convert Speech to Text and Text to Speech – GeeksforGeeks](https://www.geeksforgeeks.org/python/python-convert-speech-to-text-and-text-to-speech/)
- Various YouTube tutorials on voice assistants and AI chatbots

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RavshanSean/AIchat.git
cd AIchat
