"""
Fetches screen information for a list of gene symbols.
"""

# coding: utf-8

import json
import logging
import warnings
import pandas as pd
import click

from genomecrispr.query.fetch import Fetcher
from genomecrispr.query.extract import Extractor

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

warnings.simplefilter(action="ignore", category=RuntimeWarning)

def get_publications(fetcher, pubmed_ids):
    """Returns a data frame of publications."""
    rows = []

    for pubmed_id in pubmed_ids:

        data = fetcher.get(pubmed_id)
        publication = json.loads(data)
        conditions = publication[0]["condition"]

        for cell_line, condition in conditions.items():
            for _, screen in condition.items():
                row = {
                    "Pubmed": pubmed_id,
                    "Cell line": cell_line,
                    "Screen ID": screen["screenid"],
                    "MinFC": screen["minfc"],
                    "MaxFC": screen["maxfc"]
                }
                rows.append(row)

    return pd.DataFrame.from_records(rows)

# pylint: disable=no-value-for-parameter
@click.command()
@click.argument("path")
@click.argument("basepath")
def main(path, basepath):
    """
    Gets screens info for given genes.

    This script takes 2 arguments: `PATH`, a TXT file containing the list of
    gene symbols and `BASEPATH`, the base path for the output results.

    The script takes the list of genes and returns a list of screening
    experiments with information about the screen as CSV files.
    """
    symbols = pd.read_fwf(path, header=None).iloc[:,0].values

    # we query by gene symbol
    fetcher = Fetcher("sgrnas", "symbol", "query")

    # these fields will be extracted from the response
    fields = {
        "pubmed": "Pubmed",
        "score": "Score",
        "screentype": "Screen type",
        "condition": "Screen",
        "cellline": "Cell line",
        "log2fc": "Log2Fc",
        "start": "Start",
        "end": "End",
        "hit": "Hit"
    }
    extractor = Extractor(fields)

    # the results of the query
    dframes = []
    for symbol in symbols:
        data = fetcher.get(symbol)
        dframe = extractor.get(data)
        dframe.insert(0, "Gene ID", symbol)
        dframes.append(dframe)
        logging.info("Fetch for %s done.", symbol)
    dframe = pd.concat(dframes)

    # we chage the fetcher so we can query for publications
    fetcher.database = "experiments"
    fetcher.custom = "publication"
    fetcher.param = "id"
    publications = get_publications(fetcher, dframe.Pubmed.unique())

    # all the fields
    dframe = pd.merge(dframe, publications, on=["Pubmed", "Cell line"], how="left")
    dframe.to_csv(f"{basepath}.csv", index=False)

    # just the required fields
    dframe = dframe.loc[:, ["Gene ID", "Screen ID"] + list(fields.values())[1:]]
    dframe.to_csv(f"{basepath}.all.csv", index=False)

    # just the hits
    dframe.loc[ dframe.Hit == "true" ].to_csv(f"{basepath}.hits.csv", index=False)

if __name__ == "__main__":
    main()
