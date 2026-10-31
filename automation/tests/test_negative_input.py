import pytest

@pytest.mark.parametrize("value", ['Abc', '@!~&', 9.99,
                                   None, True, False, [], {},
                                   "001.0", "Ω", "你好"])
def test_pwm_incorrect_input(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "ERROR"
    assert r["code"] == "INVALID_VALUE"


@pytest.mark.parametrize("value", ["", "   ", "\n", "\t"])
def test_pwm_unknown_command(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "ERROR"
    assert r["code"] == "UNKNOWN_COMMAND"
    