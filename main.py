import random
import time
import socket
from threading import Thread


"""
    TODO:
    1- Create an appropriate data container to store sensor data from the input file, adding an extra field for sensor 
    value
    2- Populate the data container using the data in the input file, initializing sensor value as empty
    Reminder: the input file is in the following format:
        AreaID(4dig),UnitID(3dig),SensorID(1dig),xCoordinate(double),yCoordinate(double)
    3- Use a separate thread for every unit to handle sending data every fixed interval as long as the script is running
    4- Run the function random_update_data() to randomly update 1/4 of the sensor values every fixed interval
    5- Devise some performance tests using timers and try them out by tweaking the fixed intervals to push the test to 
    its maximum acceptable response time 
"""


def __init__(self):
    """A method for initialization purposes."""
    pass


def read_parse_file():
    """A method to read the input file and parse its contents, and populate the data containers with them"""
    pass


def display_sensor():
    """A method to print sensor data"""
    pass


def distribute_to_threads():
    """A method to create threads for every unit, rerouting the thread to use send_sensor_data()"""
    pass


def send_sensor_data():
    """ A method used to compile and send the sensor data as a JSON object to the server """
    pass


def random_update_data():
    """ A method to randomly update 1/4th of the sensor values in the data container every fixed interval"""
    pass


def to_http_string(value: str) -> str:
    """A method to transform sensor values into an HTTP string"""
    http_string = "" + value + ""
    return http_string


def main():
    """The flow of code is described in this method"""
    read_parse_file()
    distribute_to_threads()
    random_update_data()
    pass


if __name__ == '__main__':
    main()



