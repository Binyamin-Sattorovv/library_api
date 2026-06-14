from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from association import book_categories
from db.base import Base

class Category(Base):
    
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, unique=True)
    
    books = relationship("Book", secondary=book_categories, back_populates="categories")