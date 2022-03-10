# Sage-DOI

## Docker
Build ezid command line interface:
```
docker build  -t sagecontinuum/ezid -f ezid/Dockerfile .
```

`ezid3.py` is set as the ENTRYPOINT in the dockerfile so it should only need to be passing arguments to `ezid3.py`

Build ezid json to xml schema converter:
```
docker build -t sagecontinuum/ezid_schema -f ezid_schema/Dockerfile .
```

## Convert metadata json file to xml file for Datacite
Currently, `ezid` only accepts the metadata as an .xml file. We will only work with json files
and then convert them to valid .xml files for Datacite metadata profile.[WIP for JSON support](https://support.datacite.org/docs/how-can-i-map-different-metadata-formats-to-the-datacite-xml#datacite-json)

Run ezid_schema docker container with `--help`:
```
docker run -v metadata:/workdir -it --rm sagecontinuum/ezid_schema --help
```

Run ezid_schema docker container to convert `test-file.json` to `metadata.xml`
```
docker run -v $(pwd)/metadata:/workdir/metadata --env-file=.env -it --rm sagecontinuum/ezid_schema --json_file metadata/test-file.json --xml_filename metadata.xml
```

## ezid python cli usage

Run ezid docker container with `--help`:
```
docker run --env-file=.env -it --rm sagecontinuum/ezid --help
```

All the commands will prompt for a password unless password is set, EZID_USER:EZID_PASS

Create a DOI for a dataset with the converted `metadata.xml` file:
```
docker run -v $(pwd)/metadata:/workdir/metadata --env-file=.env -it --rm sagecontinuum/ezid $EZID_USER:$EZID_PASS mint doi:10.5072/FK2 datacite @metadata/metadata.xml
```

View newly created DOI:
```
docker run --env-file=.env -it --rm sagecontinuum/ezid $EZID_USER:$EZID_PASS -dt view doi:10.5072/FK2QN67493
```