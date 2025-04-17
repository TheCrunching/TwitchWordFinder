#!/usr/bin/env python3
"""Twitch chat word finder!
"""

from twitch_chat_irc import twitch_chat_irc # Import Module

connection = twitch_chat_irc.TwitchChatIRC() # Start connection

channel = input("Please input the channel you would like to find a word in: ")
word = input("Please input the word you would like to find: ")# Ask user for word

def is_word(message):
    """Check if user commented word.
    Args:
        message (_type_): The message object passed from listen().
    """

    if word in message['message'].lower().split():
        print(f"User {message['display-name']} guessed '{word}'")

def main():
    """Main function
    """

    connection.listen(channel, on_message=is_word)# Start connection to chat

if __name__ == "__main__":
    main()
