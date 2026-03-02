from PIL import Image
import numpy as np
import os

def encode(img_location):
    #get data of image
    
    msg_to_hide = input('enter message to hide: ')

    #process image
    image = Image.open(img_location,'r')
    width, height = image.size

    img_arr = np.array(list(image.get_flattened_data()))


    if image.mode == "P":
        print("Not supported")
        exit()

    channels = 4 if image.mode == "RGBA" else 3
    pixels = img_arr.size // channels
    stop_indicator = "$ALL DONE$"
    stop_indicator_len = len(stop_indicator)

    msg_to_hide += stop_indicator

    #convert the message into bytes
    message_byte = ''.join(f"{ord(c):08b}" for c in msg_to_hide)
    bits = len(message_byte)

    if bits>pixels:
        print("Not enough space in miage\n " \
        "Choose a smaller sentence please")
    else:
        index = 0
        for i in range(pixels):
            for j in range(0,3):
                if index<bits: 
                    img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + message_byte[index],2)
                    index+=1
        
        img_arr = img_arr.reshape((height,width,channels))
        result = Image.fromarray(img_arr.astype('uint8'), image.mode)
        result.save("temp.png")
        return (os.path.abspath("temp.png"))

    #the bit in the 1's place, LSB, is replaced 
    #with a bit of our hidden message


