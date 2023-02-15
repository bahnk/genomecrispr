"""
Testing module for the genomecrispr.query.fetch module.
"""

import pytest
from ..fetch import Fetcher

# pylint: disable=too-few-public-methods
class TestFetcher:
    """The test class associated with the Fetcher class."""

    def test_get_raises_error_when_request_fails(self):
        """Tests Fetcher.get raises `ConnectionError` if request fails."""
        fetcher = Fetcher("sgrnas", "foo", "bar")
        with pytest.raises(ConnectionError):
            fetcher.get("test")
