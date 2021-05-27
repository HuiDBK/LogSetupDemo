#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 日志器的使用 }
# @Date: 2021/05/27 22:46
import logging

logger = logging.getLogger('server')  # 维护一个全局日志对象

logger.debug('debug log test')


def log_test1():
    logger.info('info log test')


def log_test2():
    try:
        a = 1 / 0
    except Exception as e:
        logger.error(e)


class LogDemo(object):

    @staticmethod
    def log_test():
        logger.warning('warning log test')


def main():
    pass


if __name__ == '__main__':
    main()
