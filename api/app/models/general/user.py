from mongoengine import Document
from mongoengine.fields import (StringField)

class User(Document):

    meta = {'collection': 'user'}
    username = StringField()
    password = StringField()
    name = StringField()
    