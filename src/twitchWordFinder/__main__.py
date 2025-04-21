#!/usr/bin/env python3
"""Twitch chat word finder!
"""

import argparse
from twitch_chat_irc import twitch_chat_irc # Import Module

__version__ = "1.1.0"

parser = argparse.ArgumentParser(
    prog="Twitch Chat Word Finder",
    description="Finds a word in twitch chat.",
    epilog="This is here for no reason.")

parser.add_argument("-c", "--channel", default=None, description="The channel name.")
parser.add_argument("-w", "--word", default=None, description="The word that should be found in chat.")
parser.add_argument("-v", "--version", action="version", version=__version__, description="Prints the applications version.")

args = parser.parse_args()

connection = twitch_chat_irc.TwitchChatIRC() # Start connection

if args.channel is None:
    channel = input("Please input the channel you would like to find a word in: ")
else:
    channel = args.channel

if args.word is None:
    word = input("Please input the word you would like to find: ")# Ask user for word
else:
    word = args.word

def is_word(message):
    """Check if user commented word.
    Args:
        message (_type_): The message object passed from listen().
    """

    if word.lower() in message['message'].lower().split():
        print(f"User {message['display-name']} guessed '{word}'")

def main():
    """Main function
    """

    connection.listen(channel, on_message=is_word)# Start listening to chat

if __name__ == "__main__":
    main()
