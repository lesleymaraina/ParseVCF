################################################
#About
#Remove VCF Header
################################################

import os

print __file__

def remove_text(file_name, text):
	lines = []
	new_lines = []

	with open(file_name, 'r') as text_file:
		lines = text_file.readlines()
	for line in lines:
		if text not in line:
			new_lines.append(line)
	with open(file_name, 'w') as text_file:
		for line in new_lines:
			text_file.write(line)

	print
	print lines

file_name= __file__.split('/')[-1]
print file_name
files_in_dir=os.listdir('./')

files_in_dir.remove(file_name)
# files_in_dir.remove('.DS_Store')
print files_in_dir

for file_ in files_in_dir:
	# remove_text(file_, '##fileformat=VCFv4.1')
	# remove_text(file_, '##fileDate=20160817')
	# remove_text(file_, '##ALT=<ID=DEL,Description="Deletion">')
	# remove_text(file_, '##INFO=<ID=END,Number=1,Type=Integer,Description="End position of the structural variant">')
	# remove_text(file_, '##INFO=<ID=MAPQ,Number=1,Type=Integer,Description="Median mapping quality of paired-ends')
	# remove_text(file_, '##INFO=<ID=RE,Number=1,Type=Integer,Description="read support">')
	# remove_text(file_, '##INFO=<ID=IMPRECISE,Number=0,Type=Flag,Description="Imprecisetructural variation">')
	# remove_text(file_, '##INFO=<ID=PRECISE,Number=0,Type=Flag,Description="Precise structural variation">')
	# remove_text(file_, '##INFO=<ID=SVLEN,Number=1,Type=Integer,Description="Length of the SV">')
	# remove_text(file_, '##INFO=<ID=SVMETHOD,Number=1,Type=String,Description="Type of approacused to detect SV">')
	# remove_text(file_, '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">')
	# remove_text(file_, '##FORMAT=<ID=LN,Number=1,Type=Integer,Description="predictelength">')
	# remove_text(file_, '##FORMAT=<ID=DV,Number=1,Type=Integer,Description="# supporting varit reads">')
	# remove_text(file_, '##FORMAT=<ID=TY,Number=1,Type=String,Description="Types">')
	# remove_text(file_, '##FORMAT=<ID=CO,Number=1,Type=String,Description="Coordites">')
	# remove_text(file_, '#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT')
	# remove_text(file_, '##INFO=<ID=END,Number=1,Type=Integer,Description="End position of the structural variant">')
	# remove_text(file_, '##INFO=<ID=MAPQ,Number=1,Type=Integer,Description="Median mapping quality of paired-ends">')
	# remove_text(file_, '##INFO=<ID=RE,Number=1,Type=Integer,Description="read support">')
	# remove_text(file_, '##INFO=<ID=IMPRECISE,Number=0,Type=Flag,Description="Imprecise structural variation">')
	# remove_text(file_, '##INFO=<ID=PRECISE,Number=0,Type=Flag,Description="Precise structural variation">')
	# remove_text(file_, '##INFO=<ID=SVLEN,Number=1,Type=Integer,Description="Length of the SV">')
	# remove_text(file_, '##INFO=<ID=SVMETHOD,Number=1,Type=String,Description="Type of approach used to detect SV">')
	# remove_text(file_, '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">')
	# remove_text(file_, '##FORMAT=<ID=LN,Number=1,Type=Integer,Description="predicted length">')
	# remove_text(file_, '##FORMAT=<ID=DV,Number=1,Type=Integer,Description="# supporting variant reads">')
	# remove_text(file_, '##FORMAT=<ID=TY,Number=1,Type=String,Description="Types">')
	# remove_text(file_, '##FORMAT=<ID=CO,Number=1,Type=String,Description="Coordinates">')
	# remove_text(file_, '#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	')
	remove_text(file_, '##ALT=<ID=DUP,Description="Duplication">')
	remove_text(file_, '##ALT=<ID=INV,Description="Inversion">')
	remove_text(file_, '##ALT=<ID=TRA,Description="Translocation">')
	remove_text(file_, '##ALT=<ID=INS,Description="Insertion">')
	remove_text(file_, '##INFO=<ID=CHR2,Number=1,Type=String,Description="Chromosome for END coordinate in case of a translocation">')
