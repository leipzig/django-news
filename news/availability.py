### This is a non-standard method of checking the availability of different modules in django.
### TODO: Find/create a more centralized, simple, standard method of doing this.
from django.conf import settings
from django.utils import datastructures

###
# Check if comments are available
if hasattr(settings, 'INSTALLED_APPS') and 'django.contrib.comments' in settings.INSTALLED_APPS:
    comments = True
else:
    comments = False
