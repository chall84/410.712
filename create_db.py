#!/usr/bin/env python3

import argparse
import fqry

parser = argparse.ArgumentParser(description="Build the database for the VCF Viewer")
parser.add_argument("-a", "--annovar_file", type=str, required=True, help="A VCF that has been annotated by ANNOVAR")
parser.add_argument("-s", "--snpeff_file", type=str, required=True, help="A VCF that has been annotated by snpEff")
parser.add_argument("-c", "--clinvar_file", type=str, required=True, help="A VCF that has been downloaded from ClinVar")
args = parser.parse_args()

fqry.create_db(args.snpeff_file, args.annovar_file, args.clinvar_file)
