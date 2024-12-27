# RAM/conversations/greetingResponses/GreetingResponses.py

import random

class GreetingResponses:
    """
    This class manages casual greeting responses for the RAM chatbot.
    It provides a method to retrieve a random response when the user initiates a greeting.
    """

    def __init__(self):
        self.responses = [
            "Hey there! How's it going?",
            "Hi! Great to see you.",
            "Hello! What's up?",
            "Hey! Ready to dive into some recon?",
            "Hiya! How can I assist you today?",
            "Hello! What's on your mind?",
            "Hey! How can RAM help you today?",
            "Hi! Ready to get started with your tasks?",
            "Hello! Need any help with your projects?",
            "Hey there! What's the plan for today?",
            "Hi! How's your day going?",
            "Hello! What can I do for you today?",
            "Hey! Let's tackle some security tasks.",
            "Hi! What recon activities are we starting with?",
            "Hello! Ready to secure your systems?",
            "Hey there! How can I support your work?",
            "Hi! Let's get your penetration testing underway.",
            "Hello! What's the first task today?",
            "Hey! How can I make your day easier?",
            "Hi! Ready to analyze some threats?",
            "Hello! Let's begin your security assessment.",
            "Hey there! What recon work is on the agenda?",
            "Hi! How can RAM assist with your objectives?",
            "Hello! Ready to mitigate some risks?",
            "Hey! What's our focus today?",
            "Hi! Let's enhance your security measures.",
            "Hello! How can we improve your defenses?",
            "Hey there! Ready to start your scan?",
            "Hi! Let's identify some vulnerabilities.",
            "Hello! How can I help you secure your network?",
            "Hey! Ready to explore some recon strategies?",
            "Hi! Let's kick off your security tasks."
        ]

    def get_response(self):
        """
        Returns a random casual greeting response.
        """
        return random.choice(self.responses)
