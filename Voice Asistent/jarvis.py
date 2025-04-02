import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import python_weather
import geocoder
import asyncio
import time

# Get location from IP
g = geocoder.ip('me')

# Speak text
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

# Listen to microphone input
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("🧠 Recognizing...")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that")
            return None
        except sr.RequestError:
            print("Could not request results; check your internet connection")
            return None

# Async weather fetcher
async def get_weather(city):
    try:
        async with python_weather.Client() as client:
            weather = await client.get(city)
            return f"{weather.current.temperature}°C and {weather.current.sky_text}"
    except:
        return "Sorry, I couldn't fetch the weather right now."

# Wikipedia functions
def get_wikipedia_summary(query, sentences=2):
    try:
        # Search Wikipedia
        search_results = wikipedia.search(query)
        if not search_results:
            return "Sorry, I couldn't find any information about that."
        
        # Get the first result
        page = wikipedia.page(search_results[4])
        
        # Get summary
        summary = wikipedia.summary(search_results[4], sentences=sentences)
        
        # Return both summary and URL
        return {
            'summary': summary,
            'url': page.url
        }
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages
        options = e.options[:5]  # Get first 5 options
        return f"This topic has multiple meanings. Did you mean: {', '.join(options)}?"
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# Music functions
def search_song_on_youtube(song_name):
    speechtx(f"Searching for {song_name} on YouTube")
    query = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def play_song_directly(song_name):
    speechtx(f"Playing {song_name} on YouTube")
    query = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    time.sleep(2)  # Wait for the page to load
    # Note: Direct play functionality would require YouTube API integration

# Main loop
if __name__ == '__main__':
    while True:
        text = sptext()
        if text:
            text = text.lower()

            if text == "hey peter":
                speechtx("Yes, I'm listening")

            elif text == "what is your name":
                speechtx("I'm Jarves")

            elif text == "what is your age":
                speechtx("I'm 20 years old")

            elif text == "what is your job":
                speechtx("I'm a voice assistant")

            elif text == "what is the time":
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speechtx(f"The current time is {current_time}")

            elif text == "what is the weather":
                weather = asyncio.run(get_weather(g.city))
                speechtx(f"The weather in {g.city} is {weather}")

            elif "what is the weather in" in text:
                city = text.replace("what is the weather in", "").strip()
                if city:
                    weather = asyncio.run(get_weather(city))
                    speechtx(f"The weather in {city} is {weather}")
                else:
                    speechtx("Please tell me the city name.")

            elif text == "what is the news":
                joke = pyjokes.get_joke()
                speechtx(f"Here's a joke instead: {joke}")

            elif text == "what is the stock market":
                joke = pyjokes.get_joke()
                speechtx(f"The stock market is full of surprises. Here's a joke instead: {joke}")

            elif "search" in text:
                query = text.replace("search", "").strip()
                if query:
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                    speechtx(f"Searching for {query}")
                else:
                    speechtx("What would you like me to search for?")

            # Wikipedia commands
            elif "tell me about" in text:
                query = text.replace("tell me about", "").strip()
                if query:
                    result = get_wikipedia_summary(query)
                    if isinstance(result, dict):
                        speechtx(result['summary'])
                        speechtx("Would you like me to open the full article?")
                        response = sptext()
                        if response and "yes" in response.lower():
                            webbrowser.open(result['url'])
                    else:
                        speechtx(result)
                else:
                    speechtx("What would you like to know about?")

            elif "what is" in text:
                query = text.replace("what is", "").strip()
                if query:
                    result = get_wikipedia_summary(query)
                    if isinstance(result, dict):
                        speechtx(result['summary'])
                        speechtx("Would you like me to open the full article?")
                        response = sptext()
                        if response and "yes" in response.lower():
                            webbrowser.open(result['url'])
                    else:
                        speechtx(result)
                else:
                    speechtx("What would you like to know about?")

            elif "search on wikipedia" in text:
                query = text.replace("search on wikipedia", "").strip()
                if query:
                    result = get_wikipedia_summary(query)
                    if isinstance(result, dict):
                        speechtx(result['summary'])
                        speechtx("Would you like me to open the full article?")
                        response = sptext()
                        if response and "yes" in response.lower():
                            webbrowser.open(result['url'])
                    else:
                        speechtx(result)
                else:
                    speechtx("What would you like me to search for on Wikipedia?")

            # Music commands
            elif "play" in text:
                song_name = text.replace("play", "").strip()
                if song_name:
                    play_song_directly(song_name)
                else:
                    speechtx("Please tell me which song to play")

            elif "search song" in text:
                song_name = text.replace("search song", "").strip()
                if song_name:
                    search_song_on_youtube(song_name)
                else:
                    speechtx("Please tell me which song to search for")

            elif text == "open youtube":
                webbrowser.open("https://www.youtube.com")

            elif text == "open google":
                webbrowser.open("https://www.google.com")

            elif text == "open facebook":
                webbrowser.open("https://www.facebook.com")

            elif text == "open instagram":
                webbrowser.open("https://www.instagram.com")

            elif text == "exit":
                speechtx("Goodbye!")
                break