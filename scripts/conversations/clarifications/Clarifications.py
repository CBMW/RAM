# RAM/conversations/clarifications/Clarifications.py

import random

class Clarifications:
    """
    This class manages clarification prompts for the RAM chatbot.
    It provides a method to retrieve a random clarification message when the bot needs more information.
    """

    def __init__(self):
        self.clarifications = [
            "I'm not sure what you meant. Could you please clarify that?",
            "Could you please provide more details on that?",
            "I'm having trouble understanding. Can you elaborate?",
            "Can you please explain that in a different way?",
            "I didn't quite catch that. Could you rephrase?",
            "Could you give me more information about that?",
            "I'm not certain I understand. Can you clarify?",
            "Can you provide additional context?",
            "Could you specify what you mean by that?",
            "I'm not sure I follow. Could you explain further?",
            "Can you elaborate on that point?",
            "Could you provide more specifics?",
            "I'm unclear about that. Can you clarify?",
            "Can you tell me more about that?",
            "Could you expand on your previous statement?",
            "I'm not certain I understand. Could you provide more details?",
            "Can you please give me more information?",
            "Could you clarify what you mean?",
            "I'm having difficulty understanding. Can you elaborate?",
            "Can you please explain that further?",
            "Could you provide a bit more detail?",
            "I'm not sure I understand. Can you clarify?",
            "Can you elaborate a little more on that?",
            "Could you please provide more insight?",
            "I'm unclear on that. Could you explain further?",
            "Can you give me more context?",
            "Could you specify that a bit more?",
            "I'm not certain I get it. Can you elaborate?",
            "Can you please provide additional details?",
            "Could you explain that in more depth?",
            "I'm having trouble following. Can you clarify?",
            "Can you provide more background on that?",
            "Could you please expand on that?",
            "I'm not sure I understand. Could you provide more information?",
            "Can you elaborate on what you mean?",
            "Could you give me a clearer explanation?",
            "I'm unclear about that. Can you provide more details?",
            "Can you please explain what you mean by that?",
            "Could you provide further clarification?",
            "I'm not sure I follow. Could you elaborate?",
            "Can you please give more specifics?",
            "Could you clarify your last statement?",
            "I'm having difficulty understanding. Could you provide more information?",
            "Can you explain that in a different way?",
            "Could you please provide a more detailed explanation?",
            "I'm not certain I understand. Can you elaborate further?",
            "Can you give more details on that?",
            "Could you please expand on your idea?",
            "I'm unclear about your request. Can you clarify?",
            "Can you provide more insight into that?",
            "Could you please explain that in more detail?",
            "I'm not sure I grasp that. Could you elaborate?"
        ]

    def get_clarification(self):
        """
        Returns a random clarification prompt.
        """
        return random.choice(self.clarifications)
