from dotenv import load_dotenv
import os

load_dotenv()

class Setting:
    
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    
setting = Setting()