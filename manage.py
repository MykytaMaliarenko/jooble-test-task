import os
import unittest

from dotenv import load_dotenv
from flask_script import Manager

from app import create_app, db

# load env from .env in project root folder
load_dotenv()

app = create_app()
app.app_context().push()

# for managing terminal commands
manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
