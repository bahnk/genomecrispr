Input/Output
============

.. module:: genomecrispr.query

The `query` subpackage is used to fetch and extract information from GenomeCRISPR.

Fetcher
-------

The `fetch` module is used to read files.

.. autoclass:: genomecrispr.query.fetch.Fetcher

  .. automethod:: genomecrispr.query.fetch.Fetcher.__init__

  .. automethod:: genomecrispr.query.fetch.Fetcher.get

Extractor
---------

The `extract` module is used to extract fields from a response.

.. autoclass:: genomecrispr.query.extract.Extractor

  .. automethod:: genomecrispr.query.extract.Extractor.__init__

  .. automethod:: genomecrispr.query.extract.Extractor.get

