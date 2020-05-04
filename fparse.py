#!/usr/bin/env python3

import fobjects
import re

#parses the SnpEff annotated file. Only pulls out the prediction for the first transcript. Returns a list of variant objects with attributes id, loc, gene, gt, vartype, sepred. (rs, anpred, sig, and dn are None)
def SEparse(path):
    varlist = []
    id = 0

    for line in open(path):
        if not line.startswith("#"):
            cols = line.rstrip().split("\t")
            alts = cols[4].split(",")
            for i in alts:
                loc = cols[0] + ">" + cols[1] + ":" + cols[3] + "/" + i
                info = cols[7].split("|")
                sevartype = info[1]
                sepred = info[2]
                gene = info[3]
                h= cols[9].split(":")
                gt = h[0]
                id += 1
                var = fobjects.variant(id=id, loc=loc, gene=gene, gt=gt, sevartype=sevartype, sepred=sepred)
                varlist.append(var)

    return varlist


#parses the ANNOVAR annotated file. Only pulls out the prediction from MutationTaster. Returns a list of variant objects with attributes id, loc, gene, gt, rs, vartype, anpred. (sepred, sig, and dn are None) If an attribute is missing it is None.
def ANparse(path):
    varlist = []
    id = 0

    for line in open(path):
        if not line.startswith("#"):
            cols = line.rstrip().split("\t")
            alts = cols[4].split(",")
            for i in alts:
                loc = cols[0] + ">" + cols[1] + ":" + cols[3] + "/" + i
                h = cols[9].split(":")
                gt = h[0]
                info = cols[7]
                m = re.search("Func.refGene=([^;]+);", info)
                if m:
                    anvartype = m.group(1)
                else:
                    anvartype = "."
                m2 = re.search("avsnp147=([^;]+);", info)
                if m2:
                    rs = m2.group(1)
                else:
                    rs = "."
                m3 = re.search("Gene.refGene=([^;]+);", info)
                if m3:
                    gene = m3.group(1)
                else:
                    gene = "."
                m4 = re.search("MutationTaster_pred=([^;]+);", info)
                if m4:
                    anpred = m4.group(1)
                else:
                    anpred = "."
                id += 1
                var = fobjects.variant(id=id, loc=loc, gene=gene, gt=gt, rs=rs, anvartype=anvartype, anpred=anpred)
                varlist.append(var)
            
    return varlist


#parses the CLINVAR annotated file. Returns a list of variant objects with attributes id, loc, vartype, sig, dn. (gene, gt, sepred, and anpred are None) If an attribute is missing it is None.
def CLINparse(path):
    varlist = []
    id = 0
    
    for line in open(path):
        if not line.startswith("#"):
            #id is assigned based on line number so that each variant will have a unique id in the database
            id += 1
            cols = line.rstrip().split("\t")
            loc = cols[0] + ">" + cols[1] + ":" + cols[3] + "/" + cols[4]
            info = cols[7]
            m = re.search("CLNVC=([^;]+);", info)
            if m:
                clinvartype = m.group(1)
            else:
                clinvartype = "."
            m2 = re.search("CLNSIG=([^;]+);", info)
            if m2:
                sig = m2.group(1)
            else:
                sig = "."
            m3 = re.search("CLNDN=([^;]+);", info)
            if m3:
                dn = m3.group(1)
            else:
                dn = "."

            var = fobjects.variant(id=id, loc=loc, clinvartype=clinvartype, sig=sig, dn=dn)
            varlist.append(var)
            

    return varlist

"""
file = "22snpeff.vcf"
variants = SEparse(file)
for i in variants:
    print(i.loc)


file2 = "22annovar.vcf"
variants2 = ANparse(file2)
for i in variants2:
    i.format_gt(i.gt)
    i.format_anpred(i.anpred)
    print(i.gt)
    print(i.anpred)


file3 = "clinvar.vcf"
variants3 = CLINparse(file3)
for i in variants3:
    print(i.loc)

"""
