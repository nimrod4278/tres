To run:
    1. make sure you have all the requirement parameter in .envv file
    2. make sure you are in the "tres" directory.
    3. run "pip install -r requirements.txt"
    4. follow the instructions below

use the following command to traverse an address:

    python cli.py --address <ADDRESS_YOU_WANT_TO_TRAVERSE>

    example:
    python cli.py --address 0xfb626333099a91ab677bcd5e9c71bc4dbe0238a8

use the following command to query the DB - DB_NAME and COLLECTION_NAME default to the graph db and nodes collection and can be left out:

    python cli.py --action query --db <DB_NAME> --collection <COLLECTION_NAME> --filter '<FILTER_IN+JSON_FORMAT>'

    example:
    python cli.py --action query --filter '{"address": "0xfb626333099a91ab677bcd5e9c71bc4dbe0238a8"}'


for cli information run - python cli.py --help:

    usage: cli.py [-h] [--action ACTION] [--db DB] [--collection COLLECTION] [--filter FILTER] [--address ADDRESS] [--depth DEPTH]

    Traverse transaction graph

    options:
    -h, --help                      show this help message and exit
    --action ACTION                 select query/traverse
    --db DB                         what kind of query - default to find
    --collection COLLECTION         what kind of query - default to find
    --filter FILTER                 what filter to use
    --address ADDRESS               the address you need to traverse
    --depth DEPTH                   the depth of traversal

