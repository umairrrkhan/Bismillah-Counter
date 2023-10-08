import speech_recognition as sr

def count_bismillah_occurrences(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio
        
    try:
        transcribed_text = recognizer.recognize_google(audio_data)  # Use Google's speech recognition
        # Convert the transcribed text to lowercase for case-insensitive counting
        transcribed_text = transcribed_text.lower()
        count = transcribed_text.count("bismillah")  # Count occurrences of "bismillah"
        return count
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return 0  # Return 0 if no "Bismillah" is found

# Example usage:
audio_file = "file.wav"
occurrences = count_bismillah_occurrences(audio_file)
print(f"'Bismillah' appears {occurrences} times in the audio.")
