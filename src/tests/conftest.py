"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
import os
import pty

import pytest


@pytest.fixture()
def port() -> str:
    """http://allican.be/blog/2017/01/15/python-dummy-serial-port.html"""
    _, slave = pty.openpty()
    return os.ttyname(slave)
