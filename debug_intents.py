from app.chatbot_logic import detect_intent, INTENT_KEYWORDS, calculate_intent_score, normalize_text

def debug_intents():
    queries = [
        "Do you have vegan food?",
        "parking available?",
        "how to pay?",
        "I want something spicy",
        "Do you have mushroom pasta?"
    ]
    
    print("Debugging Intent Detection...\n")
    
    for q in queries:
        print(f"Query: '{q}'")
        normalized = normalize_text(q)
        print(f"Normalized: '{normalized}'")
        
        scores = {}
        for intent, keywords in INTENT_KEYWORDS.items():
            score = calculate_intent_score(normalized, keywords)
            scores[intent] = score
            
        print(f"Scores: {scores}")
        detected = detect_intent(q)
        print(f"Detected Intent: {detected}\n")
        print("-" * 30)

if __name__ == "__main__":
    debug_intents()
