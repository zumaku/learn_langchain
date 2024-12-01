from langchain_ollama import ChatOllama

# Inisiasi
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    
    # other params...
    # format="json",
)

# Set message
messages = [
    ("system", "You are a helpful translator. Translate the user sentence to Indonesian."),
    ("human", "I love programming."),
]

# --------------------------------------

# [Direct Response]
llm_respons = llm.invoke(messages)
print(llm_respons)

# --------------------------------------

# [Sream Response]
# for chunk in llm.stream(messages):
#     print(chunk)

# --------------------------------------

# [Another Stream Response]
# stream = llm.stream(messages)
# full = next(stream)
# for chunk in stream:
#     full += chunk
#     # print(full)
#     print(full.content)

# --------------------------------------

# [JSON mode Response]
# Tambahkan parameter format denagn value json pada ChatOllama
# print(llm.invoke(messages).content)