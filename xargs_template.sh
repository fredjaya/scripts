#!/bin/bash

ls *.fa | xargs -I {} -n 1 -P 12 sh -c "do_thing {}"
