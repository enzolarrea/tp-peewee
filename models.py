from peewee import *

db = SqliteDatabase('notas.db')

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nombre = CharField(unique=True)

class Bloc(BaseModel):
    nombre = CharField()
    creador = ForeignKeyField(Usuario, backref='blocs')
    privado = BooleanField(default=False)

class Nota(BaseModel):
    texto = TextField()
    editado = BooleanField(default=False)
    autor = ForeignKeyField(Usuario, backref='notas')
    bloc = ForeignKeyField(Bloc, backref='notas')
