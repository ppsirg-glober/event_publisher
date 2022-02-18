from events_publisher import __version__
from events_publisher.broadcaster import EventBroadcaster


def test_version():
    assert __version__ == "0.1.0"


def test_event_broadcast():
    br = EventBroadcaster(topic="trial")
    br.send_dummy_events(100)
