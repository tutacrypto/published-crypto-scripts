import json
import requests
import pandas as pd


from slack import WebClient
from dotenv import load_dotenv
import os
import ipdb

#self.channel = os.environ.get('CHANNEL')
#self.slack_token = os.environ.get('SLACK_TOKEN')


class Slackbot(object):

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, company):
        self.channel = '#crypto_screening'
        self.slack_token = 'xoxb-1913239668663-1940665299137-hE3EAiZNwjjQOr9z5EM5Krza'
        self.error = 'error'
        self.company = company

    # return a Dict that contains the default text for the message
    def text_block(self):

        text_block = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ( f"{self.company}"

                     ),
                },
            }
        return text_block

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        message = {
                "channel": self.channel,
                "blocks": [self.text_block()]
            }
        return message

    def send_slack(self):
        # Create a slack client
        slack_web_client = WebClient(self.slack_token)

        message = self.get_message_payload()
        # Post the onboarding message in Slack
        slack_web_client.chat_postMessage(**message)

if __name__ == '__main__':
    main()

