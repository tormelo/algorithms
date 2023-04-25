import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "morango"

    with pytest.raises(TypeError):
        encrypt_message(2, message)
    assert encrypt_message(message, 10) == "ognarom"
    assert encrypt_message(message, 3) == "rom_ogna"
    assert encrypt_message(message, 4) == "ogn_arom"
