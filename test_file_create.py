import openai

client = openai.OpenAI()

file = client.files.create(file=open("requirements.txt", "rb"), purpose="assistants")
