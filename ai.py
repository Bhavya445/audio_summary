import cohere

class Chatbot:
    def __init__(self):
        api_key = 'tzfbnxX1Qt4F3UFelwG9pimwVTON7hxcyIC2hPNm'
        self.co = cohere.Client(api_key)
    def get_response(self, user_input):
        model_id = 'command-xlarge-nightly'

        # Generate text
        response = self.co.generate(
            model=model_id,
            prompt=user_input,
            max_tokens=50
        )

        # Print the generated joke
        fr = response.generations[0].text.strip()
        return fr

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("write a joke abt birds")
    print(response)


