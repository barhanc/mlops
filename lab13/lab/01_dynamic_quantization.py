import time
from openai import OpenAI


def get_response(msg: str, client: OpenAI) -> str:
    chat_response = client.chat.completions.create(
        model="",  # use the default server model
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How important is LLMOps on scale 0-10? "},
        ],
        max_completion_tokens=1000,
        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    )
    content = chat_response.choices[0].message.content.strip()  # type:ignore
    return content


if __name__ == "__main__":
    messages = [
        "How important is LLMOps on scale 0-10?",
        "What is your favourite color?",
        "Explain backpropagation algorithm in simple terms",
        "How many r's are in 'strawberry'?",
        "What year it is?",
        "What is 2+2?",
        "What is 783562783+8124092?",
        "Explain monads like I'm 5",
        "Do you like your job?",
        "How many messages are there?",
    ]
    client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1")

    t = time.perf_counter()
    for msg in messages:
        get_response(msg, client)
    t = time.perf_counter() - t

    print(f"Total response time: {t:.2f}s")
    print(f"Avg.  response time: {t:.2f}s")
