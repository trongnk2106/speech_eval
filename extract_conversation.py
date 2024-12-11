import io
import os
import pathlib
import re


import google.generativeai as genai

class S2TSumary:
    def __init__(self, apikey=""):
        genai.configure(api_key=apikey)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def transcribe_audio(self, audio_path):
        # Initialize a Gemini model appropriate for your use case.

        # Create the prompt.
        prompt = f"""Transcribed conversation into a structured format:
        Required Output Format:
        ```
        Role : [1]: Nhân viên tư vấn
        [2]: Khách hàng
        Conversation:
        [1]: First dialogue from consultant
        [2]: First dialogue from customer
        ...
        ```

        Guidelines:
        1. Identify which speaker is the consultant and which is the customer
        2. Preserve the exact wording
        3. Remove any filler words or repetitions
        4. Maintain the conversation flow
        5. Use the specified role tags [1] and [2]
        """

        # Load the samplesmall.mp3 file into a Python Blob object containing the audio
        # file's bytes and then pass the prompt and the audio to Gemini.
        response = self.model.generate_content([
            prompt,
            {
                "mime_type": "audio/mp3",
                "data": pathlib.Path(audio_path).read_bytes()
            }
        ])
        
        return response.text, response.usage_metadata

    def summarize_conversation(self, conversation):
        prompt = f"""From conversation in below, write review for each speaker: 
        Conversation:
        {conversation}
        Example:
        Nhận xét
        Nhân viên tư vấn:
        - Lời lẽ: Lịch sự, chuyên nghiệp, sử dụng kính ngữ phù hợp ("anh", "ạ"), giải thích rõ ràng về sản phẩm, liệu trình sử dụng và chương trình khuyến mãi. Cô cũng chủ động xác nhận thông tin đơn hàng và địa chỉ giao hàng. Cách diễn đạt dễ hiểu, không sử dụng thuật ngữ chuyên môn quá khó.
        - Thái độ: Nhiệt tình, tận tâm tư vấn, kiên nhẫn giải đáp thắc mắc của khách hàng, khuyến khích khách hàng mua liệu trình đầy đủ để đạt hiệu quả tốt nhất nhưng không gây áp lực quá mức.
        Khách hàng:
        - Lời lẽ: Ngắn gọn, dễ hiểu, thể hiện sự quan tâm đến sản phẩm và giá cả.
        - Thái độ: Cẩn trọng, muốn dùng thử sản phẩm trước khi quyết định mua liệu trình đầy đủ. Có vẻ hơi lưỡng lự ban đầu nhưng sau khi được tư vấn kỹ càng thì đồng ý mua.
        """
        response = self.model.generate_content(prompt, 
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.7
                            ))
        
        return response.text, response.usage_metadata 
    
    def format_conversation(self, conversation):
        """
        Định dạng hội thoại với màu sắc cho từng người nói.
        """
        lines = conversation.split("\n")
        formatted_lines = []
        for line in lines:
            if line.startswith("[2]:"):
                formatted_lines.append(f'<span style="color:red;">{line}</span>')
            elif line.startswith("[1]:"):
                formatted_lines.append(f'<span style="color:green;">{line}</span>')
            else:
                formatted_lines.append(line)  # Dòng không xác định giữ nguyên
        return "<br>".join(formatted_lines)
        

    def run(self, audio_path):
        # Transcribe audio
        transcription, token_usage_s2t = self.transcribe_audio(audio_path)
        pattern = r"```(.*?)```"
        conversation = re.search(pattern, transcription, re.DOTALL).group(1).strip()
        formatted_conversation = self.format_conversation(conversation)
        res, token_usage_summary = self.summarize_conversation(conversation)
        return conversation, res, formatted_conversation, token_usage_s2t, token_usage_summary



if __name__ == "__main__":
    key = os.getenv("GEMINI_API_KEY")
    res, token_count = S2TSumary(apikey=key).run('./test.wav')
    print(res)

# Example usage
# conversation = main('/path/to/your/audio/file.wav')
# print(conversation)