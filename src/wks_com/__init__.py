"""
An ultra fast cross-platform multiple screenshots module in pure python
using ctypes.

This module is maintained by Mickaël Schoentgen <contact@tiger-222.fr>.

You can always get the latest version of this module at:
    https://github.com/BoboTiG/python-wks-com
If that URL should fail, try contacting the author.
"""

from wks_com.inverter import Inverter

__version__ = "1.0.1"
__author__ = "Mickaël 'Tiger-222' Schoentgen"
__date__ = "2023-2024"
__copyright__ = f"""
Copyright (c) {__date__}, {__author__}

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee or royalty is hereby
granted, provided that the above copyright notice appear in all copies
and that both that copyright notice and this permission notice appear
in supporting documentation or portions thereof, including
modifications, that you make.
"""
__all__ = ("Inverter",)
