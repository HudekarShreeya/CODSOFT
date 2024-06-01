def simple_chatbot():
    print("Hi there! I'm a chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").lower()

        # Define some predefined responses based on user queries
        if "hello" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but thanks for asking!")
        elif "your name" in user_input:
            print("Chatbot: I'm a chatbot created to assist you.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")
        elif "what can you do" in user_input or "help me" in user_input:
            print("Chatbot: I can provide information or assist with basic queries.")
        elif "who created you" in user_input or "your creator" in user_input:
            print("Chatbot: I was created by an AI developer.")
        elif "tell me a joke" in user_input or "joke" in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif "where are you from" in user_input or "your origin" in user_input:
            print("Chatbot: I exist in the digital world!")
        elif "how old are you" in user_input or "your age" in user_input:
            print("Chatbot: I don't have an age. I'm just a program.")
        elif "tell me something interesting" in user_input:
            print("Chatbot: Did you know that honey never spoils?")
        elif "what are you doing" in user_input or "your activity" in user_input:
            print("Chatbot: I'm here to assist you. Just ask!")
        elif "do you sleep" in user_input or "sleep schedule" in user_input:
            print("Chatbot: Nope, I'm always here to chat!")
        elif "can you sing" in user_input or "sing a song" in user_input:
            print("Chatbot: I'm better at chatting than singing!")
        elif "what's the weather like" in user_input or "weather" in user_input:
            print("Chatbot: I don't have access to weather information right now.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please ask something else?")

# Start the chatbot
simple_chatbot()
