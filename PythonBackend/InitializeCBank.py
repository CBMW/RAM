# PythonBackend/InitializeCBank.py

from db.conversations.greetings.StartUpGreetings import StartUpGreetings
from db.conversations.greetings.Greetings import Greetings
from db.conversations.bye.Bye import Bye
from db.conversations.clarifications.Clarifications import Clarifications
from db.conversations.greetingResponses.GreetingResponses import GreetingResponses
from db.conversations.greetingResponses.Good import Good
from db.conversations.greetingResponses.Bad import Bad
from db.conversations.suggestions.UserSuggestions import UserSuggestions

class ConversationBank:
    """
    This class initializes and holds all conversation classes for the RAM chatbot.
    It ensures that all conversation modules are instantiated and ready for use.
    """
    def __init__(self):
        # Initialize greeting classes
        self.startup_greeter = StartUpGreetings()
        self.general_greeter = Greetings()
        
        # Initialize bye/farewell class
        self.bye_handler = Bye()
        
        # Initialize clarification class
        self.clarification_handler = Clarifications()
        
        # Initialize greeting responses
        self.greeting_responses = GreetingResponses()
        self.good_responses = Good()
        self.bad_responses = Bad()
        
        # Initialize user suggestions handler
        self.user_suggestions = UserSuggestions()
