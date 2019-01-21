import unittest
from peewee import *
from models import Todo

MODELS = [Todo]

# use an in-memory SQLite for tests.
TEST_DB = SqliteDatabase(':memory:')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        TEST_DB.bind(MODELS, bind_refs=False, bind_backrefs=False)
        TEST_DB.connect()
        TEST_DB.create_tables([Todo], safe=True)

    def test_todo_creation(self):
        """Create Todo / 1 Entry"""
        Todo.create(
            name='Launch the Space Rocket',
        )
        todo = Todo.select().get()

        self.assertEqual(Todo.select().count(), 1)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        TEST_DB.drop_tables(MODELS)

        # Close connection to db.
        TEST_DB.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.


if __name__ == '__main__':
    unittest.main()
