# Who's There
Developed by Hayato Nakamura (Experimental) using the implementation on https://www.hackster.io/gr1m/raspberry-pi-facial-recognition-16e34e?ref=channel&ref_id=425_published___&offset=2.

## Hardware Requirements

Raspberry Pi 3 B+: https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/
Night Vision Pi Camera: https://www.amazon.com/Raspberry-Camera-Module-Vision-Sensor/dp/B07J1XWD9C/ref=sr_1_1_sspa?ie=UTF8&qid=1541211263&sr=8-1-spons&keywords=pi+night+vision&psc=1

## Software Requirements

'''
pip install dlib
python setup.py install
sudo apt-get install cmake
pip install scikit-image
'''

This program is designed to take a photo of the user's face, recognize it from the database of user faces, and open the door of the room if the user has the necessary access. 
