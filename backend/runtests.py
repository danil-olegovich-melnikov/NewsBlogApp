import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

from auth_user.models import User, UserProfile, UserEmailVerification
from article.models import Article

from django_seed import Seed
from django_seed.exceptions import SeederException

seeder = Seed.seeder()


def populate():
    seeder.add_entity(User, 50)
    seeder.add_entity(UserEmailVerification, 50)

    try:
        seeder.add_entity(UserProfile, 50, {
            'picture': lambda x: 'ava.jfif',
        })
    except SeederException:
        pass

    try:
        seeder.add_entity(Article, 50, {
            'cover': lambda x: 'cover.jpg',
            'description': lambda x: seeder.faker.text(10000)
        })
    except SeederException:
        pass

    seeder.execute()


if __name__ == "__main__":
    populate()
