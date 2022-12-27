#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint,request,url_for,current_app
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.food import Food,FoodSchema
from api.utils.database import db

food_routes=Blueprint("food_routes",__name__)

@food_routes.route('/',methods=['POST'])
def create_food():
    try:
        data=request.get_json()
        food=Food(name=data["name"],food_description=data['food_description'])
        food_schema=FoodSchema()
        result=food_schema.dump(food.create())
        return response_with(resp.SUCCESS_201,value={"food_name":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
@food_routes.route('/',methods=['GET'])
def get_food_list():
    fetched=Food.query.all()
    food_schema=FoodSchema(many=True,only=['name','food_description','id'])
    food=food_schema.dump(fetched)
    return response_with(resp.SUCCESS_201,value={"foods":food})

@food_routes.route('/<int:food_id>',methods=['GET'])
def get_food_by_id(food_id):
    fetched=Food.query.get_or_404(food_id)
    food_schema=FoodSchema()
    food=food_schema.dump(fetched)
    return response_with(resp.SUCCESS_200,value={"food":food})

@food_routes.route('/<food_name>',methods=['GET'])
def get_food_by_name(food_name):
    fecthed=Food.find_food_by_name(food_name)
    food_schema=FoodSchema()
    food=food_schema.dump(fecthed)
    if food:
        return response_with(resp.SUCCESS_200,value={"food":food})
    else:
        return response_with(resp.INVALID_INPUT_422)

@food_routes.route('/<int:food_id>',methods=['PATCH','PUT'])
def update_food_info_by_id(food_id):
    data=request.get_json()
    get_food=Food.query.get_or_404(food_id)
    
    if(data.get('name')):
        get_food.name=data['name']
    if(data.get('food_description')):
        get_food.food_description=data['food_description']

    db.session.add(get_book)
    db.session.commit()

    food_schema=FoodSchema()
    food=food_schema.dump(get_food)
    return response_with(resp.SUCCESS_200,value={"food":food})

@food_routes.route('/<int:id>',methods=['DELETE'])
def delete_food_by_id(food_id):
    get_food=Food.query.get_or_404(id)
    db.session.delete(get_food)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
