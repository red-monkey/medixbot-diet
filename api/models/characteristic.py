#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


class FoodCharacteristic(db.Model):
    __tablename__='charateristic'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Agirlik=db.Column(db.Float,nullable=True)
    Karbonhidrat=db.Column(db.Float,nullable=True)
    Protein=db.Column(db.Float,nullable=True)
    Yag=db.Column(db.Float,nullable=True)
    food_id=db.Column(db.Integer,db.ForeignKey('foods.id'),nullable=False)

    def __init__(self,food_id,Agirlik=None,Karbonhidrat=None,Protein=None,Yag=None):
        self.Agirlik=Agirlik
        self.Karbonhidrat=Karbonhidrat
        self.Protein=Protein
        self.Yag=Yag
        self.food_id=food_id
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class FoodCharacteristicSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model=FoodCharacteristic
        sqla_session=db.session

    id=fields.Number(dump_only=True)
    food_id=fields.Number(required=True)
    Agirlik=fields.Float(required=False)
    Karbonhidrat=fields.Float(required=False)
    Protein=fields.Float(required=False)
    Yag=fields.Float(required=True)

