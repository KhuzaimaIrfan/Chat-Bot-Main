from app.chatbot_logic import get_bot_response, load_data

def test_chatbot():
    data = load_data()
    
    test_cases = [
        # FAQ Tests
        ("Do you have vegan food?", "vegetarian"),
        ("Is your meat halal?", "Halal certified"),
        ("parking available?", "parking lot"),
        ("how to pay?", "accept cash, credit/debit"),
        
        # Menu Search Tests
        ("I want something spicy", "Zinger Burger"), # Should match flavour/description
        ("Do you have mushroom pasta?", "Creamy Alfredo"), # Should match flavour
        ("price of zinger", "Zinger Burger"),
        ("show me the menu", "Popular Items"),
    ]
    
    print("Running Chatbot Tests...\n")
    
    for query, expected_keyword in test_cases:
        response = get_bot_response(query, data)
        passed = expected_keyword.lower() in response.lower()
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Query: '{query}'")
        print(f"Response snippet: {response[:50]}...")
        print(f"Expected: '{expected_keyword}' -> {status}\n")

if __name__ == "__main__":
    test_chatbot()
