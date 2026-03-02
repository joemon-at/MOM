from encode import encode
from upload import upload
import os
inp_name = input('enter location of image: ')
out_name = input('enter name of image: ')

store = encode(inp_name)
#now a temp file is created, we gotta store its location
upload(store,out_name)

os.remove(store)


#store should be a string, not an image