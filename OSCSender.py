import argparse
import random
import time
import sys

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)
    client.send_message("/avatar/parameters/KAT_Visible", True)
    client.send_message("/avatar/parameters/KAT_Pointer", 255)

    precision = 127
    #precision = 100

    for i in range(32):
        time.sleep(0.25)
        client.send_message("/avatar/parameters/KAT_Pointer", i + 1)
        client.send_message("/avatar/parameters/KAT_CharSync0", (i*4 + 1)/precision)
        client.send_message("/avatar/parameters/KAT_CharSync1", (i*4 + 2)/precision)
        client.send_message("/avatar/parameters/KAT_CharSync2", (i*4 + 3)/precision)
        client.send_message("/avatar/parameters/KAT_CharSync3", (i*4 + 4)/precision)
    
