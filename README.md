# Python日志模块logging的使用详解

## 日志

> 在开发一些大型项目的时候，都会使用日志来记录项目运行时产生的信息，以备出错时定位分析和从日志信息中提取数据统计分析等。在 `Python` 中使用 `logging` 内置模块即可对项目进行日志的配置。

<br/>

## logging模块的使用

### 简单使用

> `logging` 模块提供了一系列便利的函数
>
> 它们分别是 `debug(), info(), warning(), error(), critical()`

<br/>

```python
import logging

logging.debug('debug log test')
logging.info('info log test')
logging.warning('warning log test')
logging.error('error log test')
logging.critical('critical log test')
```

<br/>

**输出结果：**

```python
WARNING:root:warning log test
ERROR:root:error log test
CRITICAL:root:critical log test
```

为什么只输出了 `warning`， `error` 和 `critical` 的结果，因为 `logging` 模块默认使用 `warning` 日志级别，就是只有 `warning` 及以上日志等级才会显示。

日志等级从高到低，如下所示

| 级别       | 数值 | 何时使用                                       |
| :--------- | :--- | ---------------------------------------------- |
| `CRITICAL` | 50   | 严重的错误，表明程序已不能继续执行             |
| `ERROR`    | 40   | 由于严重的问题，程序的某些功能已经不能正常执行 |
| `WARNING`  | 30   | 表明有已经或即将发生的意外，程序仍按预期进行   |
| `INFO`     | 20   | 确认程序按预期运行                             |
| `DEBUG`    | 10   | 细节信息，仅当诊断问题时适用。                 |
| `NOTSET`   | 0    | 无任何等级限制                                 |

<br/>

我们只要把 `logging` 的默认日志等级改下就好了

```python
import logging

# 配置日志等级
logging.basicConfig(level=logging.DEBUG)

logging.debug('debug log test')
logging.info('info log test')
logging.warning('warning log test')
logging.error('error log test')
```

<br/>

**输出结果如下：**

```python
DEBUG:root:debug log test
INFO:root:info log test
WARNING:root:warning log test
ERROR:root:error log test
```

<br/>

### 指定日志输出样式

当然我们还可以指定日志输出格式

```python
import logging


# 日志输出样式
log_format = '%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s'
logging.basicConfig(format=log_format, level=logging.DEBUG)

logging.debug('debug log test')
logging.info('info log test')
logging.warning('warning log test')
logging.error('error log test')
logging.critical('critical log test')
```

<br/>

**输出结果如下：**

```python
DEBUG 2021-05-27 00:04:26,327 main.py 65 debug log test
INFO 2021-05-27 00:04:26,327 main.py 66 info log test
WARNING 2021-05-27 00:04:26,327 main.py 67 warning log test
ERROR 2021-05-27 00:04:26,327 main.py 68 error log test
CRITICAL 2021-05-27 00:04:26,327 main.py 69 critical log test
```

<br/>

其中日志信息格式化输出配置样式说明

- **%(levelname)s ，日志等级**
- **%(asctime)s ，时间**
- **%(filename)s ，文件名**
- **%(lineno)d ，行号**
- **%(message)s，日志信息**

<br/>

这些配置都是固定，不可随便写，还有好多日志格式化样式，这里只介绍了一些常用的格式配置，大家可以去官网查看更多的格式化配置信息。[https://docs.python.org/zh-cn/3.7/library/logging.html#formatter-objects](https://docs.python.org/zh-cn/3.7/library/logging.html#formatter-objects)

<br/>

### 日志记录到文件中

在 `logging.basicConfig` 中设置 `filename` 属性即可把日志信息写入文件中

```python
import logging


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
```

<br/>

运行程序后 `test.log` 如下内容

![日志信息展示](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dbb23f6033d4e5eba4618fb2103d2df~tplv-k3u1fbpfcp-watermark.image)

<br/>

## 自定义日志配置

> 通常我们在项目中都是自定义一些通用日志配置，然后供项目全局使用。写好这些配置下次要在别的项目使用之间复制粘贴过来修改修改一下即可。来康康是如何配置的。

<br/>

### 准备日志配置信息

配置日志详细信息，需要导入 `logging.config` 来进行加载日志配置信息

首先准备日志配置信息字典

```python
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
            'maxBytes': 1024 * 1024,        # 每个日志文件最大 10MB, 单位: byte
            'backupCount': 20,              # 如果文件满了, 自动扩充, 最多保留 20 个日志文件
            'encoding': 'utf8',
        },
    },

    # 默认根日志器
    'root': {
        'level': 'DEBUG',           # 允许接受的日志等级
        'handlers': ['console']     # 选择日志处理器
    },

    # 自定义的日志器
    'loggers': {
        'server': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True       # 设为 False则禁止将日志消息传递给父级记录器的处理程序中
        }
    }
}
```

<br/>

其中大字典的 `key` 都是固定，例如 `version,formatters, handlers, root, loggers`等都是固定的配置项。而有一些子选项是可以自己自定义如

- `formatters` 下的 `simple` 和 `verbose`，是可以改成自己想要的名字。
- `handlers` 下的 `console` 和 `file` 也是可以修改的。
- `loggers` 下的 `server` 都是一样可以修改的

<br/>

具体配置的说明，在这字典中都有一一注释我就不全介绍了，我就介绍一下 `handlers` 日志处理器的配置

在 `logging` 模块中有许多 **日志处理器类**，我们只需要在 `pycharm` 中输入 `logging.Handler` 就能弹出最基本的几个日志处理类。

![日志处理器](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0f2d280511d469eafccecf5dd946511~tplv-k3u1fbpfcp-watermark.image)

<br/>

而上文所用到的 `StreamHandler` 则是流处理器，日志将随着系统标准输入、输出流展示，而我们的 **PyCharm终端、控制台等** 显示的信息就属于系统标准输出流。

而 `RotatingFileHandler` 日志处理器则是 `FileHandler` 的子类。其主要作用就是把日志写入文件中，当文件内容达到最大限制时可以自动扩充日志文件，以达到日志文件的轮换。

<br/>

### 加载日志配置信息

然后使用 `logging.config.dictConfig()` 方法加载日志配置，该方法接受一个 **字典** 参数。

<br/>

```python
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

    ...与上文一致故省略

    # 默认根日志器
    'root': {
        'level': 'DEBUG',  # 接受的日志等级
        'handlers': ['console']
    },
    
    # 自定义的日志器
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
    logger = logging.getLogger()
	# logger = logging.getLogger('root')
    
    logger.debug('debug log test')
    logger.info('info log test')
    logger.warning('warning log test')
    logger.error('error log test')


def main():
    setup_logging()


if __name__ == '__main__':
    main()

```

<br/>

使用 `logging.getLogger()` 即可获取相应配置日志器，其接受一个日志器的名字，不传则默认使用 `root` 根日志器，同 `logging.getLogger('root')` 效果一致。

如果之间运行程序会出现如下错误

```python
ValueError: Unable to configure handler 'file'
```

那是因为你在日志配置中设置了一个文件处理器 `file` ，其日志文件将存储在 `filename` 配置项中，在这里是

```python
./logs/test.log		# 代表存储在当前路径下的 logs目录下的 test.log 文件
```

`logging` 模块不会自动帮我们创建目录，因此只需在当前目录中创建一个 `logs` 目录即可。

<br/>

**最后程序运行结果如下**

```python
DEBUG main 74 debug log test
INFO main 75 info log test
WARNING main 76 warning log test
ERROR main 77 error log test
```

<br/>

不用跟 `root` 根日志器，使用 `server` 日志器，代码如下

```python
import logging
import logging.config

log_dict = {...同上文省略...}

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
    
    
def main():
    setup_logging()


if __name__ == '__main__':
    main()    
```

<br/>

**运行结果如下：**

控制台

```python
DEBUG main 75 debug log test
INFO main 76 info log test
WARNING main 77 warning log test
ERROR main 78 error log test
```

<br/>

日志文件 `logs/test.log`

![文件日志信息](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f4556cc49c7456db2d74867ebbb928e~tplv-k3u1fbpfcp-watermark.image)

<br/>

由于 `server` 日志器设置了 `'propagate': True`，会 将日志消息传递给父级记录器的处理程序中，因此不仅控制台会显示日志信息，文件也会记录，但文件记录的等级被设置成 `INFO` 了，因此 `DEBUG` 调试日志信息，将不会出现在文件中。

<br/>

## 使用日志配置文件

> 这里我将采用 `yaml` 格式的日志配置文件。具体配置内容和上文大致一样，多了一个 `error_file_handler` 错误日志处理器，目的就是把 **错误日志单独放在一个文件中，方便以后排查错误**。

<br/>

### 创建日志配置文件

创建 `logging.yaml` 文件，内容如下所示

```yaml
version: 1
disable_existing_loggers: true

# 日志信息格式化输出配置
formatters:
    simple:
        format: '%(levelname)s %(filename)s %(lineno)d %(message)s'
    verbose:
        format: '%(levelname)s %(asctime)s -Loc %(filename)s -Row %(lineno)d -%(name)s %(message)s'

# 日志信息处理器配置
handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout

    # 错误日志单独处理
    error_file_handler:
        class: logging.handlers.RotatingFileHandler
        level: ERROR
        formatter: verbose
        filename: ./logs/errors.log   # 错误日志文件存储位置
        maxBytes: 10485760            # 每个日志文件最大 10MB
        backupCount: 20               # 如果文件满了, 自动扩充, 最多保留 20 个日志文件
        encoding: utf8

    server_file_handler:
      class: logging.handlers.RotatingFileHandler
      level: INFO                     # 只在文件中记录INFO级别及以上的log
      formatter: verbose
      filename: ./logs/server.log    # 项目日志文件, 记录所有日志信息
      maxBytes: 10485760             # 10MB
      backupCount: 30
      encoding: utf8

# 根日志器
root:
    level: DEBUG
    handlers: [console]

# 日志器
loggers:
    server:
        level: DEBUG      # 允许打印 DEBUG 及以上log
        handlers: [server_file_handler, error_file_handler]
        propagate: True   # 设为 False则禁止将日志消息传递给父级记录器的处理程序中
```

<br/>

### 加载日志配置函数

```python
# log_test.py 文件

import os
import yaml
import logging
import coloredlogs
import logging.config


# 项目根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 日志配置文件
LOG_CONF_FILE = os.path.join(BASE_DIR, 'logging.yaml')


def setup_logging(default_path=LOG_CONF_FILE, default_level=logging.DEBUG, env_key='LOG_CFG'):
    """
    配置项目日志信息
    :param default_path: 日志文件默认路径
    :param default_level: 日志默认等级
    :param env_key: 系统环境变量名
    :return:
    """
    path = default_path

    value = os.getenv(env_key, None)  # 获取对应的环境变量值
    if value is not None:
        path = value

    if os.path.exists(path):
        with open(path, mode='r', encoding='utf-8') as f:
            try:
                logging_yaml = yaml.safe_load(f.read())
                logging.config.dictConfig(logging_yaml)
                coloredlogs.install(level='DEBUG')
            except Exception as e:
                print(e)
                print('无法加载日志配置文件, 请检查日志目录是否创建, 使用默认的日志配置')
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('日志配置文件不存在, 使用默认的日志配置')
```

<br/>

这里使用到第三方库如下

- `yaml` 是用于读取 `yaml` 格式的日志配置文件

- `coloredlogs` 用于让日志在控制台中有颜色显示。

<br/>

然后我们在项目中只要执行完 `setup_logging()` 日志配置函数

其他模块直接使用 `logging.getLogger('server')` 就可获取我们配置好的日志器。

<br/>

```python
# log_demo.py 文件

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


```

<br/>

```python
# log_test.py

def main():
    setup_logging()

    logger = logging.getLogger('server')
    logger.debug('debug log test')
    logger.info('info log test')
    logger.warning('warning log test')
    logger.error('error log test')

    # 日志在其他模块中使用演示
    import log_demo
    log_demo.log_test1()
    log_demo.log_test2()
    log_demo.LogDemo.log_test()
    
    
if __name__ == '__main__':
    main()    
```

<br/>

### 日志效果展示

运行 `log_test.py` 结果如下

**控制台信息**

![带颜色的日志信息](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f46e58c7937448098c1d337fcacc92f~tplv-k3u1fbpfcp-watermark.image)

<br/>

**全部日志配置文件信息**

![全部日志文件信息](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e192d5ee0324c568074ed3eabcaec73~tplv-k3u1fbpfcp-watermark.image)

<br/>

**错误日志文件信息**

![错误日志文件信息](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aec72066261a4dd0854a1bc94c95da36~tplv-k3u1fbpfcp-watermark.image)

<br/>

## 源代码

源代码已上传到 **GitHub** [LogSetupDemo](https://github.com/HuiDBK/LogSetupDemo)，欢迎大家来访。

**万水千山总是情，点赞再走行不行，✍ 码字不易，还望各位大侠多多支持❤️**
