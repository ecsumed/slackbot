from peewee import *

db = SqliteDatabase('app.db')

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    assembla_key = CharField()

db.create_tables([User], safe=True)
