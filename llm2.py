


from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

# Initiating the chat model with API keyß
chat = ChatOpenAI(api_key="")

# Defines a context and query using SystemMessage and HumanMessage
messages = [
    SystemMessage(content="You are a math tutor who provides answers to math questions."),
    HumanMessage(content="What is the square of 2?"),
]
 
response = chat.invoke(messages)
print(response.content)