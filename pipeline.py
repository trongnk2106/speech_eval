from gemini_speech_eval import EvaluateSpeech
from extract_conversation import S2TSumary

def pipeline(audio_file, api_key=""):
    # Extract conversation from audio file
    transcription, summary_conv, formatted_conversation = S2TSumary(apikey=api_key).run(audio_file)
    # Evaluate the conversation
    scores = EvaluateSpeech(apikey=api_key).run(transcription)
 
    return transcription, summary_conv, scores, formatted_conversation



# transcription, summary_conv, scores = pipeline("test.wav")
