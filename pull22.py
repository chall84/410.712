#!/usr/bin/env python3

file = "GRCh37_latest_clinvar.vcf"
newfile = open("22clinvar.vcf", "w")

for line in open(file):
    if line.startswith("22"):
        newfile.write(line)
    
