import google.generativeai as genai 
import os   
from dotenv import load_dotenv



def ask_question(paragraph,Ques):
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API")
    genai.configure(api_key=API_KEY)
    summary = paragraph
    model = genai.GenerativeModel("gemini-1.5-flash") 
    question = Ques
    
    prompt = f"Answer from the Context only:\n{summary}\n\nQuestion: {question}"
    response = model.generate_content(prompt) 
    print(response.text)
    return (response.text)
    