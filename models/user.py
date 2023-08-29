from .base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    
    """
        TABLA USER
        
        COLLUMNS: ID, USERNAME, PASSWORD
    """
    
    __tablename__ = "usuario"
    
    id = Column(Integer(), primary_key = True, unique = True)
    username = Column(String(20), nullable = False)
    password = Column(String(20), nullable= False)
    
    def __str__(self):
        return self.name