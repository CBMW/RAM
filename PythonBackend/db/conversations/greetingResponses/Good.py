# RAM/conversations/greetingResponses/Good.py

import random

class Good:
    """
    This class manages responses for when the user indicates they are doing well.
    It provides a method to retrieve a random positive response.
    """

    def __init__(self):
        self.responses = [
            "That's great! Ready to set a new target?",
            "Awesome! Let's get started with your next task.",
            "Glad to hear that! How can I assist you today?",
            "Fantastic! What recon activity would you like to begin?",
            "Excellent! Let's dive into some penetration testing.",
            "Happy to hear! What's our first priority today?",
            "Great! Ready to analyze some security threats?",
            "Wonderful! How can RAM support your objectives?",
            "Perfect! Let's start securing your systems.",
            "That's awesome! What would you like to work on next?",
            "Good to hear! Let's identify some vulnerabilities.",
            "Superb! How can we enhance your security measures?",
            "Nice! Ready to begin your security assessment?",
            "Glad you're doing well! What's the next step?",
            "Excellent news! Let's tackle some recon tasks.",
            "That's wonderful! How can I help you today?",
            "Great to hear! Let's start your scan.",
            "Awesome! What's on the agenda today?",
            "Fantastic! Let's work on securing your network.",
            "Happy to hear! Ready to begin?",
            "Perfect! What recon strategy shall we employ?",
            "That's excellent! Let's start mitigating risks.",
            "Super! How can we improve your defenses today?",
            "Nice to hear! Let's initiate your penetration test.",
            "Glad you're good! What's our focus?",
            "Great! Let's enhance your security posture.",
            "Awesome! Ready to explore some recon methods?",
            "Fantastic! How can RAM assist with your goals?",
            "Happy to hear! Let's get to work.",
            "Perfect! What tasks are we tackling today?",
            "That's great! Let's start your security analysis.",
            "Excellent! How can we proceed with your recon?"
        ]

    def get_response(self):
        """
        Returns a random positive response.
        """
        return random.choice(self.responses)
