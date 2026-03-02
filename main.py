from encode import encode
from upload import upload
from decode import decode
import os

def uploader():
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

def decoder():
    inp_name = input('enter location of image: ')
    if(os.path.exists(inp_name)):
        decode(inp_name)
    else:
        print("The given path does not exist. Please run again")

choice = int(input("Would you like to encode[1] or decode[2]\n(enter 1 or 2): "))
if choice == 1:
    uploader()
if choice == 2:
    decoder()
else:
    print("Invalid choice. Please run again")


