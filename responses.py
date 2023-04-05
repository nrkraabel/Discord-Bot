import random
def handle_response(message) -> str:
    process_message = message.lower()

    if process_message == 'hello':
        return 'Hello there!'
    
    if process_message == 'roll':
        return str(random.randint(1,6))
    
    if process_message == 'help':
        return '`Help info: this should be info on how to use the bot but I am lazy.`'
    