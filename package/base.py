import urllib

print(urllib.__file__) # file path

from app.models.user import *
from app.models.user import all, find_by, first

all()
first()
find_by(a=1, b=2)

import app.models.user

app.models.user.all()
app.models.user.first()
app.models.user.find_by(a=1, b=2)

from app.routes import DOMAIN as domain

print(domain)

# module only import once even package code change
from app import routes

print(routes.DOMAIN) # always test.com

# reload your package
from imp import reload

reload(routes)

print(routes.DOMAIN)
