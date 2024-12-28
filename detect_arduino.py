import sys
import serial.tools.list_ports


def detect_arduino():
    ports = serial.tools.list_ports.comports()
    arduino_ports = [
        p.device
        for p in ports
        if 'Arduino' in p.description or 'CH340' in p.description  # CH340 is common for clones
    ]

    if not arduino_ports:
        print("No Arduino found")
        return None
    elif len(arduino_ports) > 1:
        print("Multiple Arduinos found - using the first one")

    print(f"Arduino connected on port: {arduino_ports[0]}")
    return arduino_ports[0]


if __name__ == '__main__':
    detect_arduino()
