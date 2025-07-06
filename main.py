from voice_transcription.voice_to_wav import record_audio
from voice_transcription.speech_to_text import transcribe_audio
from export.export_to_excel import export_workout_to_excel
from word_parsing.build_json import build_json

def main():
    print("Press Enter to start recording...")
    input()
    
    print("Recording... Press Enter to stop.")
    record_audio()
    
    print("\nTranscribing audio...")
    transcribe_audio()

    print("\nBuilding JSON...")
    build_json()

    print("\nExporting to Excel...")
    export_workout_to_excel()

    print("\nDone!")

if __name__ == "__main__":
    main()