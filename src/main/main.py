import cv2 as cv
import numpy as np
import os
import time
import concurrent.futures
from assignment import Device, Assign

# from action import *



def img_path(img_name):
    img = f'src//img//{img_name}.png'
    return img


# launch game
icon_img = img_path('icon')
notice_img = img_path('notice')
exit_img = img_path('exit')
enter_img = img_path('enter')

# makes character
mage_img = img_path('mage')
create_img = img_path('create')
confirm_img = img_path('con')
model_img = img_path('model')
confirm_app_img = img_path('confirm_app')
eg_img = img_path('eg')

# in-game
skip_img = img_path('skip')
confirm2_img = img_path('confirm2')
confirm3_img = img_path('confirm3')
ryall_img = img_path('model')
main_quest_img = img_path('main_quest')
dialogue_img = img_path('dialogue')
dialogue2_img = img_path('dialogue2')
skip2_img = img_path('skip2')

main_task = [
    icon_img,
    exit_img,
    eg_img,
    create_img,
    mage_img,
    confirm_img,
    confirm3_img,
    model_img,
    confirm_app_img,
    skip_img,
    dialogue_img,
    main_quest_img,
]



adb_names = ["badbar4","badbar5","badbar6","badbar7"]
list_of_devices = Device.devices
devices_in_total = len(list_of_devices)




# def run_init(path, sequence):
#     print(adb_names[sequence])
#     device = Assign(path, adb_names[sequence], sequence)
#     device_name = device.device_name
#     screenshot = device.screenshot


if __name__ == '__main__':
    def test(img):

        with concurrent.futures.ThreadPoolExecutor() as executor:


            results = [executor.submit(Assign,vision_image_file=img ,adb_name= adb_names[adb], device_sequence= adb)for adb in range(devices_in_total)]

            for f in concurrent.futures.as_completed(results):
                this = f.result()
                print(f'{f.result()}')
                wow = cv.cvtColor(this.screenshot, cv.COLOR_BGR2GRAY)
                cv.waitKey(100)
                cv.imshow('test', wow)









# this_device  =   Assign(ball_img, adb_names, 1)
# print(this_device.this_device())

    while True:
        # test()
        # break
        run = [test(img)for img in main_task]



        if cv.waitKey(100) == ord('q'):
            quit()
            cv.destroyAllWindows()


