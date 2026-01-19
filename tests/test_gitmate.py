from gitmate.message_generator import generate_smart_message

def test_message_generator():
    msg = generate_smart_message()
    assert isinstance(msg, str)
