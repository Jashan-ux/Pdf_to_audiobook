import fitz 
import pyttsx3

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc :
        text +=page.get_text("text") + "\n"
    return text

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} - {voice.id}")


    engine.setProperty('voice', voices[1].id) 


    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = "my.pdf"
    text = extract_text_from_pdf(pdf_path)
    text_to_speech(text)



