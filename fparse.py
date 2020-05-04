#!/usr/bin/env python3

import fobjects
import re

def SEparse(path):
    varlist = []
    id = 0

    for line in open(path):
        if not line.startswith("#"):
            id +=1
            cols = line.rstrip().split("\t")
            info = cols[7].split("|")
            h= cols[9].split(":")
            loc = cols[0] + ">" + cols[1]
            ref = cols[3]
            alt = cols[4]
            vartype = info[1]
            sepred = info[2]
            gene = info[3]
            gt = h[0]
            variants = fobjects.variant(id=id, loc=loc, ref=ref, alt=alt, gene=gene, gt=gt, rs=".",vartype=vartype, sepred=pred)
            varlist.append(variants)

    return varlist

def ANparse(path):
    varlist = []
    id = 0

    for line in open(path):
        if not line.startswith("#"):
            id+=1
            cols = line.rstrip().split("\t")
            info = cols[7]
            h = cols[9].split(":")
            loc = cols[0] + ">" + cols[1]
            ref = cols[3]
            alt = cols[4]
            gt = h[0]
            m = re.search("Func.refGene=([^;]+);", info)
            if m:
                vartype = m.group(1)
            m2 = re.search("avsnp147=([^;]+);", info)
            if m2:
                rs = m2.group(1)
            m3 = re.search("Gene.refGene=([^;]+);", info)
            if m3:
                gene = m3.group(1)
            m4 = re.search("MutationTaster_pred=([^;]+);", info)
            if m4:
                anpred = m4.group(1)
            variants = fobjects.variant(id=id, loc=loc, ref=ref, alt=alt, gene=gene, gt=gt, rs=rs, vartype=vartype, anpred=anpred)
            varlist.append(variants)
            
    return varlist
        
def snpparse(path):
    rslist = []
    for line in open(path):
        line = line.rstrip()
        m = re.search("\d+.\s(rs\d+)", line)
        if m:
            rs = m.group(1)
        m2 = re.search("SNV:(.*)", line)
        if m2:
            change = m2.group(1)
            snps = fobjects.dbsnp(rs=rs, change=change)
            rslist.append(snps)

    return rslist


file = "snp_result.txt"

snp = snpparse(file)
for i in snp:
    print(i.rs + " " + i.change)

#SE = ANparse(file)
#for i in SE:
   # print(str(i.id) + i.loc + i.ref + i.alt + i.gene + i.gt + i.rs + i.vartype + i.anpred)

#use objects to transform output to .=Null and pred=. to MODIFIER and A = Very High
