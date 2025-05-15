import random
import nltk
from nltk.chat.util import Chat, reflections

class BasicChatbot:
    def __init__(self):
        self.pairs = [
            [
                r"hi|hello|hey",
                ["Hello there!", "Hi!", "Hey! How can I help you today?"]
            ],
            [
                r"how are you ?",
                ["I'm doing well, thank you!", "I'm great! How about you?"]
            ],
            [
                r"what is your name ?",
                ["I'm a basic chatbot. You can call me Chatty!", "My name is Chatty. Nice to meet you!"]
            ],
            [
                r"quit|bye|exit",
                ["Goodbye! Have a great day!", "It was nice talking to you. Bye!"]
            ],
            [
                r"(.*)",
                ["I'm not sure I understand. Could you rephrase that?", 
                 "Interesting! Tell me more.", 
                 "I see. What else would you like to discuss?"]
            ]
        ]
        self.chatbot = Chat(self.pairs, reflections)
    
    def start_chat(self):
        print("\nChatty: Hello! I'm a basic chatbot. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'bye', 'exit']:
                print("Chatty: Goodbye!")
                break
            response = self.chatbot.respond(user_input)
            print(f"Chatty: {response}")

def main():
    nltk.download('punkt')
    chatbot = BasicChatbot()
    chatbot.start_chat()

if __name__ == "__main__":
    main()