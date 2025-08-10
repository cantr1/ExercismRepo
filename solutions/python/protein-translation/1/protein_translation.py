def proteins(strand):
    amino_acids = []
    n = 3

    rna_strands = [strand[i:i+n] for i in range(0, len(strand), n)]

    for item in rna_strands:
        if item == 'AUG':
            amino_acids.append("Methionine")
        elif item == 'UUU' or item == 'UUC':
            amino_acids.append("Phenylalanine")
        elif item == 'UUA' or item == 'UUG':
            amino_acids.append("Leucine")
        elif item == 'UCU' or item == 'UCC' or item == 'UCA' or item == 'UCG':
            amino_acids.append("Serine")
        elif item == 'UAU' or item == 'UAC':
            amino_acids.append("Tyrosine")
        elif item == 'UGU' or item == 'UGC':
            amino_acids.append("Cysteine")
        elif item == 'UGG':
            amino_acids.append("Tryptophan")
        else:
            break

    return amino_acids
        