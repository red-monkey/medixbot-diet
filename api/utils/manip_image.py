#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import base64
from PIL import Image
import api.utils.label_image as label_image
from io import BytesIO

def string_to_image(image):
    extensions=image[image.find("/")+1:image.find(";")]
    encode_image=image[image.find(",")+1:]
    decode_image=Image.open(BytesIO(base64.b64decode(bytes(encode_image,"utf-8"))))
    image_path=os.path.abspath(os.path.dirname(__file__))
    
    if(not os.path.exists(f"{image_path}/../images")):
        os.mkdir(f"{image_path}/../images")
    
    image_path=os.path.join(image_path,"../images/image.{}".format(extensions))   
    decode_image.save(image_path)




def load_image(image):
    text=label_image.main(image)
    return text


