from utils import BaseNode, debug, info, warn, error
from nodes.device_writer import OutputEvent
from evdev import ecodes as e


# If you want to intercept more keybords, add them here
# Get their names using "sudo lsusb" ou "sudo evtest"
# TODO?: Find a way to automatically do this
TARGET_DEVICES = [
    "CORSAIR CORSAIR K63 Wireless Mechanical Gaming Keyboard", 
    "CORSAIR CORSAIR K63 Wireless USB Receiver Keyboard", 
    "CORSAIR CORSAIR K63 Wireless USB Receiver", 
]


class BasicKeyboards(BaseNode):

    def __init__(self, core):
        super().__init__(core)

        for device in TARGET_DEVICES:
            core.register_listener(self, "DeviceReader:" + device, self.on_event)

    def on_event(self, topic_name, event):
        with OutputEvent(self.core) as eb:
            eb.forward(event.type, event.code, event.value)

def on_load(core):

    core.add_node(BasicKeyboards(core))
    core.require_device(TARGET_DEVICES)