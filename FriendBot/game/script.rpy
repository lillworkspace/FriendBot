define fb = Character("FriendBot")

label start:

    scene bg outside
    show s happy with dissolve
    fb "Hi, I'm FriendBot!"
    show c neutral
    fb "I am a chat bot that makes keeping a digital journal feel more interactive."
    fb "This chat bot uses the feeling of checking in with someone to help people form the habit of daily self-reflection."
    fb "Type and I'll respond the best I can. Use 'quit' to end the session."

    label loop_start:

        python:
            import chatbot
            text_input = renpy.input("You:").encode('ascii','ignore')
            response = chatbot.check_for_greeting(text_input)

        fb "[response]"
        if (text_input == "quit"):
            return
        else:
            jump loop_start

    return