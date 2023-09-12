# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

f = open("NM_207618.2.fasta","r")
sequence = f.read()
sequence

with open("NM_207618.2.fasta","r") as inf:
    data = inf.read().splitlines(True)
with open('dna1.txt','w') as outf:
    outf.writelines(data[1:])
f = open("dna1.txt","r")
sequence = f.read()
sequence

print(sequence)

sequence = sequence.replace('\n','')
sequence

sequence = sequence.replace('\r','')
sequence = sequence.replace(' ','')
sequence[0:3]

genetic_code = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

genetic_code['ATA']


# +
def read_seq(inputfile):
    with open(inputfile,'r') as f:
        sequence = f.read()
    sequence = sequence.replace(' ','')
    sequence = sequence.replace('\n','')
    sequence = sequence.replace('\r','')
    return sequence

with open('NM_207618.2.fasta','r') as inf:
    data = inf.read().splitlines(True)

with open('dna.txt','w') as outf:
    outf.writelines(data[1:])
    
dna = read_seq('dna.txt')
print(dna)


# +
def convert(seq):
    """DNA 시퀸스를 아미노산 시퀸스로 변환"""
    genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    
    if len(seq) % 3 == 0:    # 데이터 길이가 3의 배수이면 아래를 실행
        for i in range(0,len(seq),3):
            codon = seq[i:i+3]
            protein += genetic_code[codon]
    return protein

print(convert(dna[20:938]))
# -

print(convert(dna[20:935]))

prot = read_seq('protein.txt')
print(prot)

prot == convert(dna[20:935])
