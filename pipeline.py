from gemini_speech_eval import EvaluateSpeech
from extract_conversation import S2TSumary
from const import cost_api
import os

def calculate_cost(token_usage):
    """
    Tính toán chi phí dựa trên số lượng token.
    """
    return (
        token_usage.prompt_token_count * cost_api['input_token'] +
        token_usage.candidates_token_count * cost_api['output_token'] +
        token_usage.cached_content_token_count * cost_api['cached_token']
    )

def initialize_cost_entry():
    """
    Khởi tạo một mục chi phí mặc định.
    """
    return {
        "number of input token": 0,
        "number of output token": 0,
        "number of cached token": 0,
        "cost": 0
    }

def pipeline(audio_file, api_key=""):
    # Trích xuất hội thoại từ file âm thanh
    transcription, summary_conv, formatted_conversation, token_usage, token_usage_summary = S2TSumary(apikey=api_key).run(audio_file)

    # Đánh giá hội thoại
    scores, list_token_usage = EvaluateSpeech(apikey=api_key).run(transcription)

    # Tính chi phí cho các tác vụ
    logs_cost = {
        "speech to text": {
            "number of input token": token_usage.prompt_token_count,
            "number of output token": token_usage.candidates_token_count,
            "number of cached token": token_usage.cached_content_token_count,
            "cost": calculate_cost(token_usage)
        },
        "text summary": {
            "number of input token": token_usage_summary.prompt_token_count,
            "number of output token": token_usage_summary.candidates_token_count,
            "number of cached token": token_usage_summary.cached_content_token_count,
            "cost": calculate_cost(token_usage_summary)
        }
    }

    # Tổng hợp chi phí đánh giá văn bản
    text_evaluate_cost = initialize_cost_entry()
    for tokens in list_token_usage:
        text_evaluate_cost["number of input token"] += tokens.prompt_token_count
        text_evaluate_cost["number of output token"] += tokens.candidates_token_count
        text_evaluate_cost["number of cached token"] += tokens.cached_content_token_count
        text_evaluate_cost["cost"] += calculate_cost(tokens)
        print(text_evaluate_cost)

    # Thêm chi phí đánh giá văn bản vào tổng chi phí
    logs_cost["text evaluate"] = text_evaluate_cost

    # Tính tổng chi phí
    total_cost = sum(item["cost"] for item in logs_cost.values())

    return transcription, summary_conv, scores, formatted_conversation, logs_cost, total_cost

if __name__ == "__main__":
    key = os.getenv("GEMINI_API_KEY")
    transcription, summary_conv, scores = pipeline("test.wav", key)