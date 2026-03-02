from encode import encode
from upload import upload
import os
inp_name = input('enter location of image: ')
out_name = input('enter name of image\n(file will be saved in S3 using this name): ')

store = encode(inp_name)
if(store == "Path DNE"):
    print("Invalid image location. Please run again")
else:
    #now a temp file is created, we gotta store its location
    upload(store,out_name)

try:

    if os.path.exists(store):
        os.remove(store)
    
except PermissionError:
    print(f"unable to delete temp file as permission denied, please delete manually at {store}")
except OSError as e:
    print(f"An error occured: {e}")



#store should be a string, not an image