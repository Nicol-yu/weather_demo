import os
import logging
import logging.config


def init_logger(level: int, mode: str, path: str) -> None:
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(asctime)s %(pathname)'
                          's:%(filename)s:%(lineno)d %(message)s'
            }
        },
        'handlers': {
            'stdout': {
                'level': level,
                'formatter': 'simple',
                'class': 'logging.StreamHandler',
            },
            'info': {
                'level': level,
                'formatter': 'simple',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(path, 'info.log'),
                'when': 'D',
                'interval': 24,
                'backupCount': 30,
                'encoding': 'utf-8',
            },
            'error': {
                'level': logging.WARNING,
                'formatter': 'simple',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(path, 'error.log'),
                'when': 'D',
                'interval': 24,
                'backupCount': 30,
                'encoding': 'utf-8',
            },
        },
        'loggers': {
            'logger': {
                'handlers': [],
                'level': 'DEBUG',
                'propagate': True,
            }
        }
    }

    if not os.path.isdir(path):
        os.makedirs(path)

    if mode.lower() == 'file':
        log_config['loggers']['logger']['handlers'] = ['info', 'error']
    elif mode.lower() == 'stdout':
        log_config['loggers']['logger']['handlers'] = ['stdout']
    else:
        log_config['loggers']['logger']['handlers'] = ['stdout', 'info', 'error']

    logging.config.dictConfig(log_config)





