# PythonBackend/ConversationHandler.py

from db.conversations.greetings.StartUpGreetings import StartUpGreetings
from db.conversations.greetings.Greetings import Greetings
from db.conversations.bye.Bye import Bye
from db.conversations.clarifications.Clarifications import Clarifications
from db.conversations.greetingResponses.GreetingResponses import GreetingResponses
from db.conversations.greetingResponses.Good import Good
from db.conversations.greetingResponses.Bad import Bad
from db.conversations.suggestions.UserSuggestions import UserSuggestions
from InitializeCBank import ConversationBank
from datetime import datetime
import json

class ConversationHandler:
    """
    This class handles conversation responses and suggestion management.
    It utilizes the ConversationBank to fetch appropriate responses based on user input.
    """
    
    def __init__(self):
        # Initialize the conversation bank
        self.conversation_bank = ConversationBank()

    def get_response(self, user_input: str) -> str:
        """
        Processes the user input and returns the appropriate bot response.
        
        Parameters:
            user_input (str): The message input by the user.
        
        Returns:
            str: The bot's response.
        """
        user_input = user_input.lower().strip()

        # Simple keyword-based response logic
        if user_input in ["hi", "hello", "hey"]:
            return self.conversation_bank.greeting_responses.get_response()
        elif user_input in ["bye", "goodbye", "see you"]:
            return self.conversation_bank.bye_handler.get_goodbye()
        elif "good" in user_input:
            return self.conversation_bank.good_responses.get_response()
        elif "bad" in user_input:
            return self.conversation_bank.bad_responses.get_response()
        elif user_input.startswith("!suggestion"):
            # Handle suggestion submission
            suggestion = user_input.replace("!suggestion", "").strip()
            if suggestion:
                self.save_suggestion(suggestion)
                return "Thank you for your suggestion! We'll review it shortly."
            else:
                return self.conversation_bank.clarification_handler.get_clarification()
        else:
            return self.conversation_bank.clarification_handler.get_clarification()

    def save_suggestion(self, suggestion: str):
        """
        Saves the user's suggestion to a JSON file with a timestamp.
        
        Parameters:
            suggestion (str): The suggestion message from the user.
        """
        suggestion_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "suggestion": suggestion
        }
        try:
            with open("suggestions.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(suggestion_data) + "\n")
        except Exception as e:
            print(f"Error saving suggestion: {e}")
