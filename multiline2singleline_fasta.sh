#!/bin/bash

# Author: Jorge Amigo (Biostars)
# https://www.biostars.org/p/9262/#118460

perl -pe '$. > 1 and /^>/ ? print "\n" : chomp' in.fa > out.fa
