<h1 align="center"> HELPER</h1>

This application allows users to input stories, articles, or any custom text, and then ask questions about the content. The system uses a text summarizer to extract key points and leverages an LLM-powered Q&A module to provide accurate and contextual answers.

**Live Demo:** No live demo Yet 😔

---

<img width="1915" height="1031" alt="image" src="https://github.com/user-attachments/assets/973d8986-2128-40d7-84b2-54f586682a4a" />

---
### Features
-  Input any text (stories, paragraphs, articles, etc.)
-  Summarizes the input text for better context understanding
-  Ask questions related to the provided text
-  our application generates answers based on summarized content

### Tech Stack Used:
 - Flask – Web framework
 - speech_recognition – For converting speech to text
 - Google Generative AI (Gemini) – For LLM-based question answering
 - dotenv – For securely handling API keys
 - streamlit - for trial run 

### Workflow
 - User speaks a story → Captured via microphone
 -  Text is stored and summarized
 - User asks a question → Passed with summary to LLM
 - LLM generates contextual answers
 - ur answer

### Acknowledgments
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) for speech-to-text
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Google Generative AI](https://ai.google.dev/) for the LLM-based Q&A

```
 [helper]/
  │── .gitignore                # Git ignore file
  ├── frontend.py               # Flask frontend integration
  ├── main.py                   # Trial to run the program using streamlit
  ├── output.txt                # Stores user queries and responses (optional)
  ├── qanda.py                  # Q&A module with Google Generative AI (Gemini)
  ├── requirements.txt          # Python dependencies
  ├── speechToText.py           # Speech recognition and text saving
  ├── summerizer.py             # Text summarization logic
  └──  README.md                # Project documentation
```


