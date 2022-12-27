#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint,request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.characteristic import FoodCharacteristic,FoodCharacteristicSchema
from api.models.food import Food,FoodSchema
from api.utils.database import db

characteristic_routes=Blueprint("characteristic_routes",__name__)


@characteristic_routes.route('/',methods=['POST'])
def create_characterisitc():
    try:
        data=request.get_json()
        characteristic=FoodCharacteristic(food_id=data['food_id'],
                                          Agirlik=data['Agirlik'],
                                          Karbonhidrat=data['Karbonhidrat'],
                                          Protein=data['Protein'],
                                          Yag=data['Yag'])
        char_schema=FoodCharacteristicSchema()
        result=char_schema.dump(characteristic.create())
        return response_with(resp.SUCCESS_201,value={"characteristic":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@characteristic_routes.route('/',methods=['GET'])
def get_charateristic_list():
    fetched=FoodCharacteristic.query.all()
    char_schema=FoodCharacteristicSchema(many=True,only=['id','food_id',
                                                         'Agirlik','Karbonhidrat',
                                                         'Protein','Yag'])
    charac_=char_schema.dump(fetched)
    return response_with(resp.SUCCESS_201,value={'characteristic':charac_})


@characteristic_routes.route('/<int:food_id>',methods=['PUT','PATCH'])
def update_food_charac_by_id(food_id):
    
    data=request.get_json()
    get_char=FoodCharacteristic.query.get_or_404(food_id)
    
    if(data.get('Agirlik')):
        get_char.Agirlik=data['Agirlik']
    if (data.get('Karbonhidrat')):
        get_char.Karbonhidrat=data['Karbonhidrat']
    if(data.get('Protein')):
        get_char.Protein=data['Protein']
    if(data.get('Yag')):
        get_char.Yag=data['Yag']

    db.session.add(get_char)
    db.session.commit()

    return response_with(resp.SUCCESS_204)


