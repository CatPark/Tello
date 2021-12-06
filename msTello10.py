from djitellopy import tello
from time import sleep
import cv2

print("Hello tello")

mytello = tello.Tello()

mytello.connect()
print(f"Tello battery: {mytello.get_battery()}")
print(f"Tello current state:{mytello.get_current_state()}")
print(f"Tello TOF: {mytello.get_distance_tof()}")
print(f"Tello flight time: {mytello.get_flight_time()}")
print(f"Tello height: {mytello.get_height()}")

mytello.takeoff()
print(f"Tello height: {mytello.get_height()}")
sleep(1)
mytello.land()

print(f"Tello flight time: {mytello.get_flight_time()}")




