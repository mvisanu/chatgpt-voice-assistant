import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech input
def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print("You said:", voice_data)
            return voice_data
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that. Please try again.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")

# Define a function to set reminders
def set_reminder():
    speak("What do you want me to remind you about?")
    reminder = get_audio()
    speak("When should I remind you?")
    time = get_audio()
    # Convert time string to datetime object
    time_obj = datetime.datetime.strptime(time, '%H:%M')
    # Calculate time difference in seconds
    time_diff = (time_obj - datetime.datetime.now()).total_seconds()
    # Schedule reminder using Python's built-in 'time' module
    time.sleep(time_diff)
    speak("Reminder: " + reminder)

# Define a function to create to-do lists
def create_todo_list():
    speak("What should be added to the to-do list?")
    task = get_audio()
    with open("todo.txt", "a") as f:
        f.write("- " + task + "\n")
    speak("Task added to to-do list.")

# Define a function to search the web
def search_web():
    speak("What do you want me to search for?")
    search_query = get_audio()
    url = 'https://www.google.com/search?q=' + search_query
    webbrowser.get().open(url)
    speak("Here are the search results for " + search_query)

# Start the voice assistant
speak("Hi, how can I help you today?")

while True:
    voice_data = get_audio().lower()
    if "set reminder" in voice_data:
        set_reminder()
    elif "create to-do list" in voice_data:
        create_todo_list()
    elif "search web" in voice_data:
        search_web()
    elif "exit" in voice_data or "bye" in voice_data:
        speak("Goodbye!")
        break
