#!/usr/bin/env python3
"""Twitch chat word finder!
"""

import warnings
import sys
from twitch_chat_irc import twitch_chat_irc # Import Module

connection = twitch_chat_irc.TwitchChatIRC() # Start connection
Channel = "mud_flaps123"
def is_word(message):
    """Check if user commented word.

    Args:
        message (_type_): The message object passed from listen().
    """
    if Word in message['message'].lower().split():
        print(f"User {message['display-name']} guessed '{Word}'")

def start():
    """Function to init the program.
    """
    if Word is None:
        warnings.warn("Word must not be equal to 'None'.")
        sys.exit(1)
    connection.listen(Channel, on_message=is_word)# Start connection to chat

if __name__ == "__main__":
    Word = input("Please input the word you would like to find: ")# Ask user for word
    start()# Call start when script is loaded
else:
    Word = None# Define word just in case
