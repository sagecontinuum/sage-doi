#! /usr/bin/env python
import argparse
from datacite import schema42
import json
import os
from os.path import join
import uuid

METADATA_OUTDIR = os.getenv('METADATA_OUTDIR')
print(METADATA_OUTDIR)
METADATA_PROFILE='Datacite'
cli_parser = argparse.ArgumentParser(description= METADATA_PROFILE +' Schema JSON to XML converter')

cli_parser.add_argument('--json_file',
                        nargs = 1,
                        metavar='json_file',
                        type=argparse.FileType('r'),
                        help='JSON file to convert to XML file'
                       )

cli_parser.add_argument('--xml_filename',
                        nargs='?',
                        metavar='xml_filename',
                        type=str,
                        help='XML desired file name'
                       )

args = cli_parser.parse_args()
json_file = args.json_file[0]
xml_filename = args.xml_filename
data = json.load(json_file)

assert schema42.validate(data), 'Invalid JSON file.'

doc = schema42.tostring(data)
if xml_filename is None:
    xml_filename = 'metadata_' + str(uuid.uuid4()) + '.xml'

if METADATA_OUTDIR is None:
    xml_abspath = xml_filename
else:
    xml_abspath = join(METADATA_OUTDIR,xml_filename)

with open(xml_abspath, 'w') as xfile:
    xfile.write(doc)
    xfile.close()
