try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

setup(name = 'django-news',
      description = "Fork of monokrome's lightweight news app",
      author = 'Byron Ruth, Kevin Murphy, Brandon R. Stoner (orig)',
      author_email = 'b@devel.io',
      version = '0.7.1',

      zip_safe = False,
      include_package_data = True,
      packages = find_packages(),
      url = 'http://github.com/cbmi/django-news/',

      classifiers = [
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independant",
          "Programming Language :: Python",
          "Framework :: Django",
          "Topic :: Internet :: WWW/HTTP / :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP / :: Site Management",
      ],
)

