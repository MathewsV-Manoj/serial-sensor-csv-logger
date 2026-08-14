# Serial Sensor CSV Logger

A Python utility that records newline-separated readings from a microcontroller serial port into a CSV file.

## Setup

Install the only dependency:

    pip install pyserial

Then run it with your port name:

    python sensor_logger.py COM3 --baud 9600 --output readings.csv

The logger adds an ISO timestamp to each received line and flushes after every row so the data is still useful if a session is interrupted.