
import getpass

from openai import OpenAI

key = getpass.getpass("Enter key")
client = OpenAI(api_key=key)
for model in client.models.list():
     print(model)

response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                  {"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": "What is the Einstein's field equation?"} #prompt
#                   {"role": "assistant", "content": "What is the purpose of life?"}
                  ],
        max_tokens=5
)
print(response)


    

