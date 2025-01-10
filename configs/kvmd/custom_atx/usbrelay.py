import sys
import serial


def send_command(device_info, channel, onoff):
    if channel not in (1, 2) or onoff not in (0, 1):
        return
    with serial.Serial(device_info, 9600) as ser:
        data_bytes = bytes([0xA0, channel, onoff, 0xA0 + channel + onoff])
        ser.write(data_bytes)


def main():
    if len(sys.argv) != 4:
        print("Usage:\n" "\tpython script.py id on|off")
        return

    try:
        device_info = sys.argv[1]
        id = int(sys.argv[2])
        if sys.argv[3].lower() == "on":
            onoff = 1
        elif sys.argv[3].lower() == "off":
            onoff = 0
        else:
            raise ValueError
    except ValueError:
        print("Invalid command, use 'on' or 'off'")
        return

    send_command(device_info, id, onoff)
    print(f"Sent command to channel {id}: {'ON' if onoff else 'OFF'}")


if __name__ == "__main__":
    main()
