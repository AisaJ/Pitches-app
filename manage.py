from app import create_app,db
from app.models import Pitch
from flask_script import Server,Manager

#Creating an app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
  manager.run()