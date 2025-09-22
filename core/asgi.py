"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

#Standard Django ASGI app
django_app = get_asgi_application()

#new fastapi app (empty for now)
fastapi_app = FastAPI(title = "FastAPI-Django Combo")

#mounting will be done later; right now we just expose both if needed 
application = django_app

