#!/usr/bin/env python3

# server/seed.py

from app import app
from models import db, Message
from faker import Faker
from random import choice

fake = Faker()

usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def seed_data():
    messages = []
    for _ in range(20):
        message = Message(
            body=fake.sentence(),
            username=choice(usernames)
        )
        messages.append(message)

    db.session.bulk_save_objects(messages)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
