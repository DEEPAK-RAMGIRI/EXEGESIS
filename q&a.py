import google.generativeai as genai 
import os 
from speechToText import ouput_text , Record_Question   
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API")
genai.configure(api_key=API_KEY)
summary = ''' '''
ouput_text(summary)
model = genai.GenerativeModel("gemini-1.5-flash") 
question =  Record_Question()
ouput_text(question)
prompt = f"Answer from the Context only:\n{summary}\n\nQuestion: {question}"
response = model.generate_content(prompt) 
print(response.text)