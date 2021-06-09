import enum
import random
import time
import requests
from requests.structures import CaseInsensitiveDict
from threading import Thread


class Sensor:
    """
        TODO:
        1- Create an appropriate data container to store sensor data from the input file, adding an extra field for
        sensor value
        2- Populate the data container using the data in the input file, initializing sensor value as empty
        Reminder: the input file is in the following format:
            AreaID(4dig),UnitID(3dig),SensorID(1dig),xCoordinate(double),yCoordinate(double)
        3- Use a separate thread for every unit to handle sending data every fixed interval as long as the script is
        running
        4- Run the function random_update_data() to randomly update 1/4 of the sensor values every fixed interval
        5- Devise some performance tests using timers and try them out by tweaking the fixed intervals to push the test
        to
        its maximum acceptable response time
    """

    def __init__(self, area: int, unit: int, id: int, xcoor: float, ycoor: float, value: bool):
        """A method for initialization purposes."""

        self.area = area
        self.unit = unit
        self.id = id
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.value = value

    def display_sensor(self):
        """A method to print sensor data"""
        str_id = self.get_str_id()
        print("Sensor ID: " + str_id + " with Coordinates (" + str(self.xcoor) + ", " + str(self.ycoor) + ")")

    def send_sensor_data(self):
        """ A method used to compile and send the sensor data as a JSON object to the server """
        str_id = self.get_str_id()
        print(str_id + " with value:" + str(self.value))
        url = "http://localhost:3000/update"
        data = \
            {"id": str_id,
             "empty": self.value}
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        # resp = requests.patch(url, headers=headers, data=data)
        # print("Sending Sensor ID: " + str_id + " STATUS: " + str(resp.status_code))

    def random_update_data(self):
        """ A method to randomly update sensor value at a chance of 1/4"""
        chance = random.randint(1, 100)
        if chance <= 25:
            self.value = not self.value

    def get_str_id(self) -> str:
        """A method to transform sensor values into an HTTP string"""
        str_id = ""
        area = self.area
        unit = self.unit
        while (area / 1000) < 1:
            str_id += "0"
            area = area * 10
        str_id += str(self.area)
        while (unit / 100) < 1:
            str_id += "0"
            unit = unit * 10
        str_id += str(self.unit) + str(self.id)
        return str_id


class RequestState(enum.Enum):
    PACKET_LOST = 0
    PACKET_SENT = 1


""" List of all Sensors & threads being employed"""
sensors = list()
threads = list()


def read_parse_file(filename: str):
    """ A method to read an input and parse its contents to appropriate types"""
    f = open(filename + ".txt", "r")
    for line in f:
        if not line.startswith("Area"):
            line_strips = line.strip().split(',')
            sensor = Sensor(int(line_strips[0]), int(line_strips[1]), int(line_strips[2]), float(line_strips[3]),
                            float(line_strips[4]), False)
            sensors.append(sensor)
    return None


def setup_sending_threads():
    """A method to create threads for every unit, routing the thread to use unit_sender() to dispatch a unit to the
    server separately"""

    current_area_id = 1
    current_unit_id = 1
    unit = list()
    while True:
        for sensor in sensors:
            sensor.send_sensor_data()
            sensor.random_update_data()


def unit_sender(*args):
    """ Threaded work: A method to dispatch each each sensor to be sent to the server"""
    unit = args[0]
    print("Sent")
    for s in unit:
        s.display_sensor()
    print("Received")
    while True:
        time.sleep(random.uniform(0, 1.00))
        for sensor in unit:
            sensor.display_sensor()
            sensor.random_update_data()
            sensor.send_sensor_data()


def manage_threads():
    """ A method to start & manage all threads"""
    for thread in threads:
        thread.start()


def main():
    """The flow of code is described in this method"""
    # filename = input("Enter filename, without the .txt:")
    read_parse_file("input")
    setup_sending_threads()
    print("Number of Sensors: " + str(len(sensors)) + "  & Number of threads:" + str(len(threads)))
    #manage_threads()


if __name__ == '__main__':
    main()
