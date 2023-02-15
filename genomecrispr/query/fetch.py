"""
Fetches data as JSON from the GenomeCRISPR REST API.
"""

import json
from urllib3 import PoolManager

class Fetcher:
    """Class to fetch data from GenomeCRISPR REST API."""

    _url: str = "http://genomecrispr.dkfz.de/api"
    _database: str = None
    _custom: str = None
    _param: str = None
    _pool: PoolManager = None

    def __init__(self, database: str, custom: str, param: str) -> None:
        """\
        Constructor of the Fetcher class.

        This class creates a `PoolManager` from `urllib3` library. It uses it
        to get JSON data from GenomeCRISPR REST API.

        Parameters
        ----------
        database
            The database (for example `sgrnas` or `experiments`.
        custom
            The subdatabase or table (for example `symbol` or `publication`).
        param
            The query parameter (for example `query` or `id`).
        """
        self._database = database
        self._custom = custom
        self._param = param
        self._pool = PoolManager()

    @property
    def database(self):
        """Getter for _database."""
        return self._database

    @database.setter
    def database(self, new_database):
        """Setter for _database."""
        self._database = new_database

    @property
    def custom(self):
        """Getter for _custom."""
        return self._custom

    @custom.setter
    def custom(self, new_custom):
        """Setter for _custom."""
        self._custom = new_custom

    @property
    def param(self):
        """Getter for _param."""
        return self._param

    @param.setter
    def param(self, new_param):
        """Setter for _param."""
        self._param = new_param

    def get(self, query: str) -> bytes:
        """\
        Gets JSON `bytes` from GenomeCRISPR REST API.

        The methods returns a `bytes` containing the JSON information
        associated with the query. The methods raises a `ConnectionError`
        if the request fails or if the HTTP status is not 200.

        Parameters
        ----------
        query
            The search query.
        """
        url = f"{self._url}/{self._database}/{self._custom}"
        headers = {"Content-Type": "application/json"}
        data = json.dumps({self._param: query})

        try:
            response = self._pool.request("POST", url, headers=headers, body=data)
        except Exception as exc:
            raise ConnectionError(f"{url} with {data} request failed") from exc

        if response.status != 200:
            raise ConnectionError(f"{url} with {data} request status is not 200")

        return response.data
