from pydantic_settings import BaseSettings

class Settings(BaseSettings):
     database_hostname: str
     database_port : str
     database_password : str
     database_name : str
     database_username : str
     secret_key : str
     algorithm : str
     access_token_expire_minutes : int

     class Config:
         extra = "allow"  # Allows extra fields in the .env file
          
settings = Settings(_env_file='.env')
