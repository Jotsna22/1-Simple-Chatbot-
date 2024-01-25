import random

class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your simple chatbot. How can I assist you today?"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask later."

    def respond_to_greeting(self):
        return "Hi there! How can I help you today?"

    def respond_to_question(self, question):
        responses = {
            "How are you?": "I'm just a computer program, but thanks for asking!",
            "What's your name?": "I'm a chatbot without a name.",
            "What do you do?": "I'm here to assist and answer your questions.",
            "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "Who created you?": "I was created by a human."
        }

        return responses.get(question, "I'm not sure how to answer that. Can you try another question?")

    def ask_user(self, question):
        user_response = input(question + " ")
        self.context[question] = user_response
        return user_response

    def chat(self):
        print(self.greet())

        for _ in range(3):
            user_response = self.ask_user("How may I assist you today?")
            print(self.respond_to_question(user_response))

        print(self.farewell())

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
