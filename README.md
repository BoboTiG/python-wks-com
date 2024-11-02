# Python Inverter COM

[![PyPI Version](https://img.shields.io/pypi/v/wks-com.svg)](https://pypi.python.org/pypi/wks-com)
[![PyPI Status](https://img.shields.io/pypi/status/wks-com.svg)](https://pypi.python.org/pypi/wks-com)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/wks-com.svg)](https://pypi.python.org/pypi/wks-com)
[![Tests](https://github.com/BoboTiG/python-wks-com/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/BoboTiG/python-wks-com/actions/workflows/tests.yml)
[![Github License](https://img.shields.io/github/license/BoboTiG/python-wks-com.svg)](https://github.com/BoboTiG/python-wks-com/blob/main/LICENSE)

Python module to communicate with WKS EKO Circle inverters.

## Installation

```bash
$ python -m pip install -U wks-com
```

## Module

You can use the module directly from your code:

```python
from wks_com import constants
from wks_com.inverter import Inverter


# Init the inverter (default port is /dev/ttyUSB0, several optional keyword-arguments are available)
# Example: inverter = Inverter("/dev/ttyAMA0", timeout=5.0)
inverter = Inverter()

# Send a command to the inverter
response = inverter.send("QID")

# The same command via an alias
response = inverter.send("serial-no")

# The same command using a constant
response = inverter.send(constants.CMD_SERIAL_NO)
```

## Program

The module comes with the `wks-read` program.
You can use it to send commands to inverters, and see what data you can get from.

The usage is as follows:

```bash
$ wks-read [--port SERIAL_PORT] [--debug] COMMAND_OR_ALIAS [COMMAND_OR_ALIAS...]
```

As an example, here is how to retrieve the inverter serial number:

```bash
$ wks-read QID
"96332309100452"

# The same command via an alias
$ wks-read serial-no
"96332309100452"
```

When enabling debug logs, it will likely show:

```log
$ wks-read --debug serial-no
DEBUG:wks_com.inverter:/dev/ttyUSB0 > SEND 'QIDÖê\r'
DEBUG:wks_com.inverter:/dev/ttyUSB0 > WRITTEN 6 chars (OK)
DEBUG:wks_com.inverter:/dev/ttyUSB0 < RAW b'(96332309100452?\xf3\r'
DEBUG:wks_com.inverter:/dev/ttyUSB0 < DECODED '96332309100452'
"96332309100452"
```

The default port is `/dev/ttyUSB0`, you can change that:

```log
$ wks-read --port /dev/ttyAMA0 serial-no
"96332309100452"
```

## Commands and Aliases

You can send any commands as defined in the official documentation, and even unknown commands.

There are also aliases you could use:

- `daily-load` for the `QLD` command (it will automatically fill the date using the current time);
- `daily-pv` for the `QED` command (it will automatically fill the date using the current time);
- `metrics` for the `QPGS0` command;
- `monthly-load` for the `QLM` command (it will automatically fill the date using the current time);
- `monthly-pv` for the `QEM` command (it will automatically fill the date using the current time);
- `ratings` for the `QPIRI` command;
- `serial-no` for the `QID` command;
- `status` for the `QPIGS` command;
- `time` for the `QT` command;
- `total-load` for the `QLT` command;
- `total-pv` for the `QET` command;
- `warnings` for the `QPIWS` command;
- `yearly-load` for the `QLY` command (it will automatically fill the date using the current time);
- `yearly-pv` for the `QEY` command (it will automatically fill the date using the current time);

When the inverter does not understand a command, it will respond with `NAK`.

## Development

Set up a virtual environment:

```bash
$ python -m venv venv
$ . venv/bin/activate
```

Install, or update, dependencies:

```bash
$ python -m pip install -U pip
$ python -m pip install -e '.[dev]'
```

Run tests:

```bash
$ python -Wd -m pytest --doctest-modules src
```

Run linters, and quality checkers:

```bash
$ ./checks.sh
```
