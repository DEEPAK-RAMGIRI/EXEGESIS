<h1 align="center"> EXEGESIS</h1>

This application allows users to input stories, articles, or any custom text, and then ask questions about the content. The system uses a text summarizer to extract key points and leverages an LLM-powered Q&A module to provide accurate and contextual answers.

**Live Demo:** No live demo Yet 😔

---

![WhatsApp Image 2025-09-18 at 10 19 55_fd17aa30](https://github.com/user-attachments/assets/9d37a5c7-42fd-4426-9ff0-9d3e9818cae9)

---
### Features
-  Input any text (stories, paragraphs, articles, etc.)
-  speech_recognition – Convert speech to text
-  Google Generative AI (Gemini) – LLM-based question answering
-  Summarizes the input text for better context understanding
-  Ask questions related to the provided text
-  our application generates answers based on summarized content

### Tech Stack Used:
 - Flask – Web framework
 - speech_recognition – For converting speech to text
 - Google Generative AI (Gemini) – For LLM-based question answering
 - dotenv – For securely handling API keys
 - streamlit - for trial run
 - BartTokenizer- For  tokenizing and giving ids
 - BartForConditionalGeneration- For summarizing the given converted tokens

### Workflow
 - User gives a story or article 
 -  Text is stored 
 -  That stored text is summerized using the BART Model
 - User asks a question → Passed with summary to LLM (or) Type the question
 - LLM generates contextual answers from the summerized text
 - ur answer

### Docker Usage
```
docker pull deepakramgiri/exegesis
```
get ur [API HERE:](https://aistudio.google.com/apikey?_gl=1*9jchcg*_ga*OTMyMDY4NzA0LjE3NTczMjM2ODA.*_ga_P1DBVKWT6V*czE3NTgyNTgwMTYkbzIkZzAkdDE3NTgyNTgwMTYkajYwJGwwJGgxMjkxNTI0ODg5)
```
docker run -p 8000:5000 -e GOOGLE_API_KEY="YOUR_API_KEY" -e USE_MIC=0 deepakramgiri/exegesis.
```
Access the app at: http://localhost:8000

### Acknowledgments
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) for speech-to-text
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Google Generative AI](https://ai.google.dev/) for the LLM-based Q&A
- [Text Summarization with BART Model](https://medium.com/@sandyeep70/demystifying-text-summarization-with-deep-learning-ce08d99eda97) For the summerizeing the text
```


 EXEGESIS/
  │──.dockerignore 
  │── .gitignore                # Git ignore file
  │── Dockerfile
  │── favicon.ico
  ├── frontend.py               # Flask frontend integration
  ├── main.py                   # Trial to run the program using streamlit
  ├── output.txt                # Stores user queries and responses (optional)
  ├── qanda.py                  # Q&A module with Google Generative AI (Gemini)
  ├── requirements.txt          # Python dependencies
  ├── speechToText.py           # Speech recognition and text saving
  ├── summerizer.py             # Text summarization logic
  └──  README.md                # Project documentation
```


