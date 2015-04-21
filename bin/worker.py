#!/usr/bin/env python

import os
import sys
import json
import argparse
import logging

from sqlalchemy import create_engine

here = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(here, "..")))

import r3d2msa.db.rcad as db
import r3d2msa.db.hub as hub
import r3d2msa.ranges as ranges
import r3d2msa.background.worker as work


class Worker(work.Worker):

    def expand(self, ranges):
        if not self.hub:
            return []

        expanded = []
        for (start, stop) in ranges:
            try:
                found = self.hub.units(start, stop)
                expanded.extend(found)
            except Exception as err:
                self.logger.error("Failed expanding range %s %s", start, stop)
                self.logger.exception(err)

        return ','.join(expanded)

    def process(self, query):
        if self.canned:
            canned = dict(self.canned)
            canned['id'] = query['id']
            canned['expanded_units'] = self.expand(query['ranges'])
            return canned

        rcad = db.connect(config)

        def translator(chain):
            return db.get_translation(rcad, query['pdb'], query['model'],
                                      chain)

        translated = ranges.translate(translator, query['ranges'])
        full, summ, reqs = db.seqvar(rcad, query['pdb'], query['model'],
                                     translated)
        return {
            'id': query['id'],
            'units': query['units'],
            'full': full,
            'summ': summ,
            'reqs': reqs,
            'pdb': query['pdb'],
            'model': query['model'],
            'ranges': query['ranges'],
            'expanded_units': self.expand(query['ranges'])
        }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', dest='config', default='conf/config.json',
                        help='Config file to use')
    parser.add_argument('--log-file', dest='log_filename', default='',
                        help='File to log to')
    parser.add_argument('--name', dest='name', default='Worker',
                        help='Name of the worker for logging')
    parser.add_argument('--test-data', dest='canned', default='',
                        help='Canned data to use if any')
    args = parser.parse_args()

    if args.log_filename:
        logging.basicConfig(filename=args.log_filename)
    else:
        logging.basicConfig()

    canned = None
    if args.canned:
        with open(args.canned, 'rb') as raw:
            canned = json.load(raw)

    with open(args.config, 'rb') as raw:
        config = json.load(raw)

    rna3dhub = None
    try:
        engine = create_engine(config['rna3dhub']['connection'])
        rna3dhub = hub.db.Hub(engine)
    except Exception as err:
        logging.error("Could not connect to rna3dhub")
        logging.error("Will not have full units for 3D display")
        logging.exception(err)

    worker = Worker(config, name=args.name, canned=canned, hub=rna3dhub)
    worker()
