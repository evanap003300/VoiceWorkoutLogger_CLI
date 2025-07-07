# Voice Transcription and Workout Parser (CLI MVP)

A Python-based CLI tool that combines voice transcription with workout information extraction. This MVP (Minimum Viable Product) allows you to record your workouts by speaking naturally, and the system will automatically transcribe your voice, extract workout information, and generate both JSON and Excel reports. This is the first phase of a larger full-stack project.

## Features

- **Voice Recording**:
  - Easy-to-use voice recording with Enter key control
  - High-quality audio recording (44.1kHz sample rate)
  - Saves audio as WAV file

- **Transcription**:
  - Fast and accurate transcription using the Whisper model
  - Outputs clean text format

- **Workout Information Extraction**:
  - Exercise detection from a comprehensive exercise database
  - Sets, reps, and weight tracking
  - Support for various weight units (lbs, kg, etc.)
  - Handles both numeric and word-form numbers
  - Natural language processing to understand workout descriptions

- **Data Export**:
  - Structured JSON output with proper exercise-to-set mapping
  - Chronologically ordered Excel spreadsheet generation with:
    - Exercise name
    - Set numbers
    - Reps per set
    - Weight used
  - Auto-formatted columns for readability

## Requirements

- Python 3.7 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - numpy (≥1.20.0)
  - sounddevice (≥0.4.5)
  - scipy (≥1.7.0)
  - faster-whisper (≥0.9.0)
  - spacy (≥3.7.2)
  - word2number (≥1.1)
  - pandas (≥2.0.0)
  - openpyxl (≥3.1.0)

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd voice-transcription-project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install spaCy's English language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Run the main program:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Press Enter to start recording
   - Speak your workout information naturally
   - Press Enter again to stop recording
   - Wait for processing to complete

3. The system will automatically:
   - Save the audio as `output.wav`
   - Transcribe to text in `data/text.txt`
   - Extract workout data to `data/workout_data.json`
   - Generate an Excel report in the `output` directory with chronologically ordered exercises and sets

### Example Voice Input

You can speak naturally about your workout. For example:
```
"I did bench press today, three sets. First set was 135 pounds for 10 reps, 
then 145 for 8, and finished with 155 for 6 reps."
```

## Project Structure

```
voice-transcription-project/
├── data/
│   ├── exercises.json     # Exercise database
│   ├── text.txt          # Transcribed text
│   └── workout_data.json # Processed workout data
├── exercises/
│   └── loading_exercises.py
├── export/
│   └── export_to_excel.py
├── output/
│   └── workout_log_*.xlsx # Generated Excel reports
├── voice_transcription/
│   ├── speech_to_text.py
│   └── voice_to_wav.py
├── word_parsing/
│   ├── build_json.py     # Processes and structures workout data
│   └── extract_workout_info.py # Extracts workout details using NLP
└── main.py               # Main program entry point
```

## Future Development Plans

This CLI version serves as an MVP for a larger full-stack application. Future development will focus on:

### 1. Web Application Development
- **Frontend (React)**:
  - Real-time recording interface
  - Workout history visualization
  - Exercise progress tracking
  - User authentication
  - Mobile-responsive design

- **Backend (FastAPI)**:
  - RESTful API endpoints
  - WebSocket support for real-time updates
  - User management
  - Workout data persistence
  - Exercise database management

### 2. Enhanced Features
- **Data Analysis**:
  - Progress tracking over time
  - Performance analytics
  - Workout recommendations
  - Goal setting and tracking

- **Natural Language Processing Improvements**:
  - Handle more casual speech patterns
  - Better context understanding
  - Support for:
    - Incomplete sentences
    - Corrections mid-speech
    - Multiple exercises in one sentence
    - Implicit exercise references

### 3. Mobile Application
- Native mobile apps for iOS and Android
- Offline support
- Push notifications
- Integration with health platforms

## Note

- Ensure your microphone is properly connected and selected as the default input device
- The workout parser supports various ways of expressing numbers and exercises
- For best results, speak clearly and include exercise name, sets, reps, and weights
- The system can handle natural speech but works best with complete information 