# RAM/conversations/suggestions/UserSuggestions.py

import random

class UserSuggestions:
    """
    This class manages user suggestion prompts for the RAM chatbot.
    It provides a method to retrieve a random message inviting the user to make a suggestion.
    """

    def __init__(self):
        self.suggestions = [
            "We are constantly striving to improve RAM and your experience. If you have any ideas or features you'd like to see, please share them with us. Type !suggestion YOUR MESSAGE HERE to submit your suggestion!",
            "Your feedback is invaluable to us! If there's something you'd like RAM to do better or a new feature you'd love to have, let us know. Type !suggestion YOUR MESSAGE HERE to provide your input.",
            "Help us enhance RAM by sharing your thoughts and ideas. Whether it's a new functionality or an improvement to existing features, your suggestions matter. Type !suggestion YOUR MESSAGE HERE to submit your suggestion!",
            "We're always looking to make RAM better for our users. If you have any recommendations or innovative ideas, we'd love to hear them. Please type !suggestion YOUR MESSAGE HERE to share your suggestion.",
            "Your insights can help shape the future of RAM. If you have any suggestions on how we can improve or expand our capabilities, don't hesitate to let us know. Type !suggestion YOUR MESSAGE HERE to provide your feedback.",
            "At RAM, we value your opinions and ideas. If there's something you'd like to see implemented or enhanced, please share your suggestions with us. Type !suggestion YOUR MESSAGE HERE to submit your thoughts.",
            "Do you have an idea that could make RAM more effective or user-friendly? We'd love to hear it! Please type !suggestion YOUR MESSAGE HERE to share your suggestion with our development team.",
            "Your suggestions play a crucial role in the development of RAM. If you have any ideas for new features or improvements, please let us know. Type !suggestion YOUR MESSAGE HERE to provide your input.",
            "We're committed to delivering the best experience with RAM. If you have any feedback or suggestions on how we can achieve this, we'd love to hear from you. Type !suggestion YOUR MESSAGE HERE to submit your suggestion.",
            "Help us build a better RAM by sharing your ideas and feedback. Whether it's a small improvement or a major feature request, your suggestions are welcome. Type !suggestion YOUR MESSAGE HERE to contribute your thoughts.",
            "Your feedback helps us enhance RAM to better meet your needs. If you have any suggestions or ideas, please share them with us. Type !suggestion YOUR MESSAGE HERE to submit your suggestion.",
            "We believe in continuous improvement and your input is key. If you have any suggestions for RAM, please let us know by typing !suggestion YOUR MESSAGE HERE.",
            "Have an idea that could improve RAM's functionality or usability? We'd love to hear it! Type !suggestion YOUR MESSAGE HERE to share your suggestion with us.",
            "Your ideas can make a significant impact on RAM's development. If you have any suggestions or feedback, please share them by typing !suggestion YOUR MESSAGE HERE.",
            "We're eager to hear your thoughts on how we can enhance RAM. If you have any suggestions or ideas, please let us know by typing !suggestion YOUR MESSAGE HERE.",
            "Your input is essential for the growth of RAM. If you have any suggestions or feature requests, please share them with us by typing !suggestion YOUR MESSAGE HERE.",
            "Help us tailor RAM to better suit your needs by sharing your suggestions and ideas. Type !suggestion YOUR MESSAGE HERE to provide your feedback.",
            "We're dedicated to making RAM the best it can be, and your suggestions are a big part of that. Please type !suggestion YOUR MESSAGE HERE to share your ideas.",
            "Your feedback drives the evolution of RAM. If you have any suggestions or improvements in mind, please share them by typing !suggestion YOUR MESSAGE HERE.",
            "Join us in enhancing RAM by providing your valuable suggestions. Whether it's a new feature or an improvement, we'd love to hear from you. Type !suggestion YOUR MESSAGE HERE to submit your idea."
        ]

    def get_suggestion_prompt(self):
        """
        Returns a random user suggestion prompt.
        """
        return random.choice(self.suggestions)
