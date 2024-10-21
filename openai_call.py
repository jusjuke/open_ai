import getpass

import openai


def complete(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ],
    )
    return response.choices[0].message.content

openai.api_key = getpass.getpass("Please enter your OpenAI Key:")
# Setup the article title
article = "What is data engineering?"
# Inject the article title into the base prompt
base_prompt = f'Write a numbered, hierarchical outline for an article on "{article}"\n\nHere is an example, of the structure:\n\n1. Introduction \n    a. Definition of digital marketing \n2. Types of Digital Marketing \n    a. Search Engine Optimization \n    b. Social Media Marketing \n    c. Content Marketing \n    d. Pay-Per-Click Advertising \n    e. Email Marketing \n3. Benefits of Digital Marketing \n    a. Cost-Effective \n    b. Targeted Audience \n    c. Measurable Results \n    d. Increased Reach \n\n----\n'


result = complete(base_prompt)
print(result)
complete("is this working?")