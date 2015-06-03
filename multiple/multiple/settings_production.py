from settings import *
import os

# ##### DEPLOYMENT REQUIRED SETTINGS
# for  manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["*"]

ADMINS = MANAGERS = (
    ('Mike Velazco', "mvelazco@netwarmonitor.com"),
    ('Omar Mendoza', "r2d2@netwarmonitor.com"),
    )
