import datetime

from peewee import Model, SqliteDatabase, CharField, DateTimeField

DATABASE = SqliteDatabase('todo.db')


class Todo(Model):
    name = CharField(max_length=200)
    pub_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()
