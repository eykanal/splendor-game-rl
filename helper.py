import pickle
import json

import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('json_file')
def pickle_data(json_file):
    """
    Read card or tile data from JSON_FILE and save to pickle format.
    """
    data = json.load(open(json_file, "r"))
    # output file has same name but add .p extension
    output_name = '.'.join(json_file.split('.')[0:-1])
    pickle.dump(data, open("%s.p" % output_name, "wb"))

if __name__ == "__main__":
    cli()
