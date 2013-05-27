from . import bridge
from . import effects

def connect(address='192.168.1.100', port=50000):
    return bridge.Bridge(address, port)
