import openai
import os

from pathlib import Path

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    cwd = Path.cwd().absolute()
    with open((cwd / ".apikey"), "r") as f:
        API_KEY = f.read().strip()

openai.api_key = API_KEY


class ChatMessage:
    __name__ = ""

    def __init__(self, content=""):
        self.role = self.__name__
        self.content = content

    def extend(self, content):
        self.content += content

    def gen_param(self):
        return {"role": self.role, "content": self.content}


class SystemMessage(ChatMessage):
    __name__ = "system"


class AssistantMessage(ChatMessage):
    __name__ = "assistant"


class UserMessage(ChatMessage):
    __name__ = "user"


class ChatPacket:
    __model__ = "gpt-3.5-turbo"

    def __init__(self):
        self.messages = []

    def add_msg(self, msg: ChatMessage):
        self.messages.append(msg)

    def __call__(self):
        messages = [x.gen_param() for x in self.messages]
        return {"model": self.__model__, "stream": True, "messages": messages}


class Chat:
    def __init__(self, system_message=""):
        self.packet = ChatPacket()
        self.packet.add_msg(SystemMessage(system_message))

        self.setup()

    def setup(self):
        pass

    def ask(self, msg, window=None):
        msg = msg.strip()
        self.packet.add_msg(UserMessage(msg))

        resp = openai.ChatCompletion.create(**self.packet())

        # message_entry = {"role": "", "content": ""}
        assistant = AssistantMessage()

        for chunk in resp:
            delta = chunk["choices"][0]["delta"]

            content = delta.get("content")
            if content:
                assistant.extend(content)
                print(content, end="", flush=True)
                if window:
                    window.Refresh()
        self.packet.add_msg(assistant)


class EmailRevisor(Chat):
    def setup(self):
        pass


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
