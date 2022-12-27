#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from api.models.characteristic import FoodCharacteristicSchema


class Food(db.Model):
    __tablename__='foods'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    food_description=db.Column(db.String(500),nullable=True)
    food_characteristic=db.relationship('FoodCharacteristic',backref='Food',cascade='all,delete-orphan')

    def __init__(self,name,food_description=None,food_characteristic=[]):
        self.name=name
        self.food_description=food_description
        self.food_characteristic=food_characteristic

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    @classmethod
    def find_food_by_name(cls,name) ->str:
        return cls.query.filter_by(name=name).first()


class FoodSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model=Food
        sqla_session=db.session

    id=fields.Number(dump_only=True)
    name=fields.String(required=True)
    food_description=fields.String(required=False)
    food_characteristic=fields.Nested(FoodCharacteristicSchema,many=True,only=['Agirlik','Karbonhidrat','Protein','Yag','food_id'])
