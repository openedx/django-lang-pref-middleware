from distutils.core import setup

setup(
    name='django-lang-pref-middleware',
    version='0.1.0',
    packages=['lang_pref_middleware'],
    url='https://github.com/edx/django-lang-pref-middleware',
    description="Django middleware for setting the user's language preference at request time.",
    long_description=open('README.md').read(),
    tests_require=[
        "django>1.4",
        'django-nose==1.4.1',
        "coverage==3.7.1",
        "pep8==1.5.7",
        "pep257==0.3.2",
        "pylint==1.2.1",
    ]
)
