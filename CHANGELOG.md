# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Current] - 202x-xx-xx

### Added
- 

### Changed
- 

### Deleted
-

## [1.2.1] - 2024-11-02

### Added
- CI: PyPI release workflow
- CI: auto-merge dependency pull-requests on successful tests

### Changed
- docs: misspellings on the README

## [1.2.0] - 2024-09-18

### Added
- new constant: `DEFAULT_PORT` with value "/dev/ttyUSB0"
- docs: example how to use the module as a module

### Changed
- the default `Inverter.port` is set to `constants.DEFAULT_PORT`
- `Inverter` arguments are all forced to be keyword-only except for `port`

### Deleted
- duplicate imports in `helpers.test_commands()`

## [1.0.1] - 2024-09-17

### Added
- Python 3.13 support

### Changed
- fixed the date padding in `helpers.expand_command()` (see issue [#3])
- moved from `black`, `flake8`, and `isort` to `ruff`
- pinned all dependencies to prevent surprises

## [1.0.0] - 2023-12-29

### Added
- first working version
- initial commit on `2023-12-08`


[Current]: https://github.com/BoboTiG/python-wks-com/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/BoboTiG/python-wks-com/tree/v1.2.1
[1.2.0]: https://github.com/BoboTiG/python-wks-com/tree/v1.2.0
[1.0.1]: https://github.com/BoboTiG/python-wks-com/tree/v1.0.1
[1.0.0]: https://github.com/BoboTiG/python-wks-com/tree/v1.0.0

[#3]: https://github.com/BoboTiG/python-wks-com/issues/3

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
