import logging


class BaseConfig(object):
    DEBUG = True
    LOG_MODE = 'all'                # stdout,file or all, default all
    LOG_FILE_PATH = 'log'           # specify the file storage directory
    LOG_LEVEL = logging.DEBUG

    MAP_BOX_TOKEN = 'pk.eyJ1Ijoiam9obmtvbWFybmlja2kiLCJhIjoiY2t5NjFzODZvMHJkaDJ1bWx6OGVieGxreSJ9.IpojdT3U3NENknF6_WhR2Q'
    OPEN_WEATHER_MAP_APP_ID = '7efa332cf48aeb9d2d391a51027f1a71'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = logging.WARNING


config = DevelopmentConfig()
# config = TestConfig()
# config = ProductionConfig()
