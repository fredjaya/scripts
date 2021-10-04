#!/usr/bin/env python3

import argparse
from Bio import AlignIO

# Read in sequence file
alignment = AlignIO.read("../rec-bench/data/fmdv/FMDV_Kenya_plaques_refs.fas", "fasta")

# https://stackoverflow.com/questions/39249121/extract-a-part-of-fasta-sequence-based-on-bp-coordinates
with open("FMDV_Kenya_plaques_refs_Lpro.fa", "w") as out:
    AlignIO.write(alignment[:,0:603], out, "fasta")

with open("FMDV_Kenya_plaques_refs_VP2-3-1.fa", "w") as out:
    AlignIO.write(alignment[:,859:2805], out, "fasta")

with open("FMDV_Kenya_plaques_refs_2A-B-C.fa", "w") as out:
    AlignIO.write(alignment[:,2806:4275], out, "fasta")

with open("FMDV_Kenya_plaques_refs_3A-B-C-D.fa", "w") as out:
    AlignIO.write(alignment[:,4276:], out, "fasta")

Lpro   = AlignIO.read("FMDV_Kenya_plaques_refs_Lpro.fa",     "fasta")
VP231  = AlignIO.read("FMDV_Kenya_plaques_refs_VP2-3-1.fa",  "fasta")
TABC   = AlignIO.read("FMDV_Kenya_plaques_refs_2A-B-C.fa",   "fasta")
TABCD  = AlignIO.read("FMDV_Kenya_plaques_refs_3A-B-C-D.fa", "fasta")

print("Alignment length Lpro %i" % Lpro.get_alignment_length())
print("Alignment length VP231 %i" % VP231.get_alignment_length())
print("Alignment length 2ABC %i" % TABC.get_alignment_length())
print("Alignment length 3ABCD %i" % TABCD.get_alignment_length())

# Arguments ----------
parser = argparse.ArgumentParser()
parser.add_argument("fasta", help = "Path to .fasta file")
parser.add_argument("regions", help = "Path to .csv file containing name of region, start, and end sites")

