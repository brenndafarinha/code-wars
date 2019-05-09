def dna_strand(dna):
    return dna.translate(str.maketrans('ATGC', 'TACG'))




print(dna_strand('ATCG'))

