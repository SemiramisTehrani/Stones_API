# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uqr01n%1*rlhzl+q5%##ij_exxu%f^15lyq-hw!bk_$4zp!ch^'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME'  : 'stones_database',
        'HOST': 'localhost',
        'USER':'root',
        'PASSWORD': 'password'
    }
}


