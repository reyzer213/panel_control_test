import django_setup

from user_management import *
from user_management.something.models import User

user1 = User.objects.create_user(
    name="Bodya Kyper",
    email="test@gmail.com",
    role="admin"
).save()
user2 = User.objects.create_user(
    name="Sergey Kyper",
    email="test22@gmail.com",
    role="user"
).save()
user3 = User.objects.create_user(
    name="Volodya Kyper",
    email="test2@gmail.com",
    role="user"
).save()
user3 = User.objects.get(id=1).all() # Ще є first() і last() і замість get є filter
print(user3[0].email)

user2_to_update = User.objects.get(id=2)
print(user2_to_update.email)
user2_to_update.email = "example@gmail.com"
user2_to_update.save()

delete_user3 = User.objects.get(id=3)
delete_user3.delete()