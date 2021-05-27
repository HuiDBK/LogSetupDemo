#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 日志模块logging的使用 }
# @Date: 2021/05/26 23:14
import logging
import logging.config

log_dict = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器

    # 日志信息格式化输出配置
    'formatters': {

        # 简单的日志输出
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },

        # 详细的日志输出
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s'
        },
    },

    # 日志信息处理器配置
    'handlers': {

        # 向终端中输出日志
        'console': {
            'level': 'DEBUG',                   # 处理的日志等级，DEBUG及以上
            'class': 'logging.StreamHandler',   # 日志处理器
            'formatter': 'simple'               # 日志格式化配置
        },

        # 向文件中输出日志
        'file': {
            'level': 'INFO',                                    # 处理的日志等级，DEBUG及以上
            'class': 'logging.handlers.RotatingFileHandler',    # 使用文件日志处理器
            'formatter': 'verbose',                             # 日志格式化配置
            'filename': './logs/test.log',                      # 日志文件存储位置
            'maxBytes': 1024 * 1024,                            # 每个日志文件最大 10MB, 单位: byte
            'backupCount': 20,                                  # 如果文件满了, 自动扩充, 最多保留 20 个日志文件
            'encoding': 'utf8',
        },
    },

    # 默认根日志器
    'root': {
        'level': 'DEBUG',           # 允许接受的日志等级
        'handlers': ['console']     # 选择日志处理器
    },

    # 自定义日志器
    'loggers': {
        'server': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True       # 设为 False则禁止将日志消息传递给父级记录器的处理程序中
        }
    }
}


def setup_logging():
    """
    配置日志信息
    :return:
    """
    logging.config.dictConfig(config=log_dict)
    # logger = logging.getLogger()

    logger = logging.getLogger('server')
    logger.debug('debug log test')
    logger.info('info log test')
    logger.warning('warning log test')
    logger.error('error log test')


def log_simple_use():
    """日志模块简单使用"""

    # 日志输出样式
    log_format = '%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s'
    logging.basicConfig(
        filename='test.log',
        format=log_format,
        level=logging.DEBUG
    )

    logging.debug('debug log test')
    logging.info('info log test')
    logging.warning('warning log test')
    logging.error('error log test')
    logging.critical('critical log test')


def main():
    # log_simple_use()
    setup_logging()


if __name__ == '__main__':
    main()
