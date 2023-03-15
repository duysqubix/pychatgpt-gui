import PySimpleGUI as sg

general_chat_layout = [
    [
        sg.Multiline("", key="gc_input_context", size=(50, 50)),
        sg.Multiline(
            key="gc_chat_log",
            size=(50, 50),
            autoscroll=True,
            disabled=True,
            reroute_stdout=True,
            reroute_stderr=False,
            write_only=True,
        ),
    ],
    [sg.Button("Submit", key="gc_button"), sg.Button("Clear", key="gc_button_clear")],
]

email_writer_layout = [
    [
        sg.Multiline(
            "Dear Friend, how are you?", key="ew_input_context", size=(50, 50)
        ),
        sg.Multiline(
            key="ew_chat_log",
            size=(50, 50),
            autoscroll=True,
            disabled=True,
            # echo_stdout_stderr=True,
            reroute_stdout=True,
            reroute_stderr=False,
            write_only=True,
        ),
        sg.Multiline(
            (
                "You are a professional email writer designed to revise the emails you receieve as input. "
                + "Be courteous, professional, and friendly in your responses. Be sure to only provide factual "
                + "information and refrain from using filler words that would make you sound unprofessional"
            ),
            key="ew_system_prompt",
            size=(50, 50),
        ),
    ],
    [sg.Button("Submit", key="ew_button"), sg.Button("Clear", key="ew_button_clear")],
]
linkedin_post_writer = [[sg.T("This is inside Tab2")], [sg.In(key="in")]]


main_layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("General Chat", general_chat_layout, key="Tab_General_Chat"),
                    sg.Tab("Email Writer", email_writer_layout, key="Tab_Email_Writer"),
                    sg.Tab(
                        "LinkedIn Post", linkedin_post_writer, key="Tab_Post_Helper"
                    ),
                ]
            ],
            key="Tabs",
        ),
    ],
]
