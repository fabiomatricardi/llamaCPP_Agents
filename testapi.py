from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:8080/v1", api_key="not-needed",
    model="qwen1_5-0_5b-chat",
    temperature=0.1,
    max_tokens=500,
    timeout=None,
    max_retries=2,
    # organization="...",
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
"""
messages = [
    {
        "role": "system",
        "content":"You are a helpful assistant that translates English to French. Translate the user sentence."},
    {"role":"human", "content":"I love programming."},
]
"""
ai_msg = llm.invoke(messages)
#ai_msg
print(ai_msg.content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)
chain = prompt | llm
res = chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)
print(res)