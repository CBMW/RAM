# RAM/conversations/greetings/StartUpGreetings.py

import random

class StartUpGreetings:
    """
    This class manages the startup greetings for the RAM chatbot.
    It provides a method to retrieve a random greeting when the bot is first launched.
    """

    def __init__(self):
        self.greetings = [
            "Hello! I'm RAM, your Recon Analysis and Mitigation assistant. How can I help you today?",
            "Hi there! RAM here, ready to assist you with your penetration testing activities.",
            "Greetings! I'm RAM, your security reconnaissance partner. Let's get started!",
            "Welcome! I'm RAM, here to help you analyze and mitigate security threats. What would you like to do first?",
            "Hello! RAM at your service for all your recon and mitigation needs. How can I assist you today?",
            "Hi! I'm RAM, your dedicated assistant for recon and security analysis. How may I help you?",
            "Welcome aboard! RAM is ready to support your penetration testing endeavors. What's our first task?",
            "Greetings! RAM here to streamline your recon and mitigation processes. How can we proceed?",
            "Hello! Let's kick off your security assessment with RAM by your side. What would you like to begin with?",
            "Hi! RAM is online and ready to assist with your recon and mitigation strategies. How can I assist?",
            "Welcome! I'm RAM, designed to enhance your penetration testing workflow. What’s next on the agenda?",
            "Hello! RAM is here to help you navigate through your security analysis tasks. How can I support you today?",
            "Hi there! Ready to dive into some recon activities with RAM? Let’s get started!",
            "Greetings! RAM is set to assist you in identifying and mitigating security vulnerabilities. How may I help?",
            "Welcome! I'm RAM, your partner in comprehensive recon and mitigation efforts. What would you like to tackle first?"
        ]

    def get_greeting(self):
        """
        Returns a random startup greeting.
        """
        return random.choice(self.greetings)
