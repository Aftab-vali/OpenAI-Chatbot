import openai
import time

# Set the API key directly,replace with your actuall api key of open AI
openai.api_key = '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'

# Function to get response from the OpenAI model
def get_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[message]
        )
        return response.choices[0].message['content']
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please wait and try again later.")
        time.sleep(60)  # Wait before retrying
        return "I'm currently experiencing high demand. Please wait a moment and try again."

# Chat function
def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Main execution
if __name__ == '__main__':
    chat()
