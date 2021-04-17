from dotenv import load_dotenv
from app.factory import create_app

# load env from .env in project root folder
load_dotenv()

app = create_app()
