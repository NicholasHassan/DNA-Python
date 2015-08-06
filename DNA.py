import os
os.getcwd()

file = open("dna2.fasta")
file.seek(0)
dna = file.read()
seq = dna.split(">")
del seq[0]

for i in range(len(seq)):
    seq[i] = seq[i].split("shotgun sequence")
    del seq[i][0]
    seq[i] = seq[i][0]


seq2 = [""] * len(seq)
for i in range(len(seq)):
    for j in range(len(seq[i])):
        if seq[i][j] == "\n":
            pass
        else:
            seq2[i] = seq2[i] + seq[i][j] 
    seq[i] = seq2[i]

max_length = 0
for i in range(len(seq)):
    max_length = max(max_length, len(seq[i]))

min_length = 1e7
for i in range(len(seq)):
    min_length = min(min_length, len(seq[i]))
    

