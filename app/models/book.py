from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from association import book_categories
class Book(Base):
    
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String, nullable=False)
    
    year = Column(Integer, nullable=False)
    
    description = Column(Text)
    
    author_id = Column(Integer, ForeignKey("autors.id"))
    
    author = relationship("Author", back_populates="books")
    
    categories = relationship("Category", secondary=book_categories, back_populates="books")
    
    