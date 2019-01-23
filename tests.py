import unittest
import json
from peewee import SqliteDatabase
from models import Todo
from app import app

MODELS = [Todo]

# use an in-memory SQLite for tests.
TEST_DB = SqliteDatabase(':memory:')


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        self.client = app.test_client()
        TEST_DB.bind(MODELS, bind_refs=False, bind_backrefs=False)
        TEST_DB.connect()
        TEST_DB.create_tables([Todo], safe=True)
        Todo.create(
            name='Launch the Space Rocket',
        )

    def test_todo_creation(self):
        """Create Todo / 1 Entry"""
        self.assertEqual(Todo.select().count(), 1)

    def test_todo_listview_get(self):
        self.response = self.client.get('http://0.0.0.0:8000/api/v1/todos')
        decoded = json.loads(self.response.data.decode("utf-8"))

        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(decoded,
                         [{"id": 1, "name": "Launch the Space Rocket"}])

    def test_todo_listview_post(self):
        sending_data = {'name': 'Rocket Launched'}
        self.response = self.client.post('http://0.0.0.0:8000/api/v1/todos',
                                         data=sending_data)
        decoded = json.loads(self.response.data.decode("utf-8"))

        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(decoded,
                         {"id": 2, "name": "Rocket Launched"})

    def test_todo_detailview_get(self):
        self.response = self.client.get('http://0.0.0.0:8000/api/v1/todos/1')
        decoded = json.loads(self.response.data.decode("utf-8"))

        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(decoded,
                         {"id": 1, "name": "Launch the Space Rocket"})

    def test_todo_detailview_post(self):
        sending_data = {'name': 'Rocket Launched Edited'}
        self.response = self.client.put('http://0.0.0.0:8000/api/v1/todos/1',
                                        data=sending_data)
        decoded = json.loads(self.response.data.decode("utf-8"))

        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(decoded,
                         {"id": 1, "name": "Rocket Launched Edited"})

    def test_todo_deleteview(self):
        self.response = self.client.delete('http://0.0.0.0:8000/api/v1/todos/1')
        decoded = ''
        if self.response.data:
            decoded = json.loads(self.response.data.decode("utf-8"))

        self.assertEqual(self.response.status_code, 204)
        self.assertEqual(decoded, '')

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
