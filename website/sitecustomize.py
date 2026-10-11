"""Compatibility shims for older Python versions used in local checks."""

import datetime as _datetime

try:
    _datetime.UTC
except AttributeError:  # pragma: no cover - exercised on Python < 3.11
    _datetime.UTC = _datetime.timezone.utc
