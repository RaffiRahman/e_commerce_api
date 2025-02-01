from datetime import datetime
from email.policy import default
from tortoise import Model, fields
from pydantic import BaseModel

class User(Model):
    id = fields.IntField(pk = True, index = True)
    username = fields.CharField(max_length = 20, null = False, unique = True)
    email = fields.CharField(max_length = 200, null = False, unique = True)
    password = fields.CharField(max_length = 100, null = False)
    is_verified = fields.BooleanField(default = False)
    join_date = fields.DatetimeField(default = datetime.now(datetime.timezone.utc))

class Business(Model):
    id = fields.IntField(pk = True, index = True)
    business_name = fields.CharField(max_length = 20, null = False, unique = True)
    city = fields.CharField(max_length = 100, null = False, default = 'Unspecified')
    region = fields.CharField(max_length = 100, null = False, default = 'Unspecified')
    business_description = fields.TextField(null = True)
    logo = fields.CharField(max_length = 200, null = False, default = 'default.jpg')
    owner = fields.ForeignKeyField('models.User', related_name = 'business')

class Product(Model):
    id = fields.IntField(pk = True, index = True)
    name = fields.CharField(max_length = 100, null = False, index = True)
    catagory = fields.CharField(max_length = 100, index = True)
    original_price = fields.DecimalField(max_degit = 12, decimal_places = 2)
    new_price = fields.DecimalField(max_degit = 12, decimal_places = 2)
    
