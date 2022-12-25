import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "Fortnite battle pass"

    if p_message == 'roll':
        return str(random.randint(1, 100))

    if p_message == '!help':
        return "´No´"

    else:
        return "idk what you said lmfao"