import re

def get_bot_response(user_input):
   
    user_input = user_input.lower()

   
    if re.search(r'hi|hello|hey', user_input):
        return "Hello there! How can I assist you today?"
    
    elif re.search(r'how are you', user_input):
        return "I am just a program, but I am functioning perfectly! How about you?"
    
    elif re.search(r'name', user_input):
        return "You can call me rule based chatBot"
    elif re.search(r'help', user_input):
        return "I can respond to greetings, questions about my name, and status updates."
    
    elif re.search(r'bye|goodbye', user_input):
        return "Goodbye! Have a great day!"
    
    else:
        return "I am sorry, I didn't quite understand that. Could you try asking something else?"

def start_chatbot():
    print("--- Welcome to the Chatbot (Type 'bye' to exit) ---")
    
    while True:
        
        user_input = input("You: ")
        
       
        if user_input.lower() in ['bye', 'goodbye']:
            print("Bot: Goodbye! Have a great day!")
            break
        
        response = get_bot_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    start_chatbot()
        