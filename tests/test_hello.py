from satfootprint import hello


def test_hello_returns_greeting() -> None:
    assert hello() == "Hello from satfootprint!"
