import PySimpleGUI as sg

from layout import main_layout
from chatgpt import Chat
from datetime import datetime

window = sg.Window("PyChatGPT", main_layout)

chat_manager = {"email": None, "poster": None}


def process_email_writer(values):
    # chat_manager = {x: (None if x != "email" else x) for x in chat_manager.keys()}
    sys_message = window["ew_system_prompt"].get()
    if not chat_manager.get("email"):
        chat_manager["email"] = Chat(system_message=sys_message)

    input_context = window["ew_input_context"].get()

    if not input_context:
        return

    # print(datetime.now())
    chat_manager["email"].ask(msg=input_context, window=window)
    print("\n")


if __name__ == "__main__":
    sg.theme("Dark Blue 3")  # please make your windows colorful

    while True:  # Event Loop
        try:
            event, values = window.read(timeout=0.1)
            if event == "__TIMEOUT__":
                continue

            if "ew_" in event:
                process_email_writer(values)

            if event == sg.WIN_CLOSED or event == "Exit":
                break
        except:
            break

    window.close()
