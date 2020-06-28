import re
import pandas as pd
import numpy as np
import argparse

def read_reltime(file_path):
    '''
    Read in a reltime output tree file (.nex) into memory for parsing
    '''
    f = open(file_path, 'r')
    f = f.read()
    return f

"""
def get_internal_node(reltime_file):
    r = re.compile('\d+\[\&.*?\]\:\d+\.\d+E[\+\-]\d+')
    nodes = re.findall(r, reltime_file)
    return nodes

def get_node_num(nodes):
    r = re.compile('^\d+')
    node_num = re.findall(r, nodes)
    return node_num

def get_node_age(nodes):
    r = re.compile('(?<=\:).*$')
    node_age = re.findall(r, nodes)
    return node_age

def parse_nodes(nodes):
    for i in nodes:
        node_num = get_node_num(i)
        node_age = get_node_age(i)
        print(node_num, node_age)
    return
"""

def get_divtimes(reltime_file):
    '''
    In the reltime newick line, retrieve all node divtimes in order of appearance (sci. not. only)
    '''
    r = re.compile('(?<=divtime\=)\d+\.\d+E[\+\-]\d+')
    divtimes = re.findall(r, reltime_file)
    return divtimes

def get_ci(reltime_file):
    '''
    In the reltime newick line, retrieve the upper and lower confidence intervals (95%) for estimated divtimes (sci. not. only) 
    '''
    r = re.compile('(?<=divtime\_95\%\_CI\=\{).*?(?=\})')
    ci = re.findall(r, reltime_file)
    return ci

def prep_df(divtimes, cis):
    '''
    Concatenate divtimes and confidence intervals in a single dataframe
    '''
    df = pd.DataFrame({'divtimes':divtimes, 
                       'cis':cis})
    df[['lower_ci', 'upper_ci']] = df['cis'].str.split(",", expand = True)
    df = df.drop(columns = ['cis'])
    df.index = np.arange(1, len(divtimes) + 1)
    return df
    
def main(file_path, out_name):
    reltime_file = read_reltime(file_path)
    divtimes = get_divtimes(reltime_file)
    cis = get_ci(reltime_file)
    df = prep_df(divtimes, cis)
    df.to_csv(out_name)
    return df

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("reltime_file", help = "path to reltime tree (.nex)")
parser.add_argument("output_name", help = "name of output file (.csv)")
args = parser.parse_args()

# Main
main(args.reltime_file, args.output_name)
