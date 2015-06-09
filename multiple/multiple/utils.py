from django.db import router
from django.contrib.auth.models import User
from django.db.models import ImageField, FileField


class NMImageField(ImageField):
    """docstring for NMImageField"""
    def __init__(self, *args, **kwargs):
        def content_file_name(instance, filename):
            path = ""
            if instance._state.db is None:
                path = "/".join([router.db_for_read(User), filename])
                return path

        kwargs['upload_to'] = content_file_name
        super(NMImageField, self).__init__(*args, **kwargs)


class NMFileField(FileField):
    """docstring for NMFileField"""
    def __init__(self, *args, **kwargs):
        def content_file_name(instance, filename):
            path = ""
            if instance._state.db is None:
                path = "/".join([router.db_for_read(User), filename])
                return path

        kwargs['upload_to'] = content_file_name
        super(NMFileField, self).__init__(*args, **kwargs)
