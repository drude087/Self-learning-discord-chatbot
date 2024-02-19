# Self-learning-discord-chatbot
This Discord chat bot is designed to provide intelligent responses to user queries and learn from interactions. It leverages a combination of natural language processing techniques and a simple question-answer storage system to engage in meaningful conversations with users.

The bot employs the difflib library to find the closest match to user queries. If a matching question is found in its knowledge base, it retrieves the corresponding answer.

If the bot encounters a question it doesn't recognize, it prompts the user to provide an explanation along with the answer. It then stores this new question-answer pair for future reference, enhancing its knowledge base over time.

The bot interacts with users in a conversational manner, prompting them for clarification when needed and expressing gratitude for new information.
  
The bot maintains a JSON file as its knowledge base, allowing it to retain learned information across sessions.

The bot can be cutomized to perform various tasks
you can message or train the model in private messages not in the server chat.
