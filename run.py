#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
from main import application
from waitress import serve

if __name__=='__main__':
    serve(application, host="0.0.0.0", port=os.environ.get('PORT', 5000))
