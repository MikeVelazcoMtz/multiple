from django.db import router
from django.contrib.auth.models import User


def content_file_name(instance, filename):
    path = ""
    if instance._state.db is None:
        path = "/".join([router.db_for_read(User), filename])
        return path
