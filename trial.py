# works with both python 2 and 3
from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "naimahassan"
        self.api_key = "a0eac5d57c6d7988203f5c1c18a84d9629a5494957df435b0a7ab439daa32586"
    

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+254798355300"]

            # Set your message
            message = "testing tesing i hope its working";

            # Set your shortCode or senderId
            # sender =  "+254700860970"
            try:
                # Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()