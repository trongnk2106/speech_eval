import ast
import google.generativeai as genai
import os

from const import communication_skill, product_expertise, sales_skills

# Set up Gemini API (make sure to set your API key as an environment variable)
class EvaluateSpeech:
    def __init__(self, apikey=""):
            
        genai.configure(api_key=apikey)

        self.base_systemp_prompt = "Evaluate the following conversation based on the provided evaluation criteria. For each sub-criterion, assign a score from 1 to 5 based on the performance of the consultant. Provide a justification for each score."

        self.systemp_prompt_communiation_skill = f"""{self.base_systemp_prompt}
        Evaluation Criteria : {communication_skill}
        """
        self.systemp_prompt_product_expertise = f"""{self.base_systemp_prompt}
        Evaluation Criteria : {product_expertise}
        """

        self.systemp_prompt_sales_skills = f"""{self.base_systemp_prompt}
        Evaluation Criteria : {sales_skills}
        """

        self.output_expect = {
            "Key_A": {
                "Key_1": "value_1",
                "Key_2": "value_2",
                "Key_3": "value_3"
            },
            "Key_B": {
                "Key_4": "value_4",
                "Key_5": "value_5",
                "Key_6": "value_6"
            },
            "Key_C": {
                "Key_7": "value_7",
                "Key_8": "value_8",
                "Key_9": "value_9"}
        }




    def generate_input(self, conversation):
        user_prompt = f"""Evaluate the communication skill of the consultant in the following conversation.
        Conversation: {conversation}
        The output should be in valid JSON format. Strictly follow this JSON structure:
        {self.output_expect}
        Provide scores. Only return the JSON object."""
        return user_prompt

    def eval_speech(self, user_prompt, systemp_prompt):
        # Use Gemini Pro for text generation
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Combine system prompt and user prompt
        full_prompt = f"{systemp_prompt}\n\n{user_prompt}"
        
        try:
            response = model.generate_content(full_prompt, 
                                            generation_config=genai.types.GenerationConfig(
                                                temperature=0.7
                                            ))
            
            # Extract and parse the JSON response
            # You might need to adjust this parsing based on Gemini's exact output format
            res_text = response.text.strip()
            token_usage = response.usage_metadata
            # Try to parse the JSON response
            try:
                res = ast.literal_eval(res_text)
                return res, token_usage
            except (SyntaxError, ValueError):
                # If direct parsing fails, you might need more sophisticated parsing
                if "```json" in res_text:
                    res_text = res_text.split("```json")[1]
                    res_text = res_text.split("```")[0]
                    res = ast.literal_eval(res_text)
                # print(res_text)
                return res, token_usage
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def run(self, conversation):
        dict_metric_prompt = {
            "communication_skill": self.systemp_prompt_communiation_skill,
            "product_expertise": self.systemp_prompt_product_expertise,
            "sales_skills": self.systemp_prompt_sales_skills
        }
        const_dict = {
            "communication_skill": communication_skill,
            "product_expertise": product_expertise,
            "sales_skills": sales_skills
        }
        score_dict = {
            "communication_skill": 0.4,
            "product_expertise": 0.3,
            "sales_skills": 0.3
        }
        
        total_score = 0
        list_token_usage = []
        for key, value in const_dict.items():
            system_prompt = dict_metric_prompt[key]
            user_prompt = self.generate_input(conversation)
            res, token_usage = self.eval_speech(user_prompt, system_prompt)
            list_token_usage.append(token_usage)
            if not res: 
                while True: 
                    res = self.eval_speech(user_prompt, system_prompt)
                    if res:
                        break
            
            scores = []
            for k, v in res.items():
                weight = value[k]["weight"]
                scores.append((sum(map(int, v.values())) / 3) * weight)
            
            total_score += sum(scores) * score_dict[key]
        
        print(f"Total score: {total_score}")
        return total_score, list_token_usage
    


if __name__ == "__main__":
    conversation = """Role : [1]: Nhân viên tư vấn
    [2]: Khách hàng
    Converstation: 
    [1]: A lô.
    [2]: Bên gọi số điện thoại của anh Dũng bên đặt bên em keo chống thấm trong suốt đúng không anh?
    [1]: Cái gì cơ nhờ?
    [2]: Là keo chống thấm trong suốt anh ơi. Keo để quét chống thấm.
    [1]: À. Ờ để người ta đang xem xem cái hôm nọ đặt một chỗ rồi gửi về nhà mà nó không không không thấy có tác dụng lắm.
    [2]: Cái đó thì anh đặt ở đâu em không có biết anh nha. Còn cái này bên em bán 3 đến 4 năm nay rồi anh.
    [1]: À thế à? Ờ ờ ờ để để coi xem nào nha.
    [2]: Là sao? Chưa sao chưa đặt hàng mà để thông tin đặt hàng ở đây rồi giờ xem lại nữa là sao anh?
    [1]: Thì mình xem lại cái cái cái mặt hàng nó như thế nào đã nha. Chứ không không xem cho kỹ là mới để thông tin đặt hàng. Ừm ừm.
    [2]: Ừ. Cái gì anh? Chưa, chưa có xem là để thông tin đặt hàng ở đây là sao?
    [1]: Chắc là bấm nhầm hay sao?
    [2]: Bấm nhầm cái gì mà để cái thông tin khu Thượng khu Thượng Phong gì ở Quốc Niệm, Bắc Ninh ở đây anh? Vũ Văn Dũng anh anh để anh bấm nhầm dùm em để cái tên của anh ở đây. Trời ơi nha, lần sau không có nhu cầu đừng để thông tin đặt hàng, cảm ơn nha.
    [1]: Ừm."""

    EvaluateSpeech().run(conversation)
    