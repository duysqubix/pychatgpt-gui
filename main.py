import PySimpleGUI as sg
import sys

from layout import main_layout
from chatgpt import EmailRevisor
from datetime import datetime

window = sg.Window("PyChatGPT", main_layout)

chat_manager = {"email": None, "poster": None}


def process_email_writer(event, values):
    if event is None:
        return

    if event == "ew_button_clear":
        window["ew_chat_log"].update("")
        chat_manager["email"] = None
        return

    sys_message = window["ew_system_prompt"].get()
    if not chat_manager.get("email"):
        chat_manager["email"] = EmailRevisor(system_message=sys_message)

    input_context = window["ew_input_context"].get()

    if not input_context:
        return

    print(datetime.now().ctime())
    chat_manager["email"].ask(msg=input_context, window=window)
    print("\n")


if __name__ == "__main__":
    # sg.theme("Dark Blue 3")  # please make your windows colorful

    while True:  # Event Loop
        try:
            event, values = window.read(timeout=0.1)
            if event == "__TIMEOUT__":
                continue
            if "ew_" in event:
                process_email_writer(event, values)
        except KeyboardInterrupt as e:
            break

    window.close()
