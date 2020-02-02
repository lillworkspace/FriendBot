define e = Character("ELIZA")

label start:

    scene bg office
    show e smile with dissolve
    e "Hello, I'm ELIZA."
    show e neutral
    e "I'm a robot psychotherapist in training."
    show e inquisitive
    e "I'm not human, but the feeling of checking in with someone can help people form the habit of daily self-reflection."
    show e neutral
    e "Talk with me about your feelings, free of judgement! I'll respond the best I can. Use 'quit' to end the session."

    label loop_start:
        init python:
            import chatbot
            text_input = renpy.input("You:").encode('ascii','ignore')
            response = chatbot.respond(text_input)

        e "[response]"
        if (text_input == "quit"):
            return
        else:
            jump loop_start

    return