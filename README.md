# Voice Transcription and Workout Parser

A Python tool that combines voice transcription with workout information extraction. Record your workouts by speaking naturally, and the system will automatically transcribe your voice, extract workout information, and generate both JSON and Excel reports.

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

- **Data Export**:
  - Structured JSON output
  - Excel spreadsheet generation with:
    - Exercise name
    - Set numbers
    - Reps per set
    - Weight used
  - Auto-formatted columns for readability

## Requirements

- Python 3.7 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - numpy
  - sounddevice
  - scipy
  - faster-whisper
  - spacy
  - word2number
  - pandas
  - openpyxl

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install spaCy's English language model:
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
   - Generate an Excel report in the `output` directory

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
│   ├── build_json.py
│   └── extract_workout_info.py
└── main.py               # Main program entry point
```

## Future Plans

### 1. Frontend Development
- Create a React-based web interface
- Features planned:
  - Real-time recording status
  - Workout history visualization
  - Exercise progress tracking
  - User authentication
  - Mobile-responsive design

### 2. Backend Enhancement
- Convert to FastAPI backend
- Features planned:
  - RESTful API endpoints
  - WebSocket support for real-time updates
  - User management
  - Workout data persistence
  - Exercise database management

### 3. Natural Language Processing Improvements
- Enhanced parser capabilities:
  - Handle more casual speech patterns
  - Better context understanding
  - Support for:
    - Incomplete sentences
    - Corrections mid-speech
    - Multiple exercises in one sentence
    - Implicit exercise references
  - Improved error handling for:
    - Ambiguous statements
    - Missing information
    - Unit conversions
    - Exercise variations

## Note

- Ensure your microphone is properly connected and selected as the default input device
- The workout parser supports various ways of expressing numbers and exercises
- For best results, speak clearly and include exercise name, sets, reps, and weights
- The system can handle natural speech but works best with complete information 