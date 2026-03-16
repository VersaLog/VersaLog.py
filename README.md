## What is VersaLog.py?

[![PyPI version](https://badge.fury.io/py/VersaLog.svg)](https://badge.fury.io/py/VersaLog)
[![Downloads](https://pepy.tech/badge/VersaLog)](https://pepy.tech/project/VersaLog)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Support%20Server-7289DA?style=flat&logo=discord)](https://discord.gg/9EAsByDV)

What is VersaLog.py?
VersaLog is a powerful and flexible logging library for Python.
It supports everything from simple usage to advanced, highly customizable configurations to meet a wide range of needs.

## Support

Join our Discord server for support, questions, and community discussions:

[![Discord](https://img.shields.io/badge/Discord-Support%20Server-7289DA?style=flat&logo=discord)](https://discord.gg/9EAsByDV)

## Installation

```
pip install VersaLog
```

### Enum

| Enum       | Description                                                                  |
| ---------- | ---------------------------------------------------------------------------- |
| `detailed` | Logs including execution time and log levels                                 |
| `file`     | Logs with filename and line number                                           |
| `simple`   | Simple and easy-to-read logs                                                 |
| `simple2`  | Simple and easy-to-read log format. The timestamp is automatically included. |

### Options

| Options            | Description                                                                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `show_file`        | True : Display filename and line number (for simple and detailed modes)                                                                                                         |
| `show_tag`         | True : Show self.tag if no explicit tag is provided                                                                                                                             |
| `tag`              | Default tag to use when show_tag is enabled                                                                                                                                     |
| `enable_all`       | Shortcut to enable both show_file and show_tag                                                                                                                                  |
| `notice`           | True : When an error or critical level log is output, a desktop notification (using plyer.notification) will be displayed. The notification includes the log level and message. |
| `all_save`         | True : When an error or critical level log is output, the log will be saved to a file.                                                                                          |
| `save_levels`      | A list of log levels to save. Defaults to ["INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"].                                                                                    |
| `silent`           | True : Suppress standard output (print)                                                                                                                                         |
| `catch_exceptions` | True : Automatically catch unhandled exceptions and log them as critical                                                                                                        |

## Tag set

````python

# one tag
logger = VersaLog(enum="detailed", tag="a", show_tag=True)

# two tag
logger = VersaLog(enum="detailed", tag=["a", "a"], show_tag=True)
```                                                                                                    |

## Log save

````

[2025-08-06 04:10:36][INFO] : ok

```