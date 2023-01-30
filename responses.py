import random


def handle_response(message) -> str:
    p_message = message.lowe()

    if p_message == 'hello':
        return 'Hey there'

    if p_message == 'roll':
        return str(random.ranInt(1, 6))

    if p_message == '!help':
        return "This is help."

    return "I dont know what you said."
