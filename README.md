# Python Inverter COM

Python module to communicate with WKS EKO Circle inverters.

## Installation

```bash
$ python -m pip install inverter-com
```

## Utility

When installing the module, the `inverter-com` program is made available.
You can use it to send commands to inverters, and see what data you can get from.

The usage is as follow:

```bash
$ inverter-com COMMAND_OR_ALIAS [COMMAND_OR_ALIAS...] [--port SERIAL_PORT] [--debug]
```

As an example, here is how to retrieve the inverter serial number:

```bash
$ inverter-com QID

# The same command with an alias:
$ inverter-com serial-no
```

The output will be something like that:

```log
$ inverter-com serial-no
"96332309100452"
```

When enabling debug logs, it will likely show:

```log
$ inverter-com serial-no --debug
DEBUG:inverter_com.inverter:/dev/ttyUSB0 > SEND 'QIDÖê\r'
DEBUG:inverter_com.inverter:/dev/ttyUSB0 > WRITTEN 6 chars (OK)
DEBUG:inverter_com.inverter:/dev/ttyUSB0 < RAW b'(96332309100452?\xf3\r'
DEBUG:inverter_com.inverter:/dev/ttyUSB0 < DECODED '96332309100452'
"96332309100452"
```

The default port is `/dev/ttyUSB0`, you can change that:

```log
$ inverter-com serial-no --port /dev/ttyAMA0
"96332309100452"
```

### Available Commands

You can send any commands as defined in the official documentation, and even unknown commands.

There are also aliases you could use:

- `flags` for the `QFLAG` command;
- `metrics` for the `QPGS0` command;
- `metrics-n` (where `n` is a number between 1 and 9) for the `QPGSn` command;
- `ratings` for the `QPIRI` command;
- `serial-no` for the `QID` command;
- `settings` for the `QDI` command;

When the inverter does not understand a command, it will return the `NAK` keyword.

## Development

Setup a virtual environment:

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
