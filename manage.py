import os
import unittest

from dotenv import load_dotenv
from flask_script import Manager

from app.factory import create_app

# load env from .env in project root folder
load_dotenv()

app = create_app()
app.app_context().push()

# for managing terminal commands
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
