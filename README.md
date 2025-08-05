## What is VersaLog.py?

What is VersaLog.py?
VersaLog is a powerful and flexible logging library for Python.
It supports everything from simple usage to advanced, highly customizable configurations to meet a wide range of needs.

## Installation

```
pip install VersaLog
```

### Mode

| Mode       | Description                                                                  |
| ---------- | ---------------------------------------------------------------------------- |
| `detailed` | Logs including execution time and log levels                                 |
| `file`     | Logs with filename and line number                                           |
| `simple`   | Simple and easy-to-read logs                                                 |
| `simple2`  | Simple and easy-to-read log format. The timestamp is automatically included. |

### Options

| Options       | Description                                                                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `show_file`   | True : Display filename and line number (for simple and detailed modes)                                                                                                         |
| `show_tag`    | True : Show self.tag if no explicit tag is provided                                                                                                                             |
| `tag`         | Default tag to use when show_tag is enabled                                                                                                                                     |
| `enable_all`  | Shortcut to enable both show_file and show_tag                                                                                                                                  |
| `notice`      | True : When an error or critical level log is output, a desktop notification (using plyer.notification) will be displayed. The notification includes the log level and message. |
| `all_save`    | True : When an error or critical level log is output, the log will be saved to a file.                                                                                          |
| `save_levels` | A list of log levels to save. Defaults to ["INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"].                                                                                    |

## Log save

```
[2025-08-06 04:10:36][INFO] : ok
```

## Sample

**Simple** : [Tap](https://github.com/kayu0514/VersaLog.py/blob/main/tests/simple_test.py)  
**Detailed** : [Tap](https://github.com/kayu0514/VersaLog.py/blob/main/tests/detailed_test.py)
**File** : [Tap](https://github.com/kayu0514/VersaLog.py/blob/main/tests/file_test.py)
