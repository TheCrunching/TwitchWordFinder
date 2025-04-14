#!/usr/bin/env python3
"""Twitch chat word finder!
"""
from twitch_chat_irc import twitch_chat_irc # Import Module

Word = ""
connection = twitch_chat_irc.TwitchChatIRC() # Start connection
Channel = "mud_flaps123"
def is_word(message):
    """Check if user commented word.

    Args:
        message (_type_): The message object passed from listen().
    """
    if message['message'].lower() == Word:
        print(f"User {message['display-name']} guessed '{Word}'")

def start():
    global Word
    Word = input("Please input word: ").lower()
    connection.listen(Channel, on_message=is_word)

if __name__ == "__main__":
    start()
