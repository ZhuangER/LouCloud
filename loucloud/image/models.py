#!/usr/bin/env python
# encoding: utf-8


from sqlalchemy import Column
from ..extensions import db
# from .constants import HOST_OK

class Host(db.Model):

    __tablename__ = 'images'

    image_name = Column(db.String(128), primary_key=True)
    image_path = COlumn(db.String(256), nullable=False)
    
