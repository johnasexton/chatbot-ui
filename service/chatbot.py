import requests

class Chatbot:
    def __init__(self):
        # Load properties from application.properties
        self.endpoint = "https://your-chatbot-endpoint"  # Replace with actual endpoint

    def get_response(self, user_input):
        # Logic to send user_input to Dialogflow and get response
        response = requests.post(self.endpoint, json={'message': user_input})
        return response.json().get('response', 'No response from chatbot')
