#!/usr/bin/env python3  

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--aln', type=str, help='Sequence alignment')
args = parser.parse_args()
