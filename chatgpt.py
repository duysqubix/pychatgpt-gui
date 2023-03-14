import openai
import os

from pathlib import Path

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    cwd = Path.cwd().absolute()
    with open((cwd / ".apikey"), "r") as f:
        API_KEY = f.read().strip()

openai.api_key = API_KEY


class Chat:
    def __init__(self, system_message="", model="gpt-3.5-turbo"):
        self.messages = [{"role": "system", "content": system_message}]
        self.params = {"model": model, "stream": True}

    def ask(self, msg, window=None):
        msg = msg.strip()
        message = {"role": "user", "content": msg}
        self.messages.append(message)

        resp = openai.ChatCompletion.create(messages=self.messages, **self.params)

        message_entry = {"role": "", "content": ""}
        for chunk in resp:
            delta = chunk["choices"][0]["delta"]

            role = delta.get("role")
            if role:
                message_entry["role"] = role

            content = delta.get("content")
            if content:
                message_entry["content"] += content
                print(content, end="", flush=True)
                if window:
                    window.Refresh()
        self.messages.append(message_entry)


if __name__ == "__main__":
    chat = Chat(
        "You are a professional email writer in charge of revising current emails"
    )
    chat.pre_message_insert(
        "Please generate me a professional alternative to the following email."
    )
    chat.ask(
        """
             Dear Fred,
             
             Thank you so much of thinking of me the other day. It meant a lot that you told me that I could fart so loud.
            """
    )
