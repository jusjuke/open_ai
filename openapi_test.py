
import getpass

from openai import OpenAI

key = getpass.getpass("Enter key")
client = OpenAI(api_key=key)
for model in client.models.list():
    print(model)
