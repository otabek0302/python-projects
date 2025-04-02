# Jarvis Voice Assistant

A powerful voice-controlled assistant that can help you with various tasks using natural language commands.

## Features

### Basic Commands
- Wake word: "hey peter"
- Basic information queries (name, age, job)
- Time and date information
- Weather information (current location and specific cities)
- Jokes and entertainment

### Web Navigation
- Open various websites (YouTube, Google, Facebook, Instagram)
- Web search functionality
- Wikipedia search and article reading

### Music Control
- Search for songs on YouTube
- Play songs on YouTube
- Direct YouTube search results

### Information Retrieval
- Wikipedia article summaries
- Weather updates
- Time and date information

## Requirements

- Python 3.6 or higher
- Microphone
- Internet connection
- Web browser

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Voice-Asistent
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the assistant:
```bash
python jarvis.py
```

2. Wait for the "🎙️ Listening..." prompt

3. Available Commands:

### Basic Interaction
- "hey peter" - Wake the assistant
- "what is your name" - Get assistant's name
- "what is your age" - Get assistant's age
- "what is your job" - Get assistant's role
- "what is the time" - Get current time
- "exit" - Close the assistant

### Weather Information
- "what is the weather" - Get weather for current location
- "what is the weather in [city]" - Get weather for specific city

### Web Navigation
- "open youtube" - Open YouTube
- "open google" - Open Google
- "open facebook" - Open Facebook
- "open instagram" - Open Instagram
- "search [query]" - Search on Google

### Wikipedia Commands
- "tell me about [topic]" - Get Wikipedia summary
- "what is [topic]" - Get Wikipedia summary
- "search on wikipedia [topic]" - Search Wikipedia

### Music Commands
- "play [song name]" - Search and play song on YouTube
- "search song [song name]" - Search for song on YouTube

## Notes

- The assistant requires an active internet connection for most features
- Voice recognition accuracy depends on microphone quality and ambient noise
- Wikipedia summaries are limited to 2 sentences by default
- YouTube playback opens search results (direct playback requires YouTube API integration)

## Troubleshooting

1. If the assistant doesn't respond:
   - Check your microphone connection
   - Ensure you're speaking clearly
   - Verify internet connection

2. If voice recognition fails:
   - Reduce background noise
   - Speak closer to the microphone
   - Check internet connection

3. If weather information fails:
   - Verify internet connection
   - Check if the city name is correct

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
