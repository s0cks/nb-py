import fonts
import marquee
from collections import namedtuple

Rectangle = namedtuple("Rectangle", "bottom left right top")
EMPTY_RECTANGLE = Rectangle(0, 0, 0, 0)

DEFAULT_ZONE_VOLUME = 0x04


class Zone(object):
    def __init__(self, name, zid, bounds=EMPTY_RECTANGLE, volume=DEFAULT_ZONE_VOLUME, font=fonts.MONOSPACE_7, message_settings=marquee.DEFAULT_MESSAGE_SETTINGS, scroll_settings=marquee.DEFAULT_SCROLL_SETTINGS):
        self.name = name
        self.zone_id = zid
        self.bounds = bounds
        self.volume = volume
        self.font = font
        self.message_settings = message_settings
        self.scroller_settings = scroll_settings

    def get_name(self):
        return self.name

    def get_zone_id(self):
        return self.zone_id

    def get_bounds(self):
        return self.bounds

    def get_volume(self):
        return self.volume

    def get_font(self):
        return self.font

    def get_message_body(self):
        return self.message_settings.body

    def get_message_delay(self):
        return self.message_settings.delay

    def get_scrolling_speed(self):
        return self.scroller_settings.speed

    def is_scrolling(self):
        return self.scroller_settings.is_scrolling