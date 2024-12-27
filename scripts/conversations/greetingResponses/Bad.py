# RAM/conversations/greetingResponses/Bad.py

import random

class Bad:
    """
    This class manages responses for when the user indicates they are not doing well.
    It provides a method to retrieve a random empathetic and encouraging response.
    """

    def __init__(self):
        self.responses = [
            "I'm sorry to hear that. How about we do some recon to take your mind off things?",
            "That's not good... Maybe some security tasks can help?",
            "I'm here for you. Let's work on some recon activities together.",
            "Sorry to hear you're feeling this way. Let's tackle a task to lighten the mood.",
            "I understand. How about we start with a simple penetration test?",
            "That's tough. Maybe analyzing some threats can help distract you.",
            "I'm here to help. Let's work on securing your systems together.",
            "I'm sorry you're feeling down. Let's engage in some recon work.",
            "It's okay to feel that way. Let's start with a security assessment.",
            "I'm here to support you. How about we begin some recon tasks?",
            "Sorry to hear that. Let's dive into some penetration testing.",
            "I understand. Maybe identifying some vulnerabilities can help?",
            "I'm sorry. Let's work together on some security measures.",
            "That's unfortunate. How about we start securing your network?",
            "I'm here for you. Let's initiate a recon scan.",
            "I'm sorry you're feeling this way. Let's begin some security tasks.",
            "It's okay. Let's work on mitigating some risks together.",
            "I'm here to assist. How about we explore some recon strategies?",
            "Sorry to hear that. Let's start with a security analysis.",
            "I'm here to help. Let's engage in some penetration testing.",
            "It's okay to feel bad. Let's begin securing your systems.",
            "I'm sorry. Let's tackle some recon activities together.",
            "I'm here for you. How about we start a security assessment?",
            "Sorry to hear that. Let's work on some recon tasks to help.",
            "I understand. Let's begin securing your network together.",
            "I'm here to support you. Let's start some penetration testing.",
            "It's okay. Let's engage in some security measures.",
            "I'm sorry you're feeling this way. Let's dive into some recon work.",
            "That's tough. Let's start with a security scan.",
            "I'm here to help. How about we begin some recon activities?",
            "Sorry to hear that. Let's work on mitigating some threats.",
            "I'm here for you. Let's initiate a security assessment.",
            "I'm sorry. Let's start securing your systems together.",
            "It's okay to feel down. Let's begin some penetration testing.",
            "I'm here to assist. How about we explore some security tasks?",
            "Sorry to hear that. Let's start with a recon scan.",
            "I understand. Let's work on securing your network.",
            "I'm here to help. Let's engage in some recon activities.",
            "It's okay. Let's begin some security measures together.",
            "I'm sorry you're feeling this way. Let's dive into some penetration testing.",
            "That's tough. How about we start with a security analysis?",
            "I'm here for you. Let's initiate some recon tasks.",
            "Sorry to hear that. Let's work on securing your systems.",
            "I'm here to support you. Let's begin a security assessment.",
            "It's okay to feel bad. Let's engage in some recon work.",
            "I'm sorry. Let's start with some penetration testing together.",
            "I understand. Let's work on mitigating some security risks.",
            "I'm here to help. How about we explore some recon strategies?",
            "Sorry to hear that. Let's begin securing your network."
        ]

    def get_response(self):
        """
        Returns a random empathetic and encouraging response.
        """
        return random.choice(self.responses)
