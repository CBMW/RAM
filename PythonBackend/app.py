# PythonBackend/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from ConversationHandler import ConversationHandler

app = FastAPI()

# Initialize the conversation handler
conversation_handler = ConversationHandler()

class Message(BaseModel):
    user_input: str

@app.post("/get-response/")
async def get_response(message: Message):
    """
    Endpoint to handle user messages and return appropriate bot responses.
    
    Parameters:
        message (Message): The user input message.
    
    Returns:
        dict: A dictionary containing the bot's response.
    """
    user_input = message.user_input

    # Get the response from ConversationHandler
    bot_response = conversation_handler.get_response(user_input)

    return {"response": bot_response}
