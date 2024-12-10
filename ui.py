import gradio as gr 
from pipeline import pipeline
import uuid
import soundfile as sf
import os 
apikey = os.getenv("GEMINI_API_KEY")
def save_audio_file(audio_data):
    if audio_data is not None:
        # Tách sample rate và mảng dữ liệu
        sample_rate, audio_array = audio_data
        # Đặt tên file để lưu
        if os.path.exists("./__logs"):
            os.makedirs("./__logs")
        save_path = "./__logs/" + str(uuid.uuid4()) + ".wav"
        # Lưu tệp âm thanh từ NumPy array
        sf.write(save_path, audio_array, sample_rate)
        return save_path
    return None


def run(audio_data):
    if isinstance(audio_data, tuple): 
        audio_file = save_audio_file(audio_data)
    elif isinstance(audio_data, str):
        # breakpoint()
        audio_file = audio_data
    conversation, sum_conv, scores, formatted_conversation = pipeline(audio_file, api_key=apikey)
    return conversation, sum_conv, scores


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Row():
        audio = gr.Audio(label="Upload an audio file", type="filepath")
    with gr.Row():
        with gr.Column():
            conversation = gr.Textbox(label="Conversation")
            # conversation = gr.HTML(label="Hội thoại đã định dạng")

        with gr.Column():
            with gr.Row():
                summary_conv = gr.Textbox(label="Summary")
            with gr.Row():
                scores = gr.Textbox(label="Scores")
                
    with gr.Row():
        try_button = gr.Button(value="RUN")
    
    try_button.click(
        fn=run,
        inputs=[audio],
        outputs=[conversation, summary_conv, scores]
    )
            
if __name__ == "__main__":
    demo.launch()