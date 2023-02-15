"""
Extracts data from a GenomeCRISPR REST API response.
"""

from typing import Dict

import json
import pandas as pd

class Extractor:
    """Class to extract data from a GenomeCRISPR REST API JSON response."""

    _fields = Dict

    def __init__(self, fields: Dict) -> None:
        """\
        Constructor of the Extractor class.

        This class extracts fields from a GenomeCRISPR REST API JSON response.

        Parameters
        ----------
        fields
            A `dict` containing fields to extract with their column name in the
            return `pandas.DataFrame`.
        """
        self._fields = fields

    @property
    def fields(self):
        """Getter for _fields"""
        return self._fields

    @fields.setter
    def fields(self, new_fields):
        """Setter for _fields"""
        self._fields = new_fields

    def get(self, data: bytes) -> pd.DataFrame:
        """\
        Extracts fields from a GenomeCRISPR REST API JSON reponse.

        The methods returns a `pandas.DataFrame` containing the extracted
        fields.

        Parameters
        ----------
        data
            `bytes` containing the GenomeCRISPR REST API JSON reponse.
        """
        json_str = data.decode("utf-8")
        screens  = json.loads(json_str)
        dframe = pd.DataFrame.from_records(screens)
        dframe = dframe[self._fields.keys()]
        dframe.columns = self._fields.values()
        return dframe
