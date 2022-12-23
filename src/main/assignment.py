from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from vision import Vision
from windowcapture import WindowCapture



class Device(object):
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()

    # devices[0].shell('input tap 443 168')

    def __init__(self, image_file, device_names, device_sequence):
        #   properties
        self.device = None
        self.device = device_names[device_sequence]
        self.image_path = image_file
        self.device_name = device_names
        self.device_sequence = device_sequence



class Recognize(Device):
    def __new__(cls, vision_image_file, adb_names, device_sequence):

        if len(cls.devices) >= 1:
            device_number = device_sequence
            devices_length = len(cls.devices)

            if devices_length == device_number:
                # print(f' No more devices to assign')
                quit()

            if devices_length > device_number:
                # determines new devices and points device as a new_device
                new_device = cls.devices[device_number]
                device = new_device

                # assigns current device to a name within an array
                new_device_name = adb_names[device_number]
                device_name = new_device_name

                # captures a window with our device name
                wincap = WindowCapture(new_device_name)
                screenshot = wincap.get_screenshot()

                # determine previous dimensions, and obtain it's total square pixels
                prev_w = WindowCapture.w
                prev_h = WindowCapture.h
                prev_sqpx = prev_w * prev_h
                print(prev_w, prev_h, prev_sqpx)

                # determine current dimensions, and obtain it's total square pixels
                curr_w = wincap.size_w
                curr_h = wincap.size_h
                curr_sqpx = curr_w * curr_h
                print(curr_w, curr_h, curr_sqpx)

                # converts img_file to a readable cv2 format
                image_path = vision_image_file
                img = cv.imread(image_path)

                # determine scale value for both height and width
                scale_w = float(curr_w / prev_w)
                scale_h = float(curr_h / prev_h)

                # obtains the average scale value
                scale_avg = float(scale_w + scale_h) / 2
                print(scale_avg)


                # determines the dimensions of the img_file
                img_w = int(img.shape[1])
                img_h = int(img.shape[0])
                img_sqpx = img_w * img_h
                print(img_w, img_h, img_sqpx)

                # determines the adjusted dimensions of our img_file to adapt changes in curr_sqpx
                final_img_sqpx = int(scale_avg * img_sqpx)
                final_img_w = int(final_img_sqpx / img_h)
                final_img_h = int(final_img_sqpx / img_w)

                print(final_img_w, final_img_h, final_img_sqpx)

                # finalizes new dimensions of our img_file for opencv
                dim = (final_img_h, final_img_w)
                img_resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

                # sends adjusted img dimension to Vision Module
                adjusted_vision_image = Vision(img_resized)
                image_data = adjusted_vision_image

                # returns the (x, y) location at which the image is found
                tap_location = image_data.find(device, scale_avg, screenshot, 0.65, 'points')

                def this_device():
                    x = device
                    y = device_name
                    z = tap_location

                    wow = f'{x}, {y}, {z}'
                    return x,y,z
                print(this_device())

            #
            if cv.waitKey(1) == ord('q'):
                quit()
                cv.destroyAllWindows()



        else:
            adjusted_device_number = device_sequence + 1
            Recognize(vision_image_file, adb_names, adjusted_device_number)

        if len(cls.devices) == 0:
            print('no device attached')
            quit()


