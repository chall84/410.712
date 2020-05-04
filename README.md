# 410.712
Multianalysis VCF Viewer allows the user to view SnpEff, ANNOVAR and ClinVar annotations at the same time, easily comparing the predictions and clinical data for each variant in a genome. To view the example data (which is the snp variants on my chromosome 22) skip to Step 3.

1. Obtain the input files:

First run the analyses on YOUR_INPUT.vcf and download the appropriate ClinVar reference file. The reference genome version for your vcf will be listed in the ## comments at the top of the file. The example commands below use hg19 as the reference genome.

SnpEff annotated VCF file
    • Dowload and unzip SnpEff to install (available here: http://snpeff.sourceforge.net/download.html)
    • Run SnpEff with this command : java -Xmx4g -jar snpEff.jar GRCh37.75 YOUR_INPUT.vcf > YOUR_OUT.ann.vcf
        ◦ Match the genome version to the reference version in YOUR_INPUT.vcf
        ◦ -Xmx4g sets the maximum heap size to 4g
        ◦ -jar runs the file snpEff.jar
        ◦ The manual is available here: http://snpeff.sourceforge.net/SnpEff_manual.html#run
ANNOVAR annotated VCF file
    • Dowload an install ANNOVAR (you must ask for a link to download here: http://download.openbioinformatics.org/annovar_download_form.php)
    • Download the refGene and avsnp147 databases
        ◦ Make sure to select the genome version that is the reference for the input VCF
        ◦ annotate_variation.pl -buildver hg19 -downdb -webfrom annovar refGene humandb/
        ◦ annotate_variation.pl -buildver hg19 -downdb -webfrom annovar avsnp147 humandb/ 
            ▪ -buildver should be the reference genome used in YOUR_INPUT.vcf
            ▪ These commands put these databases in the humandb folder within ANNOVAR
    • Run ANNOVAR with this command: table_annovar.pl YOUR_INPUT.vcf humandb/ -buildver hg19 -out YOUR_OUT -remove -protocol refGene,avsnp147 -operation g,f -nastring . -vcfinput -polish
        ◦ -buildver should be the reference genome used in YOUR_INPUT.vcf
        ◦ -remove removes the temporary files
        ◦ - protocol refGene,avsnp147 specifies the databases to be used
        ◦ - operation g,f specifes the database operations to gene and filter respectively
        ◦ -nastring . Sets the null value to a full stop
        ◦ -vcfinput specifies that the input file is a VCF
        ◦ -polish polishes the protein notation for indels
        ◦ The manual is available here: http://annovar.openbioinformatics.org/en/latest/user-guide/startup/
ClinVar VCF file
    • Download the ClinVar VCF
        ◦ Choose the genome that matches the reference genome in YOUR_INPUT.vcf
        ◦ Easy access download here: https://www.ncbi.nlm.nih.gov/genome/guide/human/
        ◦ Or download from the FTP; https://www.ncbi.nlm.nih.gov/clinvar/docs/ftp_primer/

2. Create the database:

Run create_db.py
    • Create the database with this command: ./create_db.py -a YOUR_ANNOVAR_FILE.vcf -s YOUR_SNPEFF_FILE.vcf -c YOUR_CLINVAR_FILE.vcf
    • 22annovar.vcf, 22snpeff.vcf and 22clinvar.vcf contain the example data
    • ANNOVAR runs a multianalysis but for this project only the MutationTaster predictions are parsed out.
    • SnpEff makes predictions for each transcript the variant overlaps but for this project only the prediction for the first transcript is parsed out.
      
3.  View the results:
    • Go to http://bfx3.aap.jhu.edu/chall84/final/fdisplay.html
        ◦ Search by gene is an exact match. Use the autocomplete for best results.
        ◦ Search by rs (reference snp from dbSNP) is an exact match. There is no autocomplete.
        ◦ SnpEff prediction and ANNOVAR prediction are an exact match. Use the list for best results.
        ◦ Search by diagnosis and clinical significance are not an exact match. 
            ▪ Only variants from YOUR_INPUT.vcf will be shown in the results so diagnoses that do not overlap the input variants will have no results.
    • Location column
        ◦ Location is in the format chromosome number > variant start location : reference allele/alternate allele
    • Gene column
        ◦ Pulled from the SnpEff file
        ◦ Intergenic variants sometimes have more than one gene listed
    • Genotype column
        ◦ HM = homozygous
        ◦ HT = heterozygous
        ◦ CHT = compound heterozygous
        ◦ homozygous and compound heterozygous variants are shaded
    • Clinical Diagnosis column
        ◦ Pulled from the ClinVar file
        ◦ Mutiple diagnoses are separated by “|”
    • RS column
        ◦ Pulled fom the ANNOVAR file
        ◦ As current as the ANNOVAR avsnp147 database
    • Clinical Significance column
        ◦ Pulled from the ClinVar file
        ◦ Is specific to the variant allele, not just the location of the variant
    • ClinVar variant type column
        ◦ Refers to the type of mutation rather than its location as the other variant types do
    • SnpEff prediction column
        ◦ More information on interpreting SnpEff predictions is available here: http://snpeff.sourceforge.net/SnpEff_manual.html#input (see Impact prediction category)
    • SnpEff variant type column
        ◦ SnpEff predictions are made based on variant type
    • ANNOVAR prediction column
        ◦ More information on interpreting MutationTaster predictions (provided by ANNOVAR) is available here: http://www.mutationtaster.org/info/documentation.html (see Output category)
    • ANNOVAR variant type column
        ◦ Pulled from the functional refGene annotation in the ANNOVAR file
