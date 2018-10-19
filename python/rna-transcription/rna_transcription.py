def to_rna(dna_strand):
    rna_to_dna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    
    rna = ""
    for letter in dna_strand:
        if letter in rna_to_dna.keys():
           letter = rna_to_dna[letter]

        rna += letter

    return rna
