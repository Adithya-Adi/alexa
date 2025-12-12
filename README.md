# Alexa Voice Assistant

A local voice assistant that uses wake word detection ("Alexa"), speech recognition, and OpenAI's GPT-4 to respond to voice commands.

## Features

- 🎤 Wake word detection using "Alexa"
- 🗣️ Speech-to-text using Google Speech Recognition
- 🤖 AI-powered responses via OpenAI GPT-4
- 🔊 Text-to-speech for voice responses
- 💬 Natural conversation flow

## Prerequisites

Before installing, ensure you have the following:

- **Python 3.9 or higher**
- **uv** package manager ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))
- **Microphone** and **speakers** connected to your system
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### System Dependencies

#### macOS
```bash
brew install portaudio
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install portaudio19-dev python3-pyaudio
```

#### Windows
PyAudio should install automatically with uv, but if you encounter issues:
- Download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Install it manually: `pip install <downloaded-file>.whl`

## Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd /Users/adithya/Xperiments/alexa
   ```

2. **Install dependencies using uv**:
   ```bash
   uv sync
   ```

   This will create a virtual environment and install all required packages.

## Configuration

1. **Add your OpenAI API Key**:
   
   Open `main.py` and replace the empty API key on line 10:
   ```python
   client = OpenAI(api_key="your-api-key-here")
   ```

   Replace `"your-api-key-here"` with your actual OpenAI API key.

## Running the Application

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate  # Windows
   ```

2. **Run the voice assistant**:
   ```bash
   uv run main.py
   ```

   Or if you've activated the virtual environment:
   ```bash
   python main.py
   ```

3. **Using the assistant**:
   - Wait for the message: `🤖 Alexa ONLINE. Say 'Alexa'...`
   - Say **"Alexa"** to wake the assistant
   - Wait for the response: **"Yes?"**
   - Ask your question or give a command
   - The assistant will respond using OpenAI GPT-4
   - Say **"stop"** to exit the program

## Example Usage

```
🤖 Alexa ONLINE. Say 'Alexa'...

⚠️ WAKE WORD DETECTED! (0.87)
  🗣️ SYSTEM: Yes?
  👂 LISTENING...
  ✅ YOU SAID: 'What's the weather like today?'
  Thinking...
  🗣️ SYSTEM: I don't have real-time weather data, but you can check a weather app or website for current conditions.

🤖 READY AGAIN...
```

## Troubleshooting

### Microphone Issues
- **macOS**: Grant microphone permissions in System Preferences → Security & Privacy → Privacy → Microphone
- **Linux**: Check your microphone is working with `arecord -l`
- **All platforms**: Ensure your microphone is set as the default input device

### PyAudio Installation Errors
If you encounter errors installing PyAudio:
- Make sure you've installed the system dependencies (portaudio)
- Try installing PyAudio separately: `uv pip install pyaudio`

### Wake Word Not Detecting
- Speak clearly and at a moderate volume
- Ensure there's minimal background noise
- Try adjusting the detection threshold in `main.py` (line 78, currently set to `0.5`)

### OpenAI API Errors
- Verify your API key is correct
- Check you have credits in your OpenAI account
- Ensure you have internet connectivity

## Project Structure

```
alexa/
├── main.py              # Main application file
├── pyproject.toml       # Project dependencies
├── uv.lock             # Locked dependency versions
├── README.md           # This file
└── .venv/              # Virtual environment (created after installation)
```

## Dependencies

- `pyaudio` - Audio I/O
- `numpy` - Numerical operations
- `openwakeword` - Wake word detection
- `speechrecognition` - Speech-to-text
- `pyttsx3` - Text-to-speech
- `openai` - OpenAI API client
- `onnxruntime` - ML model runtime

## License

This project is for educational and experimental purposes.
