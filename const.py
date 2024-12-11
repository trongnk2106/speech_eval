cost_api = {
    "input_token": 0.075 / 1000000,
    "output_token": 0.3 / 1000000,
    "cached_token": 0.01875 / 1000000,
}


communication_skill_expect = {
    "voice_tone": {
        "Tốc độ nói phù hợp": 3,
        "Âm lượng phù hợp": 1,
        "Rõ ràng, dễ nghe": 3
    },
    "service_attitude": {
        "Thân thiện, nhiệt tình": 2,
        "Kiên nhẫn lắng nghe": 5,
        "Không cáu gắt/thô lỗ": 5
    },
    "appropriate_language": {
        "Từ ngữ lịch sự": 1,
        "Không dùng tiếng lóng": 4,
        "Không chửi thề": 5
    }
}


product_expertise = {
    "product_knowledge": {
        "Nắm rõ tính năng" :  "1-5 điểm",
        "Nắm rõ giá cả" :  "1-5 điểm",
        "Nắm rõ chính sách" :  "1-5 điểm",
    
    },
    "appropriate_consulting": {
        "weight" : 0.3,
        "standard" : {
            "Tư vấn đúng nhu cầu" :  "1-5 điểm",
            "Giải thích rõ ràng" :  "1-5 điểm",
            "So sánh sản phẩm" :  "1-5 điểm",
        }
    },
    "handling_inquiries": {
        "weight" : 0.3,
        "standard" : {
            "Trả lời đúng trọng tâm" :  "1-5 điểm",
            "Giải đáp thỏa đáng" :  "1-5 điểm",
            "Hướng dẫn chi tiết" :  "1-5 điểm",
        }
    }
}


# 1. Kỹ năng giao tiếp (40%)
# 1.1. Tone giọng nói (30%)
# - Tốc độ nói phù hợp [1-5 điểm]
# - Âm lượng phù hợp [1-5 điểm]
# - Rõ ràng, dễ nghe [1-5 điểm]
# 1.2. Thái độ phục vụ (40%)
# - Thân thiện, nhiệt tình [1-5 điểm]
# - Kiên nhẫn lắng nghe [1-5 điểm]
# - Không cáu gắt/thô lỗ [1-5 điểm]
# 1.3. Ngôn ngữ phù hợp (30%)
# - Từ ngữ lịch sự [1-5 điểm]
# - Không dùng tiếng lóng [1-5 điểm]
# - Không chửi thề [1-5 điểm]

communication_skill = {
    "voice_tone": {
        "weight" : 0.3, 
        "standard" : {
            "Tốc độ nói phù hợp" :  "1-5 điểm",
            "Âm lượng phù hợp" :  "1-5 điểm",
            "Rõ ràng, dễ nghe" :  "1-5 điểm",
        }
    },
    "service_attitude": {
        "weight" : 0.4, 
        "standard" : {
            "Thân thiện, nhiệt tình" :  "1-5 điểm",
            "Kiên nhẫn lắng nghe" :  "1-5 điểm",
            "Không cáu gắt/thô lỗ" :  "1-5 điểm",
        }
    },
    "appropriate_language": {
        "weight" : 0.3, 
        "standard" : {
            "Từ ngữ lịch sự" :  "1-5 điểm",
            "Không dùng tiếng lóng" :  "1-5 điểm",
            "Không chửi thề" :  "1-5 điểm",
        }
    }
}

#  Chuyên môn sản phẩm (30%)
# 2.1. Kiến thức sản phẩm (40%)
# - Nắm rõ tính năng [1-5 điểm]
# - Nắm rõ giá cả [1-5 điểm]
# - Nắm rõ chính sách [1-5 điểm]
# 2.2. Tư vấn phù hợp (30%)
# - Tư vấn đúng nhu cầu [1-5 điểm]
# - Giải thích rõ ràng [1-5 điểm]
# - So sánh sản phẩm [1-5 điểm]
# 2.3. Xử lý thắc mắc (30%)
# - Trả lời đúng trọng tâm [1-5 điểm]
# - Giải đáp thỏa đáng [1-5 điểm]
# - Hướng dẫn chi tiết [1-5 điểm]

product_expertise = {
    "product_knowledge": {
        "weight" : 0.4,
        "standard" : {
            "Nắm rõ tính năng" :  "1-5 điểm",
            "Nắm rõ giá cả" :  "1-5 điểm",
            "Nắm rõ chính sách" :  "1-5 điểm",
        }
    },
    "appropriate_consulting": {
        "weight" : 0.3,
        "standard" : {
            "Tư vấn đúng nhu cầu" :  "1-5 điểm",
            "Giải thích rõ ràng" :  "1-5 điểm",
            "So sánh sản phẩm" :  "1-5 điểm",
        }
    },
    "handling_inquiries": {
        "weight" : 0.3,
        "standard" : {
            "Trả lời đúng trọng tâm" :  "1-5 điểm",
            "Giải đáp thỏa đáng" :  "1-5 điểm",
            "Hướng dẫn chi tiết" :  "1-5 điểm",
        }
    }
}


# 3. Kỹ năng bán hàng (30%)
# 3.1. Kỹ năng thuyết phục (35%)
# - Nêu lợi ích rõ ràng [1-5 điểm]
# - Xử lý phản đối [1-5 điểm]
# - Tạo niềm tin [1-5 điểm]
# 3.2. Xử lý từ chối (35%)
# - Kiên nhẫn thuyết phục [1-5 điểm]
# - Linh hoạt đàm phán [1-5 điểm]
# - Tìm giải pháp thay thế [1-5 điểm]
# 3.3. Chốt đơn (30%)
# - Nắm bắt timing [1-5 điểm]
# - Kỹ thuật chốt sale [1-5 điểm]
# - Tỷ lệ thành công [1-5 điểm]

sales_skills = {
    "persuasion_skills": {
        "weight" : 0.35,
        "standard" : {
            "Nêu lợi ích rõ ràng" :  "1-5 điểm",
            "Xử lý phản đối" :  "1-5 điểm",
            "Tạo niềm tin" :  "1-5 điểm",
        }
    },
    "handling_objections": {
        "weight" : 0.35,
        "standard" : {
            "Kiên nhẫn thuyết phục" :  "1-5 điểm",
            "Linh hoạt đàm phán" :  "1-5 điểm",
            "Tìm giải pháp thay thế" :  "1-5 điểm",
        }
    },
    "closing_orders": {
        "weight" : 0.3,
        "standard" : {
            "Nắm bắt timing" :  "1-5 điểm",
            "Kỹ thuật chốt sale" :  "1-5 điểm",
            "Tỷ lệ thành công" :  "1-5 điểm",
        }
    }
}




# communication_skill = {
    
#     "voice_tone": {
#         :{
#         "appropriate_speed": "1-5 points",
#         "appropriate_volume": "1-5 points",
#         "clear_and_easy_to_hear": "1-5 points"
#     }},
#     "service_attitude": {
#         "friendly_enthusiastic": "1-5 points",
#         "listen_patiently": "1-5 points",
#         "not_irritable_rude": "1-5 points"
#     },
#     "appropriate_language": {
#         "polite_words": "1-5 points",
#         "no_slang": "1-5 points",
#         "no_swearing": "1-5 points"
#     }
# }

# 2. Product expertise (30%)
# 2.1. Product knowledge (40%)
# - Understand the features [1-5 points]
# - Understand the price [1-5 points]
# - Understand the policy clearly [1-5 points]
# 2.2. Appropriate consulting (30%)
# - Consulting according to needs [1-5 points]
# - Explain clearly [1-5 points]
# - Compare products [1-5 points]
# 2.3. Handling inquiries (30%)
# - Answer correctly to the point [1-5 points]
# - Satisfactory answer [1-5 points]
# - Detailed instructions [1-5 points]

# product_expertise = {
#     "product_knowledge": {
#         "understand_features": "1-5 points",
#         "understand_price": "1-5 points",
#         "understand_policy": "1-5 points"
#     },
#     "appropriate_consulting": {
#         "consulting_according_to_needs": "1-5 points",
#         "explain_clearly": "1-5 points",
#         "compare_products": "1-5 points"
#     },
#     "handling_inquiries": {
#         "answer_correctly": "1-5 points",
#         "satisfactory_answer": "1-5 points",
#         "detailed_instructions": "1-5 points"
#     }
# }


# 3. Sales skills (30%)
# 3.1. Persuasion skills (35%)
# - State the benefits clearly [1-5 points]
# - Handling objections [1-5 points]
# - Create trust [1-5 points]
# 3.2. Handling objections (35%)
# - Patience and persuasion [1-5 points]
# - Flexible negotiation [1-5 points]
# - Find alternative solutions [1-5 points]
# 3.3. Closing orders (30%)
# - Grasp the timing [1-5 points]
# - Sales closing techniques [1-5 points]
# - Success rate [1-5 points]

# sales_skills = {
#     "persuasion_skills": {
#         "state_benefits": "1-5 points",
#         "handling_objections": "1-5 points",
#         "create_trust": "1-5 points"
#     },
#     "handling_objections": {
#         "patience_persuasion": "1-5 points",
#         "flexible_negotiation": "1-5 points",
#         "find_alternative_solutions": "1-5 points"
#     },
#     "closing_orders": {
#         "grasp_timing": "1-5 points",
#         "sales_closing_techniques": "1-5 points",
#         "success_rate": "1-5 points"
#     }
# }


