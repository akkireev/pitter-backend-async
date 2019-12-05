import os

DEBUG: bool = bool(int(os.getenv('DEBUG', 1)))  # pylint: disable=invalid-envvar-default

PROJECT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APISPEC_CONF: dict = dict(
    title='Pitter async API',
    version='0.1',
    url='/api/pitter-async/swagger/apispec',
    swagger_path='/api/pitter-async/swagger',
    static_path='/api/pitter-async/swagger/static',
)

# Speech to text integrations
REMOTE_STORAGE_API_KEY = os.environ['REMOTE_STORAGE_API_KEY']
REMOTE_STORAGE_TYPE = os.environ['REMOTE_STORAGE_TYPE']
REMOTE_STORAGE_BUCKET_NAME = os.environ['REMOTE_STORAGE_BUCKET_NAME']
