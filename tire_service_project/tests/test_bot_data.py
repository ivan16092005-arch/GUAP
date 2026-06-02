def test_message_format():
    message = "Иван;Замена шин;15.06.2026"

    parts = message.split(";")

    assert len(parts) == 3