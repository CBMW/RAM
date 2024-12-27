# RAM/conversations/bye/Bye.py

import random

class Bye:
    """
    This class manages the farewell messages for the RAM chatbot.
    It provides a method to retrieve a random goodbye message when the conversation ends.
    """

    def __init__(self):
        self.goodbyes = [
            "Goodbye! If you need further assistance, feel free to reach out.",
            "Farewell! Stay secure and have a great day.",
            "Bye! Let me know if you need any more help with your recon tasks.",
            "See you later! I'm here whenever you need me.",
            "Take care! Don't hesitate to call on RAM for your security needs.",
            "Goodbye! Wishing you a safe and secure day ahead.",
            "Farewell! Ready to assist you anytime you require.",
            "Bye for now! Keep your systems protected.",
            "Until next time! Stay vigilant against security threats.",
            "Take it easy! I'm here whenever you're ready to continue.",
            "Goodbye! May your networks remain secure.",
            "Farewell! Looking forward to our next session.",
            "Bye! Remember, RAM is always here to help you mitigate risks.",
            "See you! Stay safe and secure.",
            "Take care! Let RAM know if you need further assistance.",
            "Goodbye! Keep up the great work in maintaining security.",
            "Farewell! I'm just a message away if you need anything.",
            "Bye for now! Ensure your defenses are always up.",
            "Until next time! Stay proactive in your security measures.",
            "Take it easy! Let me know when you're ready to resume.",
            "Goodbye! Don't forget to review your latest scan results.",
            "Farewell! Keep your reconnaissance efforts strong.",
            "Bye! Stay alert and keep your systems updated.",
            "See you later! RAM is here to support your security initiatives.",
            "Take care! Protecting your assets is our priority.",
            "Goodbye! Let's catch up soon to enhance your security posture.",
            "Farewell! May your vulnerabilities remain minimal.",
            "Bye! Keep utilizing RAM for effective mitigation strategies.",
            "Until next time! Stay informed about the latest security trends.",
            "Take it easy! I'm here to assist you whenever needed.",
            "Goodbye! Ensure regular scans to maintain system integrity.",
            "Farewell! Keep leveraging RAM for your pentesting activities.",
            "Bye! Maintain a proactive approach to security.",
            "See you! Let RAM help you stay ahead of potential threats.",
            "Take care! I'm available for any future security assessments.",
            "Goodbye! Stay committed to securing your infrastructure.",
            "Farewell! Let’s continue to strengthen your defenses next time.",
            "Bye! Keep your recon activities thorough and effective.",
            "Until next time! Stay dedicated to your security goals.",
            "Take it easy! I'm here to streamline your mitigation processes.",
            "Goodbye! Keep leveraging the latest tools for optimal security.",
            "Farewell! Wishing you success in all your security endeavors.",
            "Bye! Let RAM assist you in maintaining robust security measures.",
            "See you later! Stay prepared against any security challenges.",
            "Take care! Remember, proactive security is the best defense.",
            "Goodbye! Let’s work together to keep your systems safe.",
            "Farewell! I'm always here to help you analyze and mitigate risks.",
            "Bye! Keep your security strategies up-to-date with RAM's assistance.",
            "Until next time! Stay resilient against security threats.",
            "Take it easy! I'm ready to support your next recon mission."
        ]

    def get_goodbye(self):
        """
        Returns a random goodbye message.
        """
        return random.choice(self.goodbyes)
