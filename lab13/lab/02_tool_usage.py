import json
import polars as pl

from typing import Callable
from openai import OpenAI


def make_llm_request(prompt: str) -> str:
    client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1")

    messages = [
        {"role": "developer", "content": "You are a data analysis assistant."},
        {"role": "user", "content": prompt},
    ]

    tool_definitions, tool_name_to_func = get_tool_definitions()

    for _ in range(10):
        response = client.chat.completions.create(
            model="",
            messages=messages,
            tools=tool_definitions,
            tool_choice="auto",
            max_completion_tokens=1000,
            extra_body={"chat_template_kwargs": {"enable_thinking": False}},
        )
        resp_message = response.choices[0].message
        messages.append(resp_message.model_dump())

        print(f"Generated message: {resp_message.model_dump()}")
        print()

        if resp_message.tool_calls:
            for tool_call in resp_message.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments)

                func = tool_name_to_func[func_name]
                func_result = func(**func_args)

                messages.append(
                    {
                        "role": "tool",
                        "content": json.dumps(func_result),
                        "tool_call_id": tool_call.id,
                    }
                )
        else:

            return resp_message.content

    last_response = resp_message.content
    return f"Could not resolve request, last response: {last_response}"


def get_tool_definitions() -> tuple[list[dict], dict[str, Callable]]:
    tool_definitions = [
        {
            "type": "function",
            "function": {
                "name": "read_remote_csv",
                "description": "Get a CSV file from a URL and return the data as a string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL to the .csv file.",
                        },
                    },
                    "required": ["url"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "read_remote_parquet",
                "description": "Get a Parquet file from a URL and return the data as a string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL to the .parquet file.",
                        },
                    },
                    "required": ["url"],
                },
            },
        },
    ]

    tool_name_to_callable = {
        "read_remote_csv": read_remote_csv_tool,
        "read_remote_parquet": read_remote_parquet_tool,
    }

    return tool_definitions, tool_name_to_callable


def read_remote_csv_tool(url: str) -> str:
    try:
        df = pl.scan_csv(url)
        return df.head(20).collect().to_pandas().to_markdown()
    except Exception as e:
        return f"Error reading CSV from {url}\n {e}"


def read_remote_parquet_tool(url: str) -> str:
    try:
        df = pl.scan_parquet(url)
        return df.head(20).collect().to_pandas().to_markdown()
    except Exception as e:
        return f"Error reading Parquet from {url}\n {e}"


if __name__ == "__main__":
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet"
    prompt = f"Can you look at the data at {url} and print the first three columns it contains?"
    response = make_llm_request(prompt)
    print("Response:\n", response)

    print()

    prompt = "What is the datetime of the first row in the provided data?"
    response = make_llm_request(prompt)
    print("Response:\n", response)

    print()

    prompt = "What are the data types of the columns in the provided data?"
    response = make_llm_request(prompt)
    print("Response:\n", response)
