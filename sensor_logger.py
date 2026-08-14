import argparse
import csv
from datetime import datetime

import serial


def main():
    parser = argparse.ArgumentParser(description="Log newline-separated serial sensor data to CSV.")
    parser.add_argument("port", help="Serial port, for example COM3 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--output", default="sensor_log.csv")
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=1) as device, open(args.output, "a", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        if output.tell() == 0:
            writer.writerow(["timestamp", "reading"])
        print("Logging. Press Ctrl+C to stop.")
        try:
            while True:
                reading = device.readline().decode("utf-8", errors="replace").strip()
                if reading:
                    writer.writerow([datetime.now().isoformat(timespec="seconds"), reading])
                    output.flush()
                    print(reading)
        except KeyboardInterrupt:
            print("Log saved to", args.output)


if __name__ == "__main__":
    main()