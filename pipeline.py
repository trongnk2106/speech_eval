from gemini_speech_eval import EvaluateSpeech
from extract_conversation import S2TSumary
from const import cost_api
import os
def pipeline(audio_file, api_key=""):
    # Extract conversation from audio file
    transcription, summary_conv, formatted_conversation, token_usage, token_usage_summary = S2TSumary(apikey=api_key).run(audio_file)
    # Evaluate the conversation
    scores, list_token_usage = EvaluateSpeech(apikey=api_key).run(transcription)
    
    cost = { "speech to text": {
            "number of input token": token_usage.prompt_token_count,
            "number of output token": token_usage.candidates_token_count,
            "number of cached token" : token_usage.cached_content_token_count,
            "cost" : token_usage.prompt_token_count * cost_api['input_token'] + token_usage.candidates_token_count * cost_api['output_token']  + token_usage.cached_content_token_count * cost_api['cached_token']
        }, 
            "text summary": {
            "number of input token": token_usage_summary.prompt_token_count,
            "number of output token": token_usage_summary.candidates_token_count,
            "number of cached token" : token_usage_summary.cached_content_token_count,
            "cost" : token_usage_summary.prompt_token_count * cost_api['input_token'] + token_usage_summary.candidates_token_count * cost_api['output_token'] + token_usage_summary.cached_content_token_count * cost_api['cached_token']
            }                                                                                                                                 
    }  
    temp = {'text evaluate': {
        "number of input token": 0,
        "number of output token": 0,
        "number of cached token": 0,
        "cost": 0
    }}
    for type_, tokens in list_token_usage:
        temp['text evaluate']['number of input token'] += tokens.prompt_token_count
        temp['text evaluate']['number of output token'] += tokens.candidates_token_count
        temp['text evaluate']['number of cached token'] += tokens.cached_content_token_count
        temp['text evaluate']['cost'] += tokens.prompt_token_count * cost_api['input_token'] + tokens.candidates_token_count * cost_api['output_token'] + tokens.cached_content_token_count * cost_api['cached_token']
    
    cost.update(temp)
    total_cost = 0
    for item in cost.keys():
        total_cost += cost[item]['cost']
    
    
    return transcription, summary_conv, scores, formatted_conversation, cost, total_cost


key = os.getenv("GEMINI_API_KEY")
transcription, summary_conv, scores = pipeline("test.wav", key)
