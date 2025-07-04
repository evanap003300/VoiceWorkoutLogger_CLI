from transcription.voice_to_wav import record_audio
from transcription.speech_to_text import transcribe_audio

def main():
    print("Press Enter to start recording...")
    input()
    
    print("Recording... Press Enter to stop.")
    record_audio()
    
    print("\nTranscribing audio...")
    transcribe_audio()

if __name__ == "__main__":
    main()