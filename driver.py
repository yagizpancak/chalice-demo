import os

from pymongo import MongoClient
from pymongo.database import Database


def get_database_url():
    database_url = "mongodb+srv://yagizcan923:123@cluster0.0nzem27.mongodb.net/?retryWrites=true&w=majorit"
    print(f"DATABASE_URL: {database_url}")  # Add this line for debugging
    if not database_url:
        raise RuntimeError("Config error: DATABASE_URL")
    return database_url


def get_database_name() -> str:
    if _database_name := "chalice-demo":
        return _database_name

    raise RuntimeError("No database NAME")


def client() -> MongoClient:
    return MongoClient(get_database_url())


class DatabaseClient:
    """
    An instance of a pymongo Database implemented as a singleton to reduce performance overheads.

    Access the singleton instantiating DatabaseClient. E.g. database = DatabaseClient().
    """

    _database: Database

    def __new__(cls, *args, **kwargs) -> Database:
        if not hasattr(cls, "_database"):
            client = MongoClient(get_database_url())
            cls._database = client[get_database_name()]
        return cls._database