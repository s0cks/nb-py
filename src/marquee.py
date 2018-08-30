from collections import namedtuple

SCROLL_SPEED_SLOW = 0x01
SCROLL_SPEED_MEDIUM = 0x02
SCROLL_SPEED_FAST = 0x03

DEFAULT_MESSAGE_DELAY = 1000

ScrollSettings = namedtuple("ScrollSettings", "speed is_scrolling")
MessageSettings = namedtuple("MessageSettings", "delay body")

DEFAULT_SCROLL_SETTINGS = ScrollSettings(SCROLL_SPEED_MEDIUM, True)
DEFAULT_MESSAGE_SETTINGS = MessageSettings(DEFAULT_MESSAGE_DELAY, "Hello World")
