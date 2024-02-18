import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
from textblob import TextBlob
from neuralintents import BasicAssistant

class VoiceAssistantGUI:
    def _init_(self, master):
        self.master = master
        master.title("Voice-Based Mental Health Journaling App")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        self.listen_label = tk.Label(master, text="Listening...", font=("Helvetica", 16))
        self.listen_label.pack(pady=10)

        self.record_button = tk.Button(master, text="Record", command=self.record_audio)
        self.record_button.pack(pady=10)

    def record_audio(self):
        # Change the listening label
        self.listen_label.config(text="Recording...", fg="red")

        # Initialize SpeechRecognition
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            try:
                # Listen to user's input
                audio = recognizer.listen(source, timeout=10)

                # Convert audio to text
                user_input = recognizer.recognize_google(audio)
                self.text_area.insert(tk.END, f"You: {user_input}\n")

                # Analyze sentiment using TextBlob
                blob = TextBlob(user_input)
                sentiment = blob.sentiment.polarity

                # Perform actions based on user input
                response = assistant.process_input("Hello How are you")
                self.text_area.insert(tk.END, f"Assistant: {response}\n")

                # Update the listening label
                self.listen_label.config(text="Listening...", fg="black")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error with the request: {e}")


# Create a Neural Assistant
assistant = BasicAssistant(r"intents.json", model_name='text_response_model')
assistant.fit_model()

# Create and run the GUI
root = tk.Tk()
app = VoiceAssistantGUI(root)
root.mainloop()
