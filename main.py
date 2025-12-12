import pyaudio
import numpy as np
import openwakeword
from openwakeword.model import Model
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
import threading

client = OpenAI(api_key="") 

def speak(text, wait=True):
    def _speak_target():
        engine = pyttsx3.init()
        print(f"  🗣️ SYSTEM: {text}")
        engine.say(text)
        engine.runAndWait()

    if wait:
        _speak_target()
    else:
        t = threading.Thread(target=_speak_target)
        t.start()

def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Keep answers under 2 sentences."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  ❌ OpenAI Error: {e}")
        return "I couldn't reach the server."

print("Loading Wake Word Model...")
model = Model(wakeword_models=["alexa"])

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1280 
audio = pyaudio.PyAudio()

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n  👂 LISTENING...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        try:
            audio_data = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            print("  Thinking...")
            text = recognizer.recognize_google(audio_data)
            print(f"  ✅ YOU SAID: '{text}'")
            return text
        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass
        except sr.RequestError:
            speak("I am offline.")
        return None

mic_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("\n🤖 Alexa ONLINE. Say 'Alexa'...")

try:
    while True:
        data = np.frombuffer(mic_stream.read(CHUNK), dtype=np.int16)
        prediction = model.predict(data)
        
        for md in model.prediction_buffer.keys():
            score = model.prediction_buffer[md][-1]
            if score > 0.5:
                print(f"\n⚠️ WAKE WORD DETECTED! ({score:.2f})")
                
                mic_stream.stop_stream()
                mic_stream.close()
                
                speak("Yes?") 
                
                user_text = listen_for_command()
                
                if user_text:
                    if "stop" in user_text.lower():
                        speak("Goodbye.")
                        exit()
                    
                    ai_response = ask_openai(user_text)
                    speak(ai_response)

                print("\n🤖 READY AGAIN...")
                mic_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
                model.reset()

except KeyboardInterrupt:
    mic_stream.stop_stream()
    mic_stream.close()
    audio.terminate()