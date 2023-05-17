"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7uje4dadc9vm1n7d0-a.oregon-postgres.render.com",
        database="todo_9rdl",
        user="root",
        password="uVuAP4FQZPAk3VOTg5s6jAvi5V1eqLgT")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
