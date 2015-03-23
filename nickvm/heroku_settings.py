import urlparse
import dj_database_url
DATABASES = dict()
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))

SWAMP_DRAGON_REDIS_HOST = redis_url.hostname
SWAMP_DRAGON_REDIS_DB = 0
SWAMP_DRAGON_REDIS_PORT = redis_url.port

DRAGON_URL = 'http://nickvm.herokuapp.com:9999'


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'