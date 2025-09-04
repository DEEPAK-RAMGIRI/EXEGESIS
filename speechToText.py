import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def Record_Question():
    while True:
        try:
            with sr.Microphone() as source:
                print("Talk something i'am listening")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                listen =  r.recognize_google(audio)
                print(listen)
                return listen
        except sr.UnknownValueError:
            print("SORRY I could not understand audio")
        except sr.RequestError as e:
            print("ERROR FROM MY SIDE SORRY🥲; {0}".format(e))
            
def ouput_text(text):
    file = open("output.txt","a")
    file.write(text)
    file.write('\n')
    file.close()
    return
    
if __name__ == "__main__":
    text = Record_Question()
    ouput_text(text)
    
    