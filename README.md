# Python Inverter COM

Python module to communicate with WKS EKO Circle inverters.

## Installation

```bash
$ python -m pip install inverter-com
```

## Utility

When installing the module, the `inverter-read` program is made available.
You can use it to send commands to inverters, and see what data you can get from.

The usage is as follow:

```bash
$ inverter-read [--port SERIAL_PORT] [--debug] COMMAND_OR_ALIAS [COMMAND_OR_ALIAS...]
```

As an example, here is how to retrieve the inverter serial number:

```bash
$ inverter-read QID

# The same command with an alias:
$ inverter-read serial-no
```

The output will be something like that:

```log
$ inverter-read serial-no
"96332309100452"
```

When enabling debug logs, it will likely show:

```log
$ inverter-read --debug serial-no
DEBUG:inverter_com.inverter:/dev/ttyUSB0 > SEND 'QIDÖê\r'
DEBUG:inverter_com.inverter:/dev/ttyUSB0 > WRITTEN 6 chars (OK)
DEBUG:inverter_com.inverter:/dev/ttyUSB0 < RAW b'(96332309100452?\xf3\r'
DEBUG:inverter_com.inverter:/dev/ttyUSB0 < DECODED '96332309100452'
"96332309100452"
```

The default port is `/dev/ttyUSB0`, you can change that:

```log
$ inverter-read --port /dev/ttyAMA0 serial-no
"96332309100452"
```

### Available Commands

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
- `warnings` for the `QPIWS` command;
- `yearly-load` for the `QLY` command (it will automatically fill the date using the current time);
- `yearly-pv` for the `QEY` command (it will automatically fill the date using the current time);

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
