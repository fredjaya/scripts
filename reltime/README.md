# Retrieve RelTime node ages

`get_node_age.py` parses a RelTime tree output (.nex) to output a .csv of the estimated divergence times and their 95% confidence intervals for each node. 

## Dependencies
- python 3
- pandas
- numpy

## Usage
```
python3 get_node_age.py <reltime_file> <output_name>
```

To show the help message and argument description:
```
python3 get_node_age.py -h
```

## Notes
This script has been written based on a single RelTime output and may not reflect all use cases.

Currently, `get_node_age.py` can only match divergence times in scientific notation, and nodes are output in order of appearance based in the newick file.

No unit tests were written and manual inspection/validation of the output .csv is advised, particularly when comparing with trees output by other programs i.e. BEAST.

## Further work
- [ ] Develop unit tests
- [ ] Validate script with other outputs
- [ ] Modify regex to match all number formats (not just sci. notation)
- [ ] Retrieve additional node information
- [ ] Intuitive node labelling
