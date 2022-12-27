#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Blueprint,request
from api.utils.manip_image import string_to_image,load_image
from api.utils import label_image
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.food import Food,FoodSchema
from collections import defaultdict
from glob import glob
from flask_cors import CORS ,cross_origin
import json

predict_routes=Blueprint("predict_routes",__name__)
base_path=os.path.abspath(os.path.dirname(__file__))

@predict_routes.route('/',methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def predict_food():
    foods={"food":[]}
    data=request.get_json()

    if(data.get('base64')):
        string_to_image(data["base64"])
    else:
        f=request.form['file']
        f.save(image_name)
        
    image_name=glob(os.path.join(base_path,"../images/image.*"))

    result=load_image(image_name[0])
    first_high_accuracy=list(result.values())[0]
    if first_high_accuracy >= .8:
        label=list(result.keys())[0]
        Accuracy=list(result.values())[0]

        fetched=Food.find_food_by_name(label)
        food_schema=FoodSchema()
        result=food_schema.dump(fetched)
        result['Accuracy']=str(Accuracy)
        foods["food"].append(result)
        return response_with(resp.SUCCESS_200,value={"data":foods})

    else:
        
        for key ,value in result.items():
            fetched=Food.find_food_by_name(key)
            food_schema=FoodSchema()
            result=food_schema.dump(fetched)

            result["Accuracy"] =str(value)
            foods["food"].append(result)

        return response_with(resp.SUCCESS_200,value={"data":foods})
    return response_with(resp.INVALID_INPUT_422)


