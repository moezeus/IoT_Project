import time
import requests
import math
import random

TOKEN = "BBFF-NDkvRg3WNX0bRRk9YW21MEYz61U8Lu"  # Put your TOKEN here
DEVICE_LABEL = "mentor_ham"  # Put your device label here 
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
VARIABLE_LABEL_2 = "humidity"  # Put your second variable label here
VARIABLE_LABEL_3 = "position"  # Put your second variable label here


def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    value_1 = random.randint(-10, 50)
    value_2 = random.randint(0, 85)

    # Creates a random gps coordinates
    lat = random.randrange(34, 36, 1) + \
        random.randrange(1, 1000, 1) / 1000.0
    lng = random.randrange(-83, -87, -1) + \
        random.randrange(1, 1000, 1) / 1000.0
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}

    return payload

def get_request():
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url1 = "{}/api/v1.6/devices/{}/{}/lv".format(url, DEVICE_LABEL, VARIABLE_LABEL_1)
    url2 = "{}/api/v1.6/devices/{}/{}/lv".format(url, DEVICE_LABEL, VARIABLE_LABEL_2)
    url3 = "{}/api/v1.6/devices/{}/{}/lv".format(url, DEVICE_LABEL, VARIABLE_LABEL_3)
    headers = {"X-Auth-Token": TOKEN}

    # Makes the HTTP requests
    status = [400,400,400]
    attempts = 0
    while status[0] >= 400 and attempts <= 5:
        req1 = requests.get(url=url1, headers=headers)
        req2 = requests.get(url=url2, headers=headers)
        req3 = requests.get(url=url3, headers=headers)
        status = [req1.status_code,req2.status_code,req3.status_code]
        attempts += 1
        time.sleep(1)

    # Processes results
    print(status)
    print(req1.json(),req2.json(),req3.json())
    if status[0] >= 400:
        print("[ERROR] Could not get data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to get data")
    # post_request(payload)
    get_request()
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)