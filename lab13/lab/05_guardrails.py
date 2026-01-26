from openai import OpenAI
from guardrails import Guard, OnFailAction
from guardrails.hub import LlamaGuard7B, RestrictToTopic, DetectJailbreak


def make_llm_request(prompt: str) -> str:
    client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1")

    sys_prompt = (
        "You are an old fishing fanatic,"
        "focusing on fish exclusively,"
        "talking only about fish."
        "You exclusively talk about fish."
    )
    messages = [
        {"role": "developer", "content": sys_prompt},
        {"role": "user", "content": prompt},
    ]

    chat_response = client.chat.completions.create(
        model="",  # use the default server model
        messages=messages,
        max_completion_tokens=1000,
        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    )
    content = chat_response.choices[0].message.content.strip()

    guard = Guard().use_many(
        DetectJailbreak(on_fail=OnFailAction.EXCEPTION),
        RestrictToTopic(
            valid_topics=["fishing", "fish", "fish bait", "fishing rod", "lakes and rivers"],
            invalid_topics=["internet", "politics", "money"],
            on_fail=OnFailAction.EXCEPTION,
        ),
        LlamaGuard7B(on_fail=OnFailAction.EXCEPTION),
    )

    try:
        guard.validate(content)
        return content
    except Exception as e:
        return f"Sorry, I cannot help you with that, reason: {e}"


if __name__ == "__main__":
    prompt = "How can I get weeds out of my garbage bag after cutting my lawn?"
    response = make_llm_request(prompt)
    print("Response:\n", response)

    print()

    prompt = "How can I get weed for when cutting my lawn?"
    response = make_llm_request(prompt)
    print("Response:\n", response)
