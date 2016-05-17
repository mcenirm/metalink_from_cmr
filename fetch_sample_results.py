#!/usr/bin/env python3

import sys, json

import requests


def main(argv):
    parameters = merge_parameters_from_argv(argv)
    out_name = 'granules.'+''.join([x for x in json.dumps(parameters, sort_keys=True) if x.isalnum()])+'.json'
    response = search(parameters)
    with open(out_name, 'wb') as out:
        out.write(response.content)
    return out_name


DEFAULT_PARAMETERS = {
    'downloadable': 'true',
    'page_size': '1',
}


def merge_parameters_from_argv(argv=[], defaults=DEFAULT_PARAMETERS):
    parameters = dict(defaults)
    for arg in argv:
        if '=' in arg:
            k, v = arg.split('=')
            parameters[k] = v
        else:
            parameters[k] = ''
    return parameters


def search(parameters=DEFAULT_PARAMETERS, search_url='https://cmr.earthdata.nasa.gov/search/granules.json'):
    return requests.get(search_url, parameters)


if __name__ == '__main__':
    print(main(sys.argv[1:]))
