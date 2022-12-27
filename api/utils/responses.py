#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import make_response,jsonify

INVALID_FIELD_NAME_SENT_422={
    'http_code':422,
    'status':'invalidField',
    'message':'Invalid fields found'
}

INVALID_INPUT_422={
    'http_code':422,
    'status':'invalidInput',
    'message':'Invalid Input'
}
MISSING_PARAMETERS_422={
    'http_code':422,
    'status':'missingParameter',
    'message':'Missing parameters'
}
BAD_REQUEST_400={
    'http_code':400,
    'status':'BadRequest',
    'message':'Bad Request'
}
SERVER_ERROR_500={
    'http_code':500,
    'status':'serverError',
    'message':'Server Error'
}

SERVER_ERROR_404={
    'http_code':404,
    'status':'notFound',
    'message':'Resource Not found'
}
UNAUTHORIZED_403={
    'http_code':403,
    'status':'notAuthorized',
    'message':'You are not authorised to execute this.'
}
ALREADY_EXIST_406={
    'http_code':406,
    'status':'userExist',
    'message':'User already exist'
}

SUCCESS_200={
    'http_code':200,
    'status':'sucess'
}
SUCCESS_201={
    'http_code':201,
    'status':'success'
}
SUCCESS_204={
    'http_code':204,
    'status':'success'
}

def response_with(response,value=None,message=None,error=None,
                  headers={},pagination=None):
    result={}
    if value is not None:
        result.update(value)
    if response.get('message',None) is not None:
        result.update({'message':response['message']})
    result.update({'status':response['status']})

    if error is not None:
        result.update({'errors':error})
    if pagination is not None:
        result.update({'pagination':pagination})

    headers.update({'Acess-Control-Allow-Origin':'*'})
    headers.update({'server':'Flask REST API'})

    return make_response(jsonify(result),response['http_code'],headers)
