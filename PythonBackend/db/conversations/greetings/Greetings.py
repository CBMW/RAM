# RAM/conversations/greetings/Greetings.py

import random

class Greetings:
    """
    This class manages the general greetings for the RAM chatbot.
    It provides a method to retrieve a random greeting after periods of idleness or specific triggers.
    """

    def __init__(self):
        self.greetings = [
            "Hello again! How can I assist you further with your security assessments?",
            "Hi! Ready to continue with your penetration testing activities?",
            "Welcome back! Let me know how I can help you today.",
            "Hey there! What would you like to work on next?",
            "Good to see you! Do you need assistance with any specific recon tasks?",
            "Hi again! What’s the next step in your security analysis?",
            "Hello! Ready to proceed with your latest penetration test?",
            "Greetings! How can RAM support your current security objectives?",
            "Welcome back! Do you have any new targets or scans to initiate?",
            "Hey! Let’s continue securing your network. What’s our focus today?",
            "Good to see you again! How can I help with your ongoing assessments?",
            "Hi! Need help interpreting recent scan results or planning next steps?",
            "Hello again! What recon activities would you like to perform now?",
            "Greetings! Let’s enhance your security posture. What’s on the agenda?",
            "Welcome back! How can RAM assist you in mitigating the latest threats?"
        ]

    def get_greeting(self):
        """
        Returns a random general greeting.
        """
        return random.choice(self.greetings)
