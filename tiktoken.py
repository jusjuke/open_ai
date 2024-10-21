import tiktoken

enc = tiktoken.get_encoding("gpt2")
assert enc.decode(enc.encode("Hello, world!")) == "Hello, world!"

enc = tiktoken.encoding_for_model("text-davinci-003")