import numpy as np
from PIL import Image

def decode(img_location):
    image = Image.open(img_location,'r')
    img_arr = np.array(list(image.get_flattened_data()))

    channels = 4 if image.mode == 'RGBA' else 3

    pixels = img_arr.size // channels

    secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0,3)]

    secret_bits = ''.join(secret_bits)

    secret_bytes= [secret_bits[i:i+8] for i in range(0,len(secret_bits),8)]


    secret_message = [chr(int(secret_bytes[i],2)) for i in range(len(secret_bytes))]

    secret_message = ''.join(secret_message)

    stop_indicator = "$ALL DONE$"

    if stop_indicator in secret_message:
        print(secret_message[:secret_message.index(stop_indicator)])
    else:
        print("couldn't find a message")


        #we know each byte had it's LSB replaced with one bit of our hidden message
        #so we traverse through to each LSB of each byte
        #we add those bits together
        #then we convert those into their ASCII values
        #and we return the message!
        #our loop runs only if we find our stop indicator somewhere at the end
    

