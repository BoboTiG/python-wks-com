"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""


def compute_crc(value: str) -> str:
    """
    >>> compute_crc("(96332309100452")
    '?\xf3'
    """
    crc = 0
    for ch in value:
        if not ch:
            assert 0, repr(value)
            break
        crc ^= ord(ch) << 8
        for _ in range(8):
            crc = crc << 1 if (crc & 0x8000) == 0 else (crc << 1) ^ 0x1021
        crc &= 0xFFFF
    return crc.to_bytes(2, "big").decode(encoding="latin1")


def extract_response(seq: bytes) -> str:
    r"""
    >>> extract_response(b"(NAKss\r")
    'NAK'
    >>> extract_response(b"(96332309100452?\xf3\r")
    '96332309100452'
    """
    # Remove leading parenthesis, and trailing CRC + CR
    seq = seq[1:-3]
    return seq.decode(encoding="latin1")


def test_command(port: str, command: str, debug: bool = False) -> None:
    import json

    from inverter_com import Inverter, constants

    if debug:
        import logging

        logging.basicConfig(level=logging.DEBUG)

    command = getattr(constants, f"CMD_{command.upper().replace('-', '_')}", command)

    inverter = Inverter(port)
    res = inverter.send(command)
    print(json.dumps(res, indent=4, sort_keys=True))
