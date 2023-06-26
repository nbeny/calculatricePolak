from app.extensions import db
from sqlalchemy import Column, Integer, String

class Formule(db.Model):
    id = Column(Integer, primary_key=True)
    formule = Column(String)
    result = Column(Integer)
