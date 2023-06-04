import serial
import time

# Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.G9D'  # Bluetooth shield HC-06

if __name__ == '__main__':
    print("Connecting to serial port ...")
    ser = serial.Serial(serial_port, serial_speed, timeout=1)
    print("Waiting for connection ...")

    connected = False
    while not connected:
        if ser.in_waiting:
            print("Connection established!")
            connected = True
        else:
            time.sleep(1)

    while connected :

        data = ser.readline()

        if data:
            print("Arduino says: %s" % data.decode())

        time.sleep(1)

    time.sleep(4)
    print("Finished program and closed connection!")