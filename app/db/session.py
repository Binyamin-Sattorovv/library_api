from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import setting


engine = create_engine(setting.DATABASE_URL)

Sessionlocal = sessionmaker(
    
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    
    db = Sessionlocal()
    
    try:
        
        yield db
        
    finally:
        
        db.close()
        
        