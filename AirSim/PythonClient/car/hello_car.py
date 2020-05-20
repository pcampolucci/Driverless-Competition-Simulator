import setup_path 
import airsim
import cv2
import numpy as np
import os
import time

# connect to the AirSim simulator 
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = airsim.CarControls()

client.jsonSettingsUpdate("FSCar")

#restore to original state
client.reset()

client.enableApiControl(False)


            
